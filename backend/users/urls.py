from django.urls import path
from . import views  # users 앱의 views.py만 import

urlpatterns = [
    path('login/', views.signin, name='login'),
    path('signup/', views.signup, name='signup'),
    path('check_username/', views.check_username, name='check_username'),
    path('check_nickname/', views.check_nickname, name='check_nickname'),
    path('mypage/', views.mypage_view, name='mypage'),
    path('logout/', views.logout_view, name='logout'),
]
