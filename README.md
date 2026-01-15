# 🤖 Multi-Agent AI Research Lab

A modular, local AI agent system designed to perform deep research and critical analysis. This project uses a **Researcher Agent** to gather data and a **Critic Agent** to evaluate and refine the findings.

---

## Prerequisites

Before you begin, ensure you have the following API keys:
1. **Groq API Key**: [Get it here](https://console.groq.com/keys)
2. **Tavily API Key**: [Get it here](https://tavily.com/)

---

## 🚀 Local Setup

### 1. Clone & Environment
```zsh
# Create your virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Keys
Create a file named `.env` in the root directory:
```zsh
GROQ_API_KEY=your_groq_key_here
TAVILY_API_KEY=your_tavily_key_here
```

---

## 📂 Project Structure

```zsh
my-ai-agents/
├── core/                # API clients & shared logic
├── agents/              
│   ├── news_agent/      # Search & Summarization
│   └── new_summary_agent/    # Summarize the news
├── main.py              # Orchestrator (Entry Point)
└── requirements.txt     # Dependency list
```

---

## Usage

### Start the Full Pipeline
Run the orchestrator from the root folder:
```zsh
export PYTHONPATH=\$PYTHONPATH:.
python main.py
```

---

## Technical Stack
- **Language:** Python 3.9+
- **LLM:** Llama 3.3 70B (via Groq)
- **Search:** Tavily AI API