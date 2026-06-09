from string import Formatter
from typing import Any, Literal

from pydantic import BaseModel, Field
from pydantic_ai import ModelRetry, RunContext
from pydantic_ai.usage import RunUsage

try:
    from .ModelGateway import ModelGateway
except ImportError:
    from ModelGateway import ModelGateway


DEFAULT_CONTEXT_RESULTS = 1
UNKNOWN_ANSWER = "I don't know based on the available documents."

DEFAULT_ANSWER_PROMPT = """
Question:
{query}

context:
{context}
"""
INSTRUCTIONS = """
# You are an helpfull assistance with the best knowledge of WebEngage product capabilities. Your task is to assist the customers and internal support teams with their prodcut queries.

# Treat the provided context as the primary knowledgebase. You may use general product or technical knowledge only to explain the retrieved information more clearly, but never to invent WebEngage product behavior, configuration steps, limitations, or availability.

Rules:
- Add a one liner headline at the top to best describe the objective of the query
- Flag limitations or assumptions as Notes at the end of the answer if needed
- Use examples to explain
- Use bullet points whenever needed to explain the steps
- Populate the sources field with the title and URL of every provided context source used in the answer
- Do not invent source titles or URLs
"""

# INSTRUCTIONS = """
# You are an helpfull assistance who has the best understanding of WebEngage product capabilities. Your task is to assist the customers and internal support teams with their prodcut queries.

# Treat the provided context as the primary knowledgebase. You may use general product or technical knowledge only to explain the retrieved information more clearly, but never to invent WebEngage product behavior, configuration steps, limitations, or availability.

# Answer Guidelines:
# - Add a one liner headline at the top to best describe the objective of the query
# - The answer should start with a one-to-two sentence summary of the key finding
# - Use tables for comparisons, bullet points for lists
# - Distinguish between facts, interpretations, and uncertainties
# - Flag data limitations or assumptions

# Sources citation rules:
# - Cite product-specific claims inline using the source page URL.
# - Use this citation style: WebEngage tracks cart and checkout events for Shopify. (https://docs.webengage.com/docs/shopify)
# - Do not cite chunk IDs in the final answer.
# - Add all the citation urls in the sources list of the GeneratedAnswer

# Answer Format:
# - Use Markdown with headers. Lead with the conclusion, then supporting evidence.

# Confidence rules:
# - high: the retrieved context directly answers the exact question.
# - medium: the retrieved context partially answers the question or supports a related workaround.
# - low: the retrieved context is weak, missing, or only generally related.
# """

class AnswerSource(BaseModel):
    title: str
    url: str


class GeneratedAnswer(BaseModel):
    objective: str
    answer: str
    sources: list[AnswerSource] = Field(default_factory=list)
    confidence: Literal["high", "medium", "low"]


class RetrievedContext(BaseModel):
    rank: int
    document_dir: str = ""
    source: str
    topic: str
    url: str
    chunk_id: str
    final_score: float = 0.0
    text: str


class TokenUsage(BaseModel):
    input_tokens: int = 0
    output_tokens: int = 0
    total_tokens: int = 0
    cache_read_tokens: int = 0
    cache_write_tokens: int = 0
    requests: int = 0


class RAGResult(BaseModel):
    answer: GeneratedAnswer
    retrieved_contexts: list[RetrievedContext] = Field(default_factory=list)
    usage: TokenUsage = Field(default_factory=TokenUsage)


