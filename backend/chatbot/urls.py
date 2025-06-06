from django.urls import path
from .views import AskView
from .views import AskView, chatbot_page 

urlpatterns = [
    path('ask/', AskView.as_view(), name='ask'),
    path('', chatbot_page, name='chatbot'),
]