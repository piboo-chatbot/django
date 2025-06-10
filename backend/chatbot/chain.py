from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory

# from history.utils import get_by_session_id
from history.utils import get_by_nickname
from .prompt.gpt_templates import chat_prompts

def get_chain(model, nickname):
    prompt = ChatPromptTemplate.from_messages([
        ("system", chat_prompts + '''
---
[검색된 문서]
{search_results}

[실제 질문]
{query}
'''),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{query}")
    ])
    chain = prompt | model
    print("===================")
    print(get_by_nickname(nickname))
    print("=================")
    return RunnableWithMessageHistory(
        chain,
        get_session_history=lambda session_id: get_by_nickname(nickname),
        input_messages_key="query",
        history_messages_key="history"
    )