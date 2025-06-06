from django.urls import path
from .views import AskView, chatbot_page, signup_view, login_view ,intro_view

urlpatterns = [
    path('ask/', AskView.as_view(), name='ask'),        # 질문 처리 API
    path('', chatbot_page, name='chatbot'),             # 챗봇 화면
    path('signup/', signup_view, name='signup'),        # 회원가입 화면
    path('login/', login_view, name='login'),           # 로그인 화면
    path('intro/', intro_view, name = 'intro'),
]
