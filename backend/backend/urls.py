from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'), 
    path('chatbot/', include('chatbot.urls')),
    path('users/', include('users.urls')), 
]
