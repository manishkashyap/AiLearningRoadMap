import argparse
import json
import os
from dataclasses import dataclass
from functools import lru_cache
from typing import Any, Literal

from pydantic import BaseModel, Field
from pydantic_ai import Agent, ModelSettings, NativeOutput
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.ollama import OllamaProvider
from pydantic_evals import Case, Dataset
from pydantic_evals.evaluators import EvaluationReason, Evaluator, EvaluatorContext

try:
    from .AnswerGenerator import AnswerGenerator, RAGResult
    from .search import search
except ImportError:
    from AnswerGenerator import AnswerGenerator, RAGResult
    from search import search


DEFAULT_MODEL = "gemma3:12b"
DEFAULT_BASE_URL = "http://localhost:11434/v1"

JUDGE_INSTRUCTIONS = """
You are evaluating a retrieval-augmented generation system.

Evaluate only the requested metric. Be strict, evidence-based, and consistent.
Return a score from 0.0 to 1.0, where 1.0 fully satisfies the rubric.
Set passed to true only when the score is at least 0.7.
Explain the most important reason for the score concisely.
"""

CORRECTNESS_RUBRIC = """
Evaluate answer correctness against the expected behavior and facts.

Scoring:
- 1.0: all required facts are correctly communicated and no forbidden claims appear.
- 0.7: mostly correct, with only minor omissions that do not change the conclusion.
- 0.4: partially correct but misses or contradicts important facts.
- 0.0: incorrect, misleading, or violates the expected behavior.

Judge semantic meaning, not exact wording. Do not require every optional detail.
"""

ANSWER_RELEVANCE_RUBRIC = """
Evaluate how directly the generated answer addresses the user's query.

Scoring:
- 1.0: directly answers the intended question with useful, focused information.
- 0.7: answers the question but includes minor tangents or misses a small part.
- 0.4: only partially addresses the question or answers a nearby question.
- 0.0: irrelevant or fails to answer the question.

Do not reward an answer merely because it discusses the same broad product area.
"""

GROUNDEDNESS_RUBRIC = """
Evaluate whether product-specific claims in the generated answer are supported by
the retrieved contexts.

Scoring:
- 1.0: every product-specific claim is supported and citations refer to retrieved sources.
- 0.7: mostly supported, with only minor clearly-labeled general guidance.
- 0.4: contains important unsupported extrapolations or weakly supported claims.
- 0.0: substantially contradicts or invents information beyond the contexts.

General technical advice is acceptable only when clearly distinguished from
documented WebEngage behavior.
"""

RETRIEVAL_RELEVANCE_RUBRIC = """
Evaluate how useful the retrieved contexts are for answering the user's query.

Scoring:
- 1.0: the top contexts directly answer the query and contain the necessary evidence.
- 0.7: the contexts are relevant and useful but incomplete.
- 0.4: the contexts are only broadly or indirectly related.
- 0.0: the contexts are irrelevant.

Consider ranking: highly relevant evidence near rank 1 is better than relevant
evidence appearing only near the bottom.
"""


class RAGTaskInput(BaseModel):
    query: str
    top_k: int = 3
    answer_top_k: int = 3
    candidate_count: int = 20
    min_score: float | None = None
    use_bm25: bool = True
    use_reranker: bool = True
    answer_retries: int = 2


class ExpectedRAGResult(BaseModel):
    required_facts: list[str] = Field(default_factory=list)
    forbidden_claims: list[str] = Field(default_factory=list)
    relevant_urls: list[str] = Field(default_factory=list)
    expected_behavior: Literal["answer", "acknowledge_insufficient_information"] = "answer"


class JudgeDecision(BaseModel):
    score: float = Field(ge=0.0, le=1.0)
    passed: bool
    reason: str


@dataclass
class EvaluationConfig:
    answer_model: str = DEFAULT_MODEL
    judge_model: str = DEFAULT_MODEL
    base_url: str = DEFAULT_BASE_URL


@lru_cache(maxsize=None)
def get_judge_agent(model_name: str, base_url: str) -> Agent:
    model = OpenAIChatModel(
        model_name=model_name,
        provider=OllamaProvider(base_url=base_url),
    )
    return Agent(
        model=model,
        output_type=NativeOutput(JudgeDecision),
        instructions=JUDGE_INSTRUCTIONS,
        model_settings=ModelSettings(temperature=0),
    )


def serialize(value: Any) -> str:
    return json.dumps(
        to_serializable(value),
        indent=2,
        ensure_ascii=False,
        default=str,
    )


def to_serializable(value: Any) -> Any:
    if isinstance(value, BaseModel):
        return value.model_dump()
    if isinstance(value, list):
        return [to_serializable(item) for item in value]
    if isinstance(value, tuple):
        return [to_serializable(item) for item in value]
    if isinstance(value, dict):
        return {key: to_serializable(item) for key, item in value.items()}
    return value


