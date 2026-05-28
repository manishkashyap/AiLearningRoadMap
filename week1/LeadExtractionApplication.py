from typing import Literal, Optional

from pydantic import BaseModel, Field
from pydantic_ai import ModelRetry, RunContext

try:
    from .ModelGateway import ModelGateway
except ImportError:
    from ModelGateway import ModelGateway


class LeadExtraction(BaseModel):
    business_type: Optional[str] = None

    intent: Literal[
        "product_inquiry",
        "pricing_inquiry",
        "demo_request",
        "support_request",
        "unknown",
    ]

    use_case: Optional[str] = None

    urgency: Literal["low", "medium", "high"]

    next_action: Literal[
        "schedule_call",
        "send_pricing",
        "send_documentation",
        "create_support_ticket",
        "no_action",
    ]

    confidence: float = Field(ge=0.0, le=1.0)


class InvalidLeadMessage(BaseModel):
    error_message: str


LeadExtractionOutput = LeadExtraction | InvalidLeadMessage


LEAD_EXTRACTION_INSTRUCTIONS = """
You are a lead extraction assistant.

Extract structured information from customer or prospect messages.

Return LeadExtraction when the message contains a meaningful business, product, pricing, demo, or support intent.

Return InvalidLeadMessage only when the message is random, meaningless, spam-like, or impossible to understand.

Rules:
- business_type can be null if not mentioned.
- use_case can be null if not mentioned.
- confidence must be between 0 and 1.
- urgency should be high only if the user shows immediate need, issue, escalation, or time pressure.
- next_action must be selected from the allowed enum.
"""


async def validate_lead_output(
    ctx: RunContext,
    model_output: LeadExtractionOutput,
) -> LeadExtractionOutput:
    if ctx.partial_output:
        return model_output

    if not isinstance(model_output, InvalidLeadMessage) and not isinstance(
        model_output,
        LeadExtraction,
    ):
        raise ModelRetry("Output must be a LeadExtraction or InvalidLeadMessage.")

    if isinstance(model_output, InvalidLeadMessage):
        return model_output

    if model_output.confidence < 0.4 and model_output.intent != "unknown":
        raise ModelRetry(
            "Confidence is too low for a specific intent. "
            "Either increase confidence with better reasoning or classify intent as unknown."
        )

    if model_output.intent == "pricing_inquiry" and model_output.next_action != "send_pricing":
        raise ModelRetry("For pricing_inquiry, next_action should usually be send_pricing.")

    if model_output.intent == "demo_request" and model_output.next_action != "schedule_call":
        raise ModelRetry("For demo_request, next_action should usually be schedule_call.")

    return model_output


class LeadExtractionApplication:
    def __init__(
        self,
        model_name: str = "gemma3:12b",
        base_url: str = "http://localhost:11434/v1",
    ):
        self.model_gateway = ModelGateway(
            output_type=LeadExtractionOutput,
            instructions=LEAD_EXTRACTION_INSTRUCTIONS,
            output_validator=validate_lead_output,
            model_name=model_name,
            base_url=base_url,
        )

    def extract_structured_data(
        self,
        raw_lead_text: str,
        retries: int = 1,
    ) -> LeadExtractionOutput:
        return self.model_gateway.run(raw_lead_text, retries=retries)
