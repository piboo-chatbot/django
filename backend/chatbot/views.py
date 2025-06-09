from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

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

from chatbot.qlora import load_qlora_llm

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
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('chatbot')  # 로그인 성공 시 chatbot 화면으로
        else:
            return render(request, 'login.html', {'error': '아이디 또는 비밀번호가 틀렸습니다.'})
    return render(request, 'login.html')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')

        # 아이디 중복 여부 확인
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': '이미 존재하는 아이디입니다.'})

        # 사용자 생성
        user = User.objects.create_user(username=username, password=password)
        # 이름, 나이, 성별, 전화번호 등은 커스텀 UserProfile 모델을 만든 후 연결하거나, 추가 필드를 위한 모델을 따로 만들어 관리하는 것을 권장해!
        # 지금은 단순 예시로 User 객체 생성만 해줄게.
        user.save()

        return redirect('login')  # 회원가입 후 로그인 화면으로

    return render(request, 'signup.html')
