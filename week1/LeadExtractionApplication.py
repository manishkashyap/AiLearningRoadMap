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


LeadExtractionOutput = LeadExtraction


LEAD_EXTRACTION_INSTRUCTIONS = """
You are a deterministic lead extraction assistant.

Your job is to classify a customer/prospect message into exactly ONE primary intent and extract structured lead information.

Return LeadExtraction for all meaningful business, product, pricing, demo, integration, documentation, security, migration, or support messages.

Return LeadExtraction with intent="unknown" and next_action="no_action" only when the message is random, spam-like, casual with no business intent, or impossible to understand.

IMPORTANT:
- Choose exactly one primary intent.
- Do not return multiple intents.
- Do not infer demo_request unless the user explicitly asks for a demo, call, meeting, walkthrough, or sales conversation.
- Do not infer support_request unless the user reports a problem, issue, error, failure, breakage, or says they are already using the product and need help.
- If the message asks about API docs, integration, security, migration, comparison, or how a feature works, classify it as product_inquiry, not support_request.
- If the message asks both demo and pricing, classify as demo_request because the strongest next action is to schedule a call.
- If the message asks both product capability and pricing, classify as pricing_inquiry only if pricing/cost/commercials is the main ask.
- If the message asks both product capability and demo, classify as demo_request only if demo/call/meeting is explicitly requested.

Intent definitions:

1. support_request
Use only when:
- user reports something is not working
- user says campaign/journey/segment/API/email/push/notification is broken
- user says they are already using WebEngage and need help
- user expresses urgency around an issue

Examples:
"Our campaigns are not going out."
"Share API documentation."
"We are already using WebEngage and segments are not updating."
"Urgent, journeys are stuck."

next_action: create_support_ticket

2. demo_request
Use only when:
- user explicitly asks for demo
- user asks to schedule a call
- user wants a walkthrough
- user wants to speak with sales/team

Examples:
"Can I get a demo?"
"Please arrange a call."
"We want to speak to your sales team."
"I would like a walkthrough."

next_action: schedule_call

3. pricing_inquiry
Use only when:
- main ask is pricing, cost, commercial details, quote, plan, package, or billing

Examples:
"Please send pricing."
"What is the cost?"
"pricing for your platform"
"Share commercial details."

next_action: send_pricing

4. product_inquiry
Use when:
- user asks about product capability
- user asks how something works
- user asks about integrations
- user asks for API documentation
- user asks about migration
- user asks about security/compliance
- user asks competitor comparison
- user asks to call
- user expresses interest but does not explicitly request demo/pricing/support

Examples:
"How does abandoned cart recovery work?"
"Do you support Shopify?"
"How is WebEngage different from CleverTap?"
"We want to integrate WebEngage with our mobile app."
"Our security team needs compliance details."

next_action:
- send_documentation for API/docs/security/integration/how-it-works/comparison/migration
- schedule_call only if the user explicitly asks for call/demo/meeting
- no_action only for unknown

5. unknown
Use only when:
- message is random text
- message is spam
- message has no business/product/support/sales intent
- message is impossible to understand

Examples:
"asdf qwer zzzz"
"Congratulations you won a free iPhone"
"Hey, hope you are doing well"

next_action: no_action

Urgency rules:
- high: urgent issue, production impact, customers affected, deadline today/tomorrow, escalation
- medium: active evaluation, asks this week, vendor finalization, asks for demo/pricing
- low: general information, documentation, casual product exploration

Field rules:
- business_type can be null if not mentioned.
- use_case can be null if not mentioned.
- confidence must be between 0 and 1.
- confidence should be below 0.6 for vague messages.
- next_action must match the selected primary intent.
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
        self
    ):
        self.model_gateway = ModelGateway(
            output_type=LeadExtractionOutput,
            instructions=LEAD_EXTRACTION_INSTRUCTIONS,
            output_validator=validate_lead_output
        )

    def extract_structured_data(
        self,
        raw_lead_text: str,
        retries: int = 1,
    ) -> LeadExtractionOutput:
        return self.model_gateway.run(raw_lead_text, retries=retries)


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
    "product_inquiry": [5, 6, 8, 9, 11, 12, 13, 21, 22, 26, 27, 28, 29],
    "pricing_inquiry": [2, 23],
    "demo_request": [1, 3, 10, 15, 18, 24, 30],
    "support_request": [4, 7, 14, 20],
    "unknown": [16, 17, 25]
}


output_123 = {
    'product_inquiry': [5, 6, 8, 9, 11, 12, 13, 21, 22, 26, 27, 28, 29], 
    'pricing_inquiry': [2, 23], 
    'demo_request': [1, 3, 10, 15, 18, 19, 24, 30], 
    'support_request': [4, 7, 14, 20], 
    'unknown': [16, 17, 25]
}

if __name__ == "__main__":
    lead_extraction_application = LeadExtractionApplication()
    output_dict = dict(product_inquiry=[], pricing_inquiry=[], demo_request=[], support_request=[], unknown=[])
    for i, message in enumerate(raw_lead_messages) :
        output = lead_extraction_application.extract_structured_data(message, 1)
        print(output)
        output_dict[output.intent].append(i+1)  
        
    print(output_dict)
    

