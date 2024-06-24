from langchain_community.tools.tavily_search import TavilySearchResults
import dotenv
import os


dotenv.load_dotenv()

# this is just a basic web search tool. In this case I use tavily.
# I might do a custom google search too.
tavily = TavilySearchResults(
    tavily_api_key=os.getenv("TAVILY_API_KEY")
)
