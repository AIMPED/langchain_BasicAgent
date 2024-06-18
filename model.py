from langchain_groq import ChatGroq
import dotenv
import os


_ = dotenv.load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama3-70b-8192",
    # model="llama3-8b-8192",
    # model="Mixtral-8x7b-32768",
    # model="gemma-7b-it",
    # model="whisper-large-v3",
    temperature=0.1
)
