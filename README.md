# Basic agent using langchain

This repo contains boilerplate code for a basic langchain agent with tool usage. 

Tools are
- RAG
- websearch
- email notification using GMAIL [I just noticed, that langchain has this buit in...](https://python.langchain.com/v0.2/docs/integrations/toolkits/gmail/)

I use www.groq.com as LLM privider, but you could easily change that to any other provider or even locally deployed LLM. The RAG tool uses Ollama embeddings. https://ollama.com/
