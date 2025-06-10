from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# askview 모델
from .models import ChatLog
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from langchain_openai import ChatOpenAI
from chatbot.chain import get_chain
from retriever.utils import (
    set_embedding_model, load_chromadbs, create_ensemble_retriever, search_documents
)

# from chatbot.qlora import load_qlora_llm

# (초기화 작업: 임베딩/리트리버/체인 등)
embedding_model = set_embedding_model()
chroma1, chroma2 = load_chromadbs(embedding_model)
ensemble_retriever = create_ensemble_retriever(chroma1, chroma2)
llm_model = ChatOpenAI(model_name='gpt-4o-mini', temperature=0.4)
# qlora_model= load_qlora_llm(
#         base_model_path="beomi/KoAlpaca-Polyglot-5.8B",
#         adapter_path="./qlora_model_koalpaca"
#     )
# chat_memory = get_chain(qlora_model)#llm_model
chat_memory = get_chain(llm_model)

@login_required
def mypage_view(request):
    nickname = request.user.nickname
    chat_logs = ChatLog.objects.filter(nickname=nickname).order_by('-created_at')[:5]

    context = {
        'user': request.user,
        'chat_logs': chat_logs,
    }

    return render(request, 'mypage.html',  context)

def chatbot_page(request):
    return render(request, 'chatbot.html')

def intro_view(request):
    return render(request, 'index.html')

class AskView(APIView):
    @method_decorator(login_required)
    def post(self, request):
        query = request.data.get('query')
        session_id = request.data.get('session_id')
        user = request.user


        search_results = search_documents(ensemble_retriever, query)
        response = chat_memory.invoke(
            {"query": query, "search_results": search_results},
            config={"configurable": {"session_id": session_id}}
        )

        # DB에 저장
        ChatLog.objects.create(
            nickname=user.nickname,  # user.nickname으로 사용자 닉네임 가져오기
            question=query,
            answer=response.content
        )

        return Response({"answer": response.content}, status=status.HTTP_200_OK)    
