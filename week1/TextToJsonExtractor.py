from pydantic import BaseModel,Field
from pydantic_ai import Agent, NativeOutput, RunContext, ModelRetry
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.ollama import OllamaProvider
from typing import Literal, Optional


raw_lead_messages = [
    # 1. Product inquiry
    "Hi, I run a Shopify store and want to try WebEngage for abandoned cart recovery. Please call me tomorrow.",

    # 2. Pricing inquiry
    "Can you send me pricing details for WhatsApp and email campaigns? We are comparing a few tools this week.",

    # 3. Demo request
    "We are a D2C skincare brand and would like to schedule a demo of your marketing automation platform.",

    # 4. Support request
    "Our email campaigns are not going out since morning. This is impacting our sale. Need help urgently.",

    # 5. Documentation request
    "Please share your API documentation. Our engineering team wants to check how user events can be pushed to WebEngage.",

    # 6. Integration inquiry
    "We want to integrate WebEngage with our mobile app to trigger push notifications based on user behavior.",

    # 7. High urgency support
    "Urgent issue. Our journey is stuck and customers are not receiving OTP and transactional notifications.",

    # 8. Vague but valid inquiry
    "Hi, I want to know more about WebEngage for my business.",

    # 9. Unknown business type
    "Can someone explain how abandoned cart automation works and whether it supports WhatsApp reminders?",

    # 10. Multi-intent: pricing + demo
    "I want to see a demo and also understand pricing for your customer engagement platform.",

    # 11. Enterprise lead
    "We are evaluating customer engagement platforms for a large BFSI client with 10 million monthly active users.",

    # 12. Shopify-specific
    "I have a Shopify Plus store and want to recover abandoned carts using email, SMS, and WhatsApp.",

    # 13. Mobile app use case
    "We have an Android and iOS app. We want to send personalized push notifications when users drop off before checkout.",

    # 14. Support but not urgent
    "I am unable to find where to configure email templates inside the dashboard. Can you help?",

    # 15. Sales-qualified lead
    "We are planning to migrate from MoEngage and would like to speak to your sales team this week.",

    # 16. Random invalid text
    "asdf qwer zzzz plmokn 123123 !!!",

    # 17. Spam-like text
    "Congratulations you have won a free iPhone. Click here now to claim your reward.",

    # 18. Hindi-English mixed
    "Mera ecommerce store hai aur mujhe abandoned cart ke liye WhatsApp automation chahiye. Demo mil sakta hai kya?",

    # 19. Low confidence / ambiguous
    "Need automation. Call me.",

    # 20. Existing customer issue
    "We are already using WebEngage and our segments are not updating properly since yesterday.",

    # 21. API/event tracking use case
    "Our backend team wants to send purchase and cart events to WebEngage through API. Please guide us.",

    # 22. Campaign creation help
    "I need help creating a campaign for users who installed the app but did not complete registration.",

    # 23. Pricing urgency
    "Please send commercial details today. We need to finalize a vendor by tomorrow.",

    # 24. Demo but no business context
    "Can I get a demo of the platform sometime this week?",

    # 25. Non-lead casual message
    "Hey, hope you are doing well. Just checking in after a long time.",

    # 26. Competitor comparison
    "How is WebEngage different from CleverTap and MoEngage for ecommerce retention?",

    # 27. Data migration use case
    "We want to migrate customer profiles and historical events from our old engagement tool to WebEngage.",

    # 28. Enterprise security inquiry
    "Before we proceed, our security team needs details about data residency, encryption, and compliance certifications.",

    # 29. Bad grammar but meaningful
    "Need webengage for my online store user come site not buy product want send message after leave cart.",

    # 30. Very clear high-quality lead
    "Hi, I lead growth for a fashion ecommerce brand doing 50k monthly orders. We want to automate abandoned cart, winback, and repeat purchase campaigns across email, WhatsApp, and push. Please arrange a demo."
]

expected_behavior = {
    "product_inquiry": [1, 6, 8, 9, 11, 12, 13, 21, 22, 26, 27, 28, 29, 30],
    "pricing_inquiry": [2, 10, 23],
    "demo_request": [3, 10, 15, 18, 24, 30],
    "support_request": [4, 7, 14, 20],
    "unknown_or_invalid": [16, 17, 25]
}


class LeadExtraction(BaseModel):
    business_type: Optional[str] = None

    intent: Literal[
        "product_inquiry",
        "pricing_inquiry",
        "demo_request",
        "support_request",
        "unknown"
    ]

    use_case: Optional[str] = None

    urgency: Literal["low", "medium", "high"]

    next_action: Literal[
        "schedule_call",
        "send_pricing",
        "send_documentation",
        "create_support_ticket",
        "no_action"
    ]

    confidence: float = Field(ge=0.0, le=1.0)


class InvalidLeadMessage(BaseModel):
    error_message: str

output = LeadExtraction | InvalidLeadMessage


class TextToJsonExtractor:
    def __init__(
        self,
        model_name: str = "gemma3:12b",
        base_url: str = "http://localhost:11434/v1",
    ):
        # Explicitly pass the local Ollama API endpoint.
        ollama_model = OpenAIChatModel(
            model_name=model_name,
            provider=OllamaProvider(base_url=base_url),
        )

        self.model = Agent(
            model=ollama_model,
            output_type=NativeOutput(output),
            instructions="""
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
            """,
        )

        @self.model.output_validator
        async def validateOutput(ctx: RunContext, model_output: output) -> output:
            if ctx.partial_output:
                return model_output
            
            if not isinstance(model_output, InvalidLeadMessage) and not isinstance(model_output, LeadExtraction):
                raise ModelRetry("Output must be a LeadExtraction or InvalidLeadMessage.")

            if isinstance(model_output, InvalidLeadMessage):
                return model_output

            if model_output.confidence < 0.4 and model_output.intent != "unknown":
                raise ModelRetry(
                    "Confidence is too low for a specific intent. "
                    "Either increase confidence with better reasoning or classify intent as unknown."
                )

            if model_output.intent == "pricing_inquiry" and model_output.next_action != "send_pricing":
                raise ModelRetry(
                    "For pricing_inquiry, next_action should usually be send_pricing."
                )

            if model_output.intent == "demo_request" and model_output.next_action != "schedule_call":
                raise ModelRetry(
                    "For demo_request, next_action should usually be schedule_call."
                )

            return model_output

    def extract(self, lead_query_text: str, retries: int = 1) -> output:
        result = self.model.run_sync(lead_query_text, retries=retries)
        return result.output


if __name__ == "__main__":
    extractor = TextToJsonExtractor()

    for query in raw_lead_messages:
        result = extractor.extract(query, retries=1)
        print("======================================================\n")
        print(query)
        print("======================================================\n")
        print(repr(result))
        print("======================================================\n")




