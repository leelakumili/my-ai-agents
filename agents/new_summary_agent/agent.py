import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class NewsSummaryAgent:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.model = "llama-3.3-70b-versatile"

    def summarize(self, topic, raw_data):
        system_prompt = (
            "You are an Executive News Summarizer (The Communications Officer). "
            "Your job is to take raw search results and create a polished briefing.\n\n"
            "Rules:\n"
            "1. Focus on high-level trends.\n"
            "2. Ensure every claim includes the source URL.\n"
            "3. Organize logically (Market Trends, Tech, Challenges).\n"
        )
        user_prompt = f"Topic: {topic}\n\nRaw Search Data:\n{raw_data}"

        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.5,
        )
        return completion.choices[0].message.content

# --- ADD THIS WRAPPER FUNCTION TO FIX THE IMPORT ERROR ---
def run_news_summary(topic, raw_data):
    """
    Wrapper function so main.py can still call 'run_news_summary'
    """
    agent = NewsSummaryAgent()
    return agent.summarize(topic, raw_data)

if __name__ == "__main__":
    # Test locally
    print(run_news_summary("Test Topic", "Sample search data from the web."))