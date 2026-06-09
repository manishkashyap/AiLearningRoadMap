const form = document.querySelector("#search-form");
const queryInput = document.querySelector("#query");
const searchButton = document.querySelector("#search-button");
const loadingPanel = document.querySelector("#loading-panel");
const errorPanel = document.querySelector("#error-panel");
const answerSection = document.querySelector("#answer-section");
const metricsSection = document.querySelector("#metrics-section");
const resultsSection = document.querySelector("#results-section");
const serviceStatus = document.querySelector("#service-status");

function setHidden(element, hidden) {
  element.classList.toggle("hidden", hidden);
}

function formatNumber(value, digits = 3) {
  return Number(value || 0).toFixed(digits);
}

function clearResults() {
  setHidden(errorPanel, true);
  setHidden(answerSection, true);
  setHidden(metricsSection, true);
  setHidden(resultsSection, true);
}

function showError(message) {
  errorPanel.textContent = message;
  setHidden(errorPanel, false);
}

function renderAnswer(answer) {
  if (!answer) {
    setHidden(answerSection, true);
    return;
  }

  document.querySelector("#answer-objective").textContent = answer.objective || "Answer";
  document.querySelector("#confidence").textContent = `${answer.confidence || "unknown"} confidence`;
  document.querySelector("#answer-content").textContent = answer.answer || "";

  const sources = document.querySelector("#answer-sources");
  sources.replaceChildren();
  for (const source of answer.sources || []) {
    const link = document.createElement("a");
    link.href = source.url;
    link.target = "_blank";
    link.rel = "noreferrer";
    link.textContent = source.title || source.url;
    sources.append(link);
  }

  setHidden(answerSection, false);
}

function renderMetrics(data) {
  document.querySelector("#retrieval-time").textContent = `${formatNumber(data.timings.retrieval_ms, 0)} ms`;
  document.querySelector("#generation-time").textContent = `${formatNumber(data.timings.answer_generation_ms, 0)} ms`;
  document.querySelector("#input-tokens").textContent = data.usage.input_tokens || 0;
  document.querySelector("#output-tokens").textContent = data.usage.output_tokens || 0;
  setHidden(metricsSection, false);
}

function createScore(label, value) {
  const span = document.createElement("span");
  const strong = document.createElement("strong");
  strong.textContent = formatNumber(value);
  span.append(`${label} `, strong);
  return span;
}

function renderSearchResults(results) {
  const resultsList = document.querySelector("#results-list");
  resultsList.replaceChildren();
  document.querySelector("#result-count").textContent = `${results.length} results`;

  for (const result of results) {
    const article = document.createElement("article");
    article.className = "result";

    const header = document.createElement("div");
    header.className = "result-header";

    const rank = document.createElement("span");
    rank.className = "rank";
    rank.textContent = String(result.rank).padStart(2, "0");

    const titleWrap = document.createElement("div");
    const title = document.createElement("a");
    title.className = "result-title";
    title.href = result.url;
    title.target = "_blank";
    title.rel = "noreferrer";
    title.textContent = result.topic || result.source;
    const url = document.createElement("span");
    url.className = "result-url";
    url.textContent = result.url;
    titleWrap.append(title, url);

    const category = document.createElement("span");
    category.className = "category";
    category.textContent = result.document_dir;

    header.append(rank, titleWrap, category);

    const scores = document.createElement("div");
    scores.className = "score-grid";
    scores.append(
      createScore("Final", result.final_score),
      createScore("FAISS", result.faiss_score),
      createScore("BM25", result.bm25_score),
      createScore("Rerank", result.rerank_score),
    );

    const text = document.createElement("p");
    text.className = "result-text";
    text.textContent = result.text;

    article.append(header, scores, text);
    resultsList.append(article);
  }

  setHidden(resultsSection, false);
}

async function checkHealth() {
  try {
    const response = await fetch("/api/health");
    if (!response.ok) throw new Error();
    serviceStatus.classList.add("online");
    serviceStatus.querySelector("span:last-child").textContent = "Service online";
  } catch {
    serviceStatus.classList.add("offline");
    serviceStatus.querySelector("span:last-child").textContent = "Service unavailable";
  }
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  clearResults();
  setHidden(loadingPanel, false);
  searchButton.disabled = true;
  searchButton.textContent = "Searching";

  const payload = {
    query: queryInput.value.trim(),
    top_k: Number(document.querySelector("#top-k").value),
    answer_top_k: Number(document.querySelector("#answer-top-k").value),
    candidate_count: Number(document.querySelector("#candidate-count").value),
    use_bm25: document.querySelector("#use-bm25").checked,
    use_reranker: document.querySelector("#use-reranker").checked,
    generate_answer: document.querySelector("#generate-answer").checked,
  };

  try {
    const response = await fetch("/api/search", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    const data = await response.json();
    if (!response.ok) {
      throw new Error(data.detail || "Search failed.");
    }

    renderAnswer(data.answer);
    renderMetrics(data);
    renderSearchResults(data.search_results || []);
  } catch (error) {
    showError(error.message || "Search failed.");
  } finally {
    setHidden(loadingPanel, true);
    searchButton.disabled = false;
    searchButton.textContent = "Search";
  }
});

checkHealth();
