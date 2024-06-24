from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain.tools.retriever import create_retriever_tool
from langchain_community.embeddings import OllamaEmbeddings


# this is just a basic RAG tool taken from the langchain homepage
# a web page is scraped, chunked in chunks and fed into the vector DB

# load a website
loader = WebBaseLoader("https://docs.smith.langchain.com/overview")
docs = loader.load()

# load into documents and split into chunks
documents = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
).split_documents(docs)

# set up the  vector database
vector = FAISS.from_documents(
    documents=documents,
    embedding=OllamaEmbeddings(model='nomic-embed-text:latest')
)

# create a retriever object
retriever = vector.as_retriever()

# create the tool for langchain
retriever_tool = create_retriever_tool(
    retriever=retriever,
    name="langsmith_search",
    description="Search for information about LangSmith. For any questions about LangSmith, you must use this tool!",
)