class AnswerGenerator:
    def __init__(
        self,
        prompt_template: str = DEFAULT_ANSWER_PROMPT,
        model_name: str = "gemma3:12b",
        base_url: str = "http://localhost:11434/v1",
    ):
        self.prompt_template = prompt_template
        self.model_gateway = ModelGateway(
            output_type=GeneratedAnswer,
            instructions=INSTRUCTIONS,
            model_name=model_name,
            base_url=base_url,
            output_validator=validate_output,
        )

    def generate_rag_result(
        self,
        query: str,
        search_results: list[dict[str, Any]],
        max_context_results: int = DEFAULT_CONTEXT_RESULTS,
        retries: int = 1,
    ) -> RAGResult:
        context_results = search_results[:max_context_results]
        retrieved_contexts = build_retrieved_contexts(context_results)

        if not context_results:
            return RAGResult(
                answer=GeneratedAnswer(
                    objective="Unknown",
                    answer=UNKNOWN_ANSWER,
                    sources=[],
                    confidence="low",
                ),
                retrieved_contexts=retrieved_contexts,
                usage=build_token_usage(RunUsage()),
            )

        prompt = render_prompt(
            self.prompt_template,
            query=query,
            context=format_context(context_results)
        )

        print(f"Prompt : {prompt}")
        result = self.model_gateway.run_with_usage(prompt, retries=retries)
        return RAGResult(
            answer=result.output,
            retrieved_contexts=retrieved_contexts,
            usage=build_token_usage(result.usage),
        )

    def generate_with_usage(
        self,
        query: str,
        search_results: list[dict[str, Any]],
        max_context_results: int = DEFAULT_CONTEXT_RESULTS,
        retries: int = 1,
    ) -> RAGResult:
        return self.generate_rag_result(
            query=query,
            search_results=search_results,
            max_context_results=max_context_results,
            retries=retries,
        )

async def validate_output(
    ctx: RunContext,
    output: GeneratedAnswer,
) -> GeneratedAnswer:
    if ctx.partial_output:
        return output

    if not isinstance(output, GeneratedAnswer):
        raise ModelRetry("Output must be a GeneratedAnswer.")

    if not output.sources and not ctx.last_attempt:
        raise ModelRetry(
            "Missing sources in the output. Include at least one source from "
            "the provided context."
        )

    return output


def build_retrieved_contexts(
    search_results: list[dict[str, Any]],
) -> list[RetrievedContext]:
    return [
        RetrievedContext(
            rank=index,
            document_dir=result.get("document_dir") or "",
            source=result.get("source") or "",
            topic=result.get("topic") or "",
            url=result.get("url") or "",
            chunk_id=result.get("chunk_id") or "",
            final_score=float(result.get("final_score") or 0.0),
            text=result.get("text") or "",
        )
        for index, result in enumerate(search_results, start=1)
    ]


def build_token_usage(usage: RunUsage) -> TokenUsage:
    input_tokens = usage.input_tokens or 0
    output_tokens = usage.output_tokens or 0

    return TokenUsage(
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        total_tokens=input_tokens + output_tokens,
        cache_read_tokens=usage.cache_read_tokens or 0,
        cache_write_tokens=usage.cache_write_tokens or 0,
        requests=usage.requests or 0,
    )


def format_context(search_results: list[dict[str, Any]]) -> str:
    context_blocks = []

    for index, result in enumerate(search_results, start=1):
        context_blocks.append(
            "\n".join(
                [
                    f"Source {result.get('source', '')}",
                    f"Title: {result.get('topic', '')}",
                    f"URL: {result.get('url', '')}",
                    f"Chunk ID: {result.get('chunk_id', '')}",
                    f"Final Score: {result.get('final_score', '')}",
                    "Context:",
                    result.get("text", ""),
                    # "\nNeighboring Chunks:",
                    # format_neighboring_chunks(result),
                ]
            )
        )

    return "\n\n---\n\n".join(context_blocks)

def format_neighboring_chunks(result: dict[str, Any]) -> str:
    neighboring_chunks = result.get("neighboring_chunks", [])

    if not neighboring_chunks:
        return "No neighboring chunks available."

    formatted_chunks = []
    matched_chunk_id = result.get("chunk_id", "")

    for chunk in neighboring_chunks:
        label = "Matched"
        if chunk.get("chunk_id") != matched_chunk_id:
            label = "Neighbor"

        formatted_chunks.append(
            "\n".join(
                [
                    f"{label} Chunk ID: {chunk.get('chunk_id', '')}",
                    chunk.get("text", ""),
                ]
            )
        )

    return "\n\n".join(formatted_chunks)


