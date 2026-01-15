# News Agent

The **News Agent** is the specialized researcher. Its primary responsibility is to fetch live, real-time news from the web and synthesize it into a clean, structured report.


## Responsibility
- **Query Optimization:** Translates topic given into effective search queries.
- **Data Retrieval:** Interface with the **Tavily Search API**.
- **Synthesis:** Filters noise and summarizes search results into a concise Markdown report.
- **Citation:** Ensures every claim is backed by a source URL.



## 🏎️ The F1 Technical Analogy

We treat our AI new agent like a professional racing team:
- **The Engine (Llama 3.3):** Our reasoning core.
- **The Driver (Groq):** Providing the high-speed inference to move the engine.
- **The Pit Crew (Tavily):** Delivering the real-time search data (fuel) we need to stay current.

This separation of **Model**, **Inference**, and **Tools** allows for maximum performance and modularity.



## File Layout
- `agent.py`: The main logic for query execution and LLM summarization.
- `__init__.py`: Marks this folder as a Python package.



## Configuration

This agent relies on the following logic defined in `agent.py`:

| Parameter | Value | Description |
| :--- | :--- | :--- |
| **Model** | `llama-3.3-70b-versatile` | High-reasoning model for summarizing facts. |
| **Search Depth** | `advanced` | Pulls in-depth content snippets for higher accuracy. |
| **Max Results** | `5` | Keeps the context window clean and focused. |

---

## Independent Testing

You can test this agent individually without running the whole pipeline:

```zsh
# Run from the project root
export PYTHONPATH=$PYTHONPATH:.
python -m agents.news_agent.agent