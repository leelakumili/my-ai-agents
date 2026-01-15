from core.client_factory import get_groq

# Initialize the 'brain' for the Critic
groq = get_groq()

def run_news_summary(research_report):
    print("🧐 Critic Agent is analyzing the report for quality and gaps...")
    
    system_prompt = (
    "You are a News Editor. Your job is to review a brief news summary. "
    "Do not expect deep technical tutorials or primary research. "
    "Instead, check for: \n"
    "1. Are the sources credible?\n"
    "2. Is the summary clear and easy to read?\n"
    "3. Is the information actually 'News' or just a definition?\n"
    "\nIf the report says 'No news found', do not critique it. Just say: 'Waiting for valid data.'"
)

    response = groq.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Please review this report:\n\n{research_report}"}
        ]
    )
    
    return response.choices[0].message.content

# Allow running this agent solo for testing
if __name__ == "__main__":
    test_report = "Solid state batteries are good and will be out in 2026. They use solid electrolytes."
    print(run_news_summary(test_report))