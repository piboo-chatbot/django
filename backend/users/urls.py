from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.signin, name='login'),
    path('signup/', views.signup, name='signup'),
    path('check_username/', views.check_username, name='check_username'),
    path('check_nickname/', views.check_nickname, name='check_nickname'),
]