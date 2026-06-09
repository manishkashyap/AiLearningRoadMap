import time
from functools import lru_cache
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException
from fastapi.concurrency import run_in_threadpool
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from AnswerGenerator import AnswerGenerator, GeneratedAnswer, RetrievedContext, TokenUsage
from search import search


APP_DIR = Path(__file__).resolve().parent
STATIC_DIR = APP_DIR / "static"


class SearchRequest(BaseModel):
    query: str = Field(min_length=2, max_length=2000)
    top_k: int = Field(default=5, ge=1, le=20)
    answer_top_k: int = Field(default=3, ge=1, le=10)
    candidate_count: int = Field(default=15, ge=1, le=100)
    min_score: float | None = Field(default=None, ge=0.0, le=1.0)
    use_bm25: bool = True
    use_reranker: bool = False
    generate_answer: bool = True
    answer_retries: int = Field(default=2, ge=0, le=5)
    answer_model: str = "gemma3:12b"
    answer_base_url: str = "http://localhost:11434/v1"


class SearchResult(BaseModel):
    rank: int
    document_dir: str
    source: str
    topic: str
    url: str
    chunk_id: str
    text: str
    final_score: float
    faiss_score: float
    bm25_score: float
    rerank_score: float


class SearchTimings(BaseModel):
    retrieval_ms: float
    answer_generation_ms: float
    total_ms: float


class SearchResponse(BaseModel):
    query: str
    answer: GeneratedAnswer | None = None
    answer_contexts: list[RetrievedContext] = Field(default_factory=list)
    search_results: list[SearchResult] = Field(default_factory=list)
    usage: TokenUsage = Field(default_factory=TokenUsage)
    timings: SearchTimings


app = FastAPI(
    title="WebEngage Knowledge Search",
    version="1.0.0",
    description="Search and answer generation over the local WebEngage document index.",
)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@lru_cache(maxsize=4)
def get_answer_generator(model_name: str, base_url: str) -> AnswerGenerator:
    return AnswerGenerator(model_name=model_name, base_url=base_url)


def serialize_search_results(results: list[dict[str, Any]]) -> list[SearchResult]:
    return [
        SearchResult(
            rank=index,
            document_dir=result.get("document_dir", ""),
            source=result.get("source", ""),
            topic=result.get("topic", ""),
            url=result.get("url", ""),
            chunk_id=result.get("chunk_id", ""),
            text=result.get("text", ""),
            final_score=float(result.get("final_score", 0.0)),
            faiss_score=float(result.get("score", 0.0)),
            bm25_score=float(result.get("bm25_score", 0.0)),
            rerank_score=float(result.get("rerank_score", 0.0)),
        )
        for index, result in enumerate(results, start=1)
    ]


def execute_search(request: SearchRequest) -> SearchResponse:
    started_at = time.perf_counter()
    retrieval_started_at = time.perf_counter()
    results = search(
        query=request.query,
        top_k=request.top_k,
        min_score=request.min_score,
        use_bm25=request.use_bm25,
        use_reranker=request.use_reranker,
        candidate_count=request.candidate_count,
    )
    retrieval_ms = (time.perf_counter() - retrieval_started_at) * 1000

    answer = None
    answer_contexts = []
    usage = TokenUsage()
    answer_generation_ms = 0.0

    if request.generate_answer:
        answer_started_at = time.perf_counter()
        generator = get_answer_generator(request.answer_model, request.answer_base_url)
        rag_result = generator.generate_rag_result(
            query=request.query,
            search_results=results,
            max_context_results=request.answer_top_k,
            retries=request.answer_retries,
        )
        answer_generation_ms = (time.perf_counter() - answer_started_at) * 1000
        answer = rag_result.answer
        answer_contexts = rag_result.retrieved_contexts
        usage = rag_result.usage

    return SearchResponse(
        query=request.query,
        answer=answer,
        answer_contexts=answer_contexts,
        search_results=serialize_search_results(results),
        usage=usage,
        timings=SearchTimings(
            retrieval_ms=round(retrieval_ms, 2),
            answer_generation_ms=round(answer_generation_ms, 2),
            total_ms=round((time.perf_counter() - started_at) * 1000, 2),
        ),
    )


@app.get("/", include_in_schema=False)
def index() -> FileResponse:
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/api/search", response_model=SearchResponse)
async def search_api(request: SearchRequest) -> SearchResponse:
    try:
        return await run_in_threadpool(execute_search, request)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error)) from error
