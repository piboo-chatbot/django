from django.urls import path
from .views import AskView, chatbot_page, intro_view, mypage_view


urlpatterns = [
    path('ask/', AskView.as_view(), name='ask'),        # 질문 처리 API
    path('', chatbot_page, name='chatbot'),             # 챗봇 화면
    path('intro/', intro_view, name = 'intro'),
    path('mypage/', mypage_view, name='mypage'),
]
