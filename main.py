from agents.news_agent.agent import run_news_search
from agents.new_summary_agent.agent import run_news_summary

def main():
    print("🚀 --- Starting Multi-Agent Research Pipeline ---")
    
    # Now it will wait for YOU to type something
    user_topic = input("📝 Enter your research topic: ")
    
    if not user_topic.strip():
        print("❌ No topic entered. Exiting...")
        return

    # Step 1: Researcher Agent
    raw_report = run_news_search(user_topic)
    
    print("\n--- RESEARCHER OUTPUT ---")
    print(raw_report)
    
    # Step 2: Critic Agent
    critique = run_news_summary(raw_report)
    
    print("\n--- CRITIC'S REVIEW ---")
    print(critique)
    
    print("\n✅ Pipeline Complete.")

if __name__ == "__main__":
    main()