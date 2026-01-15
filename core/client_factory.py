import os
from dotenv import load_dotenv
from groq import Groq
from tavily import TavilyClient

# Load the .env file once for the entire project
load_dotenv()

def get_groq():
    """Returns an initialized Groq client."""
    key = os.getenv("GROQ_API_KEY")
    if not key:
        raise ValueError("GROQ_API_KEY not found in .env file")
    return Groq(api_key=key)

def get_tavily():
    """Returns an initialized Tavily client."""
    key = os.getenv("TAVILY_API_KEY")
    if not key:
        raise ValueError("TAVILY_API_KEY not found in .env file")
    return TavilyClient(api_key=key)