def format_judge_prompt(
    rubric: str,
    inputs: RAGTaskInput,
    output: RAGResult,
    expected_output: ExpectedRAGResult | None = None,
) -> str:
    sections = [
        f"Rubric:\n{rubric.strip()}",
        f"User Query:\n{inputs.query}",
        f"Generated Answer:\n{output.answer.model_dump_json(indent=2)}",
        f"Retrieved Contexts:\n{serialize(output.retrieved_contexts)}",
    ]
    if expected_output is not None:
        sections.append(f"Expected Result:\n{expected_output.model_dump_json(indent=2)}")
    return "\n\n".join(sections)


@dataclass
class SemanticRAGEvaluator(Evaluator[RAGTaskInput, RAGResult, dict[str, Any]]):
    metric_name: str
    rubric: str
    judge_model: str
    base_url: str
    include_expected_output: bool = False

    async def evaluate(
        self,
        ctx: EvaluatorContext[RAGTaskInput, RAGResult, dict[str, Any]],
    ) -> dict[str, EvaluationReason]:
        expected_output = None
        if self.include_expected_output and isinstance(ctx.expected_output, ExpectedRAGResult):
            expected_output = ctx.expected_output

        prompt = format_judge_prompt(
            rubric=self.rubric,
            inputs=ctx.inputs,
            output=ctx.output,
            expected_output=expected_output,
        )
        decision = (
            await get_judge_agent(self.judge_model, self.base_url).run(
                prompt,
                retries=2,
            )
        ).output
        passed = decision.score >= 0.7

        return {
            f"{self.metric_name}_score": EvaluationReason(
                value=decision.score,
                reason=decision.reason,
            ),
            f"{self.metric_name}_pass": EvaluationReason(
                value=passed,
                reason=decision.reason,
            ),
        }


@dataclass
class RetrievalRecallEvaluator(Evaluator[RAGTaskInput, RAGResult, dict[str, Any]]):
    def evaluate(
        self,
        ctx: EvaluatorContext[RAGTaskInput, RAGResult, dict[str, Any]],
    ) -> dict[str, EvaluationReason]:
        if not isinstance(ctx.expected_output, ExpectedRAGResult):
            return {
                "retrieval_recall_at_k": EvaluationReason(
                    value=0.0,
                    reason="No expected relevant URLs were configured.",
                )
            }

        expected_urls = set(ctx.expected_output.relevant_urls)
        retrieved_urls = {context.url for context in ctx.output.retrieved_contexts}

        if not expected_urls:
            return {
                "retrieval_recall_at_k": EvaluationReason(
                    value=1.0,
                    reason="The case does not require a specific source URL.",
                )
            }

        matched_urls = expected_urls & retrieved_urls
        recall = len(matched_urls) / len(expected_urls)
        return {
            "retrieval_recall_at_k": EvaluationReason(
                value=recall,
                reason=(
                    f"Retrieved {len(matched_urls)} of {len(expected_urls)} expected URLs: "
                    f"{sorted(matched_urls)}"
                ),
            )
        }


@dataclass
class CitationValidityEvaluator(Evaluator[RAGTaskInput, RAGResult, dict[str, Any]]):
    def evaluate(
        self,
        ctx: EvaluatorContext[RAGTaskInput, RAGResult, dict[str, Any]],
    ) -> dict[str, EvaluationReason]:
        cited_urls = {source.url for source in ctx.output.answer.sources}
        retrieved_urls = {context.url for context in ctx.output.retrieved_contexts}

        if not cited_urls:
            return {
                "citation_validity": EvaluationReason(
                    value=False,
                    reason="The generated answer contains no sources.",
                )
            }

        unsupported_urls = cited_urls - retrieved_urls
        return {
            "citation_validity": EvaluationReason(
                value=not unsupported_urls,
                reason=(
                    "All cited URLs were present in retrieved contexts."
                    if not unsupported_urls
                    else f"Cited URLs not present in retrieved contexts: {sorted(unsupported_urls)}"
                ),
            )
        }


def build_evaluators(config: EvaluationConfig) -> tuple[Evaluator, ...]:
    return (
        SemanticRAGEvaluator(
            metric_name="answer_correctness",
            rubric=CORRECTNESS_RUBRIC,
            judge_model=config.judge_model,
            base_url=config.base_url,
            include_expected_output=True,
        ),
        SemanticRAGEvaluator(
            metric_name="answer_relevance",
            rubric=ANSWER_RELEVANCE_RUBRIC,
            judge_model=config.judge_model,
            base_url=config.base_url,
        ),
        SemanticRAGEvaluator(
            metric_name="groundedness",
            rubric=GROUNDEDNESS_RUBRIC,
            judge_model=config.judge_model,
            base_url=config.base_url,
        ),
        SemanticRAGEvaluator(
            metric_name="retrieval_relevance",
            rubric=RETRIEVAL_RELEVANCE_RUBRIC,
            judge_model=config.judge_model,
            base_url=config.base_url,
        ),
        RetrievalRecallEvaluator(),
        CitationValidityEvaluator(),
    )