def render_prompt(prompt_template: str, **values: str) -> str:
    placeholders = {
        field_name
        for _, field_name, _, _ in Formatter().parse(prompt_template)
        if field_name
    }

    if placeholders:
        return prompt_template.format_map(SafePromptValues(values))

    return "\n\n".join(
        [
            prompt_template.strip(),
            f"Question:\n{values['query']}",
            f"Retrieved Context:\n{values['context']}",
            values["output_contract"].strip(),
        ]
    )


class SafePromptValues(dict):
    def __missing__(self, key: str) -> str:
        return "{" + key + "}"
    

if __name__ == "__main__":
    import json
    import re
    json_string = r"""[
        {
            "source": "knowledgebase-webengage-com-docs-derived-attributes.md",
            "topic": "Derived Attributes",
            "url": "https://knowledgebase.webengage.com/docs/derived-attributes",
            "chunk_id": "knowledgebase-webengage-com-docs-derived-attributes.md::520",
            "final_score": "0.9794191702743773",
	            "text": "numeric attributes (e.g., total spending). Number of Event Occurrences. (e.g. Total number of orders placed) Affinity (Maximum number of times a category purchased by the user) (Available for not numeric and string variables) 📘 Note: Functions that return numeric values will return zero (0) if: No events are found, or The event exists but the attribute value is blank. Calculated Derived Attributes: Create attributes by combining existing sub-derived attributes using the Calculation Logic component. Here are the calculations that are supported. Arithmetic Operators Addition (+), Subtraction (-), Multiplication (*), Division (/) Scheduling Derived attributes can be refreshed automatically at daily, weekly, or monthly intervals. If needed, you can also trigger a manual refresh at any time, independent of the scheduled frequency. Editing Rules You can edit all parameters except : Attribute type Upload method Logic can be edited, but saved attributes cannot start returning a different data type to maintain logical consistency across usage areas like segmentation. Name changes are allowed, but if an attribute is used in segmentation or personalization, renaming may be restricted. All changes are recorded in an audit log. Stop Refreshing (Available only for attributes created using the internal Query Builder) Stops refreshing the attribute. Displays a list of impacted segments and personalizations to help users make informed decisions. Deletion Rules Deletion is blocked if the attribute is currently in use in segmentation, journeys, or campaigns. Duplicating (Available only for attributes created using the internal Query Builder) Creates a copy with \"_copy\" added to the name. View Logs View complete audit logs for each derived attribute, including modification history and user actions. Visibility in User Profiles Derived attributes appear on the user profile page. Attributes from the same group are displayed together. Naming format: [Group Name] . [Attribute Name] Uploading Custom Derived Attributes Upload the file",
            "neighboring_chunks": [
                {
                    "chunk_id":"knowledgebase-webengage-com-docs-derived-attributes.md::260",
                    "text" :"purchases. Step 3: Apply Arithmetic Operations Next, you can use the Formula Builder to create a new metric that shows what portion of total purchases is spent on fashion. Formula: (Total Fashion Spending ÷ Total Purchases) × 100 Derived Value: 20% Step 4: Store the Derived Attribute This derived value is stored as a user-level attribute, for example: fashion_spend_percentage = 20% The platform automatically updates this attribute whenever new events occur, ensuring that user data stays current. How to Create Derived Attributes? You can start creating your derived attributes by following the steps provided below. Navigate to the Data Management under Data Platform section from the left navigation panel. Once you're here proceed to the Derived Attributes tab. Here, you can start creating your derived attributes by clicking on the ➕ on the right. Once you're here you can proceed to creating your derived attributes based on attribute type i.e. with a Criteria Builder or an External . Criteria Builder The Criteria Builder allows you to create, manage, and schedule derived attributes through a simple and flexible interface. It supports creating both sub-derived attributes and calculated derived attributes using arithmetic operators and functions. How to create derived attributes using Criteria Builder? Building Sub-Derived Attributes You can create sub-derived attributes, assign unique names, and save them. Duplicate names are not allowed within the same attribute scope. Sub-derived attributes can be based on: User Attributes Below aggregates on Event Attributes Min & Max of a numeric attribute (e.g., minimum amount spent). Average of a numeric attribute. (e.g. Average order value). Sum of numeric attributes (e.g., total spending). Number of Event Occurrences. (e.g. Total number of orders placed) Affinity (Maximum number of times a category purchased by the user) (Available for not numeric and string variables) 📘 Note: Functions that return numeric values",
                },
                {
                    "chunk_id":"knowledgebase-webengage-com-docs-derived-attributes.md::520",
	                    "text" :"numeric attributes (e.g., total spending). Number of Event Occurrences. (e.g. Total number of orders placed) Affinity (Maximum number of times a category purchased by the user) (Available for not numeric and string variables) 📘 Note: Functions that return numeric values will return zero (0) if: No events are found, or The event exists but the attribute value is blank. Calculated Derived Attributes: Create attributes by combining existing sub-derived attributes using the Calculation Logic component. Here are the calculations that are supported. Arithmetic Operators Addition (+), Subtraction (-), Multiplication (*), Division (/) Scheduling Derived attributes can be refreshed automatically at daily, weekly, or monthly intervals. If needed, you can also trigger a manual refresh at any time, independent of the scheduled frequency. Editing Rules You can edit all parameters except : Attribute type Upload method Logic can be edited, but saved attributes cannot start returning a different data type to maintain logical consistency across usage areas like segmentation. Name changes are allowed, but if an attribute is used in segmentation or personalization, renaming may be restricted. All changes are recorded in an audit log. Stop Refreshing (Available only for attributes created using the internal Query Builder) Stops refreshing the attribute. Displays a list of impacted segments and personalizations to help users make informed decisions. Deletion Rules Deletion is blocked if the attribute is currently in use in segmentation, journeys, or campaigns. Duplicating (Available only for attributes created using the internal Query Builder) Creates a copy with \"_copy\" added to the name. View Logs View complete audit logs for each derived attribute, including modification history and user actions. Visibility in User Profiles Derived attributes appear on the user profile page. Attributes from the same group are displayed together. Naming format: [Group Name] . [Attribute Name] Uploading Custom Derived Attributes Upload the file",
                },
                {
                    "chunk_id":"knowledgebase-webengage-com-docs-derived-attributes.md::780",
                    "text" :"including modification history and user actions. Visibility in User Profiles Derived attributes appear on the user profile page. Attributes from the same group are displayed together. Naming format: [Group Name] . [Attribute Name] Uploading Custom Derived Attributes Upload the file from your device and create your derived attributes. You can upload your files in the following types: Full Upload - Replaces the entire dataset (once a month). Delta Upload - Updates changed records (1-4 times per day, with a minimum 6-hour gap). You can also set a schedule upload. This will automatically pick files from one of the sources mentioned below at the specific schedule. AWS SFTP / FTP HTTP / HTTPS Your file will get rejected if: the File-level violations (size, column, or record limits) then the entire file gets rejected. Record-level errors then only the faulty records are rejected. Affinity Function The Affinity() function identifies the value that appears most frequently within a selected attribute. This helps understand what your user prefers or interacts with most often. This function supports String and Numeric data types. 📘 Use Case: Personalized Recommendations Based on User Affinity Every user has unique tastes when it comes to products. By tracking what colors and categories each user interacts with, you can understand their preferences and use that data to deliver more relevant recommendations. This approach helps create a personalized shopping or browsing experience that feels tailored to each individual. How It Works? Create Affinity for Color and Category: Track what colors and product categories a user interacts with most. For example, if a user often views blue shirts or black shoes, the system builds an affinity (preference) for those colors and categories. Identify Products Using Collections: Use collections to group products based on these affinities. This helps the system easily find products that",
                }
            ]
        }
    ]"""

    valid_json_string = re.sub(r",(\s*[}\]])", r"\1", json_string)
    result_dict = json.loads(valid_json_string)
    answer = AnswerGenerator().generate_rag_result(
        "Does derived attribute only for numeric data type?",
        result_dict
    )
    print("Final Answer:\n")
    print(answer.model_dump_json(indent=2))
