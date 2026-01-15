# 📝 News Summary Agent

The **News Summary Agent** is the refiner of the pipeline. Its primary responsibility is to take the raw search data gathered by the News Agent and transform it into a high-level, executive summary that is easy to digest.

## Responsibility
- **Narrative Synthesis:** Connects the dots between different news articles to find a cohesive story.
- **Formatting:** Converts raw snippets into clean, structured Markdown.
- **Prioritization:** Highlights the most impactful news while moving minor details to the background.
- **Tone Management:** Ensures the final report sounds professional, objective, and authoritative.

## The F1 Technical Analogy
In our racing team, the News Summary Agent is the **Communications & Strategy Officer**:
- **The Engine (Llama 3.3):** The linguistic power used to rewrite and organize information.
- **The Driver (Groq):** The high-speed inference that allows for near-instant summary generation.
- **The Press Release (Output):** While the News Agent is "driving" to find the data, this agent is in the back office turning those "lap times" into a winning story for the media.

## File Layout
- `agent.py`: The logic for processing raw search context into a final executive summary.
- `__init__.py`: Marks this folder as a Python package.

## Configuration
This agent relies on the following logic defined in `agent.py`:

| Parameter | Value | Description |
| :--- | :--- | :--- |
| **Model** | `llama-3.3-70b-versatile` | Optimized for summarizing large blocks of text without losing nuance. |
| **System Role** | `Executive Summary Specialist` | The persona used to ensure the output is concise and "C-suite" ready. |
| **Constraint** | `No Hallucinations` | Strict instruction to only summarize provided news, not add outside info. |

---

## Independent Testing
You can test the summarization logic individually from the project root:

```zsh
export PYTHONPATH=$PYTHONPATH:.
python -m agents.news_summary_agent.agent