def build_cases(evaluators: tuple[Evaluator, ...]) -> list[Case]:
    return [
        Case(
            name="change-push-brand-name",
            inputs=RAGTaskInput(
                query="How can we change the brand name in push?",
            ),
            expected_output=ExpectedRAGResult(
                required_facts=[
                    "The answer must directly address whether and how the brand name can be changed.",
                    "If the retrieved documentation does not establish that capability, the answer must say so.",
                ],
                forbidden_claims=[
                    "Do not replace the brand-name question with unrelated visual styling instructions.",
                    "Do not invent unsupported WebEngage configuration steps.",
                ],
                relevant_urls=[
                    "https://knowledgebase.webengage.com/docs/push-notification-faq",
                    "https://docs.webengage.com/docs/web-push-enabling-2-step-opt-in",
                ],
            ),
            evaluators=evaluators,
        ),
        Case(
            name="update-existing-catalog-column",
            inputs=RAGTaskInput(
                query="Can I update an existing catalog with a new column?",
            ),
            expected_output=ExpectedRAGResult(
                required_facts=[
                    "A new version of a catalog file can be re-uploaded.",
                    "The latest uploaded file replaces the entire catalog.",
                    "The new column must follow the documented field-name rules and be mapped appropriately.",
                ],
                forbidden_claims=[
                    "Do not answer with catalog deletion instructions.",
                    "Do not claim that only one individual catalog row is patched unless supported.",
                ],
                relevant_urls=[
                    "https://knowledgebase.webengage.com/docs/catalogs-and-recommendations",
                ],
            ),
            evaluators=evaluators,
        ),
        Case(
            name="derived-attribute-data-types",
            inputs=RAGTaskInput(
                query="Do derived attributes support only numeric data types?",
            ),
            expected_output=ExpectedRAGResult(
                required_facts=[
                    "Derived attributes are not limited to numeric data.",
                    "Affinity supports string and numeric data types.",
                    "Arithmetic calculations operate on numeric derived values.",
                ],
                forbidden_claims=[
                    "Do not claim every derived-attribute function supports every data type.",
                ],
                relevant_urls=[
                    "https://knowledgebase.webengage.com/docs/derived-attributes",
                ],
            ),
            evaluators=evaluators,
        ),
        Case(
            name="salla-segment-export-unsupported",
            inputs=RAGTaskInput(
                query="How to best export segments from Salla to WebEngage?",
            ),
            expected_output=ExpectedRAGResult(
                required_facts=[
                    "The available Salla integration documentation does not describe exporting segments from Salla.",
                    "Any workaround must be clearly labeled as general guidance rather than documented Salla behavior.",
                ],
                forbidden_claims=[
                    "Do not claim that the documented Salla integration directly exports segments.",
                ],
                relevant_urls=[
                    "https://docs.webengage.com/docs/salla",
                ],
                expected_behavior="acknowledge_insufficient_information",
            ),
            evaluators=evaluators,
        ),
    ]


def build_rag_task(config: EvaluationConfig):
    generator = AnswerGenerator(
        model_name=config.answer_model,
        base_url=config.base_url,
    )

    def run_rag(inputs: RAGTaskInput) -> RAGResult:
        search_results = search(
            query=inputs.query,
            top_k=inputs.top_k,
            min_score=inputs.min_score,
            use_bm25=inputs.use_bm25,
            use_reranker=inputs.use_reranker,
            candidate_count=inputs.candidate_count,
        )
        return generator.generate_rag_result(
            query=inputs.query,
            search_results=search_results,
            max_context_results=inputs.answer_top_k,
            retries=inputs.answer_retries,
        )

    return run_rag


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run end-to-end RAG evaluations.")
    parser.add_argument(
        "--answer-model",
        default=os.getenv("EVAL_ANSWER_MODEL", DEFAULT_MODEL),
    )
    parser.add_argument(
        "--judge-model",
        default=os.getenv("EVAL_JUDGE_MODEL", DEFAULT_MODEL),
    )
    parser.add_argument(
        "--base-url",
        default=os.getenv("OLLAMA_BASE_URL", DEFAULT_BASE_URL),
    )
    parser.add_argument("--repeat", type=int, default=1)
    parser.add_argument("--max-concurrency", type=int, default=1)
    parser.add_argument(
        "--case",
        action="append",
        dest="case_names",
        help="Run only the named case. Repeat this option to select multiple cases.",
    )
    parser.add_argument(
        "--disable-reranker",
        action="store_true",
        help="Disable Cohere reranking for every evaluation case.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = EvaluationConfig(
        answer_model=args.answer_model,
        judge_model=args.judge_model,
        base_url=args.base_url,
    )
    evaluators = build_evaluators(config)
    cases = build_cases(evaluators)

    if args.case_names:
        selected_names = set(args.case_names)
        cases = [case for case in cases if case.name in selected_names]
        missing_names = selected_names - {case.name for case in cases}
        if missing_names:
            raise ValueError(f"Unknown evaluation cases: {sorted(missing_names)}")

    if args.disable_reranker:
        for case in cases:
            case.inputs.use_reranker = False

    dataset = Dataset(
        name="webengage-rag-evaluations",
        cases=cases,
    )
    report = dataset.evaluate_sync(
        build_rag_task(config),
        name="webengage-rag-evaluation-run",
        max_concurrency=args.max_concurrency,
        repeat=args.repeat,
    )
    report.print(include_input=True, include_output=True, include_reasons=True)


if __name__ == "__main__":
    main()
