from langchain_core.chat_history import BaseChatMessageHistory
from chatbot.models import ChatLog
from langchain_core.messages import AIMessage, HumanMessage

class ChatLogHistory(BaseChatMessageHistory):
    def __init__(self, nickname):
        self.nickname = nickname

    def add_messages(self, messages):
        question, answer = None, None
        for msg in messages:
            if isinstance(msg, HumanMessage):
                question = msg.content
            elif isinstance(msg, AIMessage):
                answer = msg.content

        if question and answer:
            ChatLog.objects.create(
                nickname=self.nickname,
                question=question,
                answer=answer
            )

    @property
    def messages(self):
        logs = ChatLog.objects.filter(nickname=self.nickname).order_by("created_at")
        result = []
        for log in logs:
            result.append(HumanMessage(content=log.question))
            result.append(AIMessage(content=log.answer))
        return result

    def clear(self):
        ChatLog.objects.filter(nickname=self.nickname).delete()

def get_by_nickname(nickname):
    return ChatLogHistory(nickname)