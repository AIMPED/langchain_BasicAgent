from langchain.agents import create_tool_calling_agent, AgentExecutor

from prompting import base_prompt
from tools import mail, rag, websearch
import model


# tools which can be used by the agent
tools = [websearch.tavily, mail.send_gmail, rag.retriever_tool]

# agent definition
agent = create_tool_calling_agent(
    llm=model.llm,
    tools=tools,
    prompt=base_prompt
)

# AgentExecutor object
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)


if __name__ == "__main__":
    results = agent_executor.invoke(
        {
            "input": "What is the current temperature in New York?" +
                     "Send all information to name@email.com",
            "chat_history": []
        }
    )

    # results = agent_executor.invoke(
    #     {
    #         "input": "Give me a brief introduction to LangSmith!" +
    #                  "Send all information to name@email.com",
    #         "chat_history": []
    #     }
    # )

    print(results)

