from core.client_factory import get_groq, get_tavily

# Initialize tools
groq = get_groq()
tavily = get_tavily()

def run_news_search(topic):
    # 1. Use 'news' topic to filter for actual articles
    search = tavily.search(query=topic, search_depth="advanced", topic="news", max_results=5)
    
    # 2. Format context with URLs so the AI can cite them
    context = "\n".join([f"Source: {r['url']}\nContent: {r['content']}" for r in search['results']])
    
    # 3. Use a high-quality System Prompt
    system_message = (
        "You are a News Journalist. Your task is to summarize the LATEST news on a topic. "
        "Rules:\n"
        "1. Use ONLY the provided search results.\n"
        "2. Format as a bulleted list.\n"
        "3. Include the Source URL for every bullet.\n"
        "4. If no news is found, say 'No recent news found'—do not give a definition."
    )

    completion = groq.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": f"Topic: {topic}\n\nSearch Results:\n{context}"}
        ]
    )
    return completion.choices[0].message.content