from django.shortcuts import render,redirect
from .forms import UserForm
from django.http import JsonResponse
from .models import User
from django.contrib.auth import authenticate, login

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # 세션에 로그인 처리
            return redirect('chatbot')
        else:
            error = "아이디 또는 비밀번호가 일치하지 않습니다."
            return render(request, 'login.html', {'error': error})
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # 회원가입 성공 시 로그인 페이지로 이동
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})

def check_username(request):
    username = request.GET.get('username')
    exists = User.objects.filter(username=username).exists()
    return JsonResponse({'exists': exists})

def check_nickname(request):
    nickname = request.GET.get('nickname')
    exists = User.objects.filter(nickname=nickname).exists()
    return JsonResponse({'exists': exists})