from agents.news_agent.agent import run_news_search
from agents.new_summary_agent.agent import run_news_summary

def main():
    print("🚀 --- Starting Multi-Agent Research Pipeline ---")
    topic = input("📝 Enter your research topic: ")

    # 1. Researcher (The Driver) gets the raw data
    raw_report = run_news_search(topic)
    print("\n--- RESEARCHER OUTPUT ---")
    print(raw_report)

    # 2. Summarizer (The Communications Officer) refines it
    # We pass both the TOPIC and the RAW_REPORT here
    summary_report = run_news_summary(topic, raw_report)
    
    print("\n--- EXECUTIVE SUMMARY ---")
    print(summary_report)

if __name__ == "__main__":
    main()