from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    PromptTemplate,
    MessagesPlaceholder,
    HumanMessagePromptTemplate,
)


base_prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate(
            prompt=PromptTemplate(
                input_variables=[],
                template='You are a helpful assistant'
            )
        ),
        MessagesPlaceholder(
            variable_name='chat_history',
            optonal=True
        ),
        HumanMessagePromptTemplate(
            prompt=PromptTemplate(
                input_variables=['input'],
                template='{input}'
            )
        ),
        MessagesPlaceholder(variable_name='agent_scratchpad')
    ]
)
