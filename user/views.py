
from django.shortcuts import render, redirect
from .models import UserModel
from django.contrib.auth import get_user_model  # 사용자가 데이터베이스 안에 있는지 검사하는 함수
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect, render




def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:  # 로그인 되어있다면
            return redirect('/') 
        else:
            return render(request, 'user/signup.html')
    elif request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        username = request.POST.get('username', None)

        if email == '' or password == '' or username == '':
            return render(request, 'user/signup.html', {'error': '빈칸을 채워주세요 :)'}, )

        elif password != password2:
            return render(request, 'user/signup.html', {'error': '인증비밀번호가 맞지 않습니다 ;)'})

        elif UserModel.objects.filter(email=email).exists():
            return render(request, 'user/signup.html', {'error': '이미 사용하고 있는 이메일입니다 ;)'})
        else:
            exist_user = get_user_model().objects.filter(email=email)
            if exist_user:
                return render(request, 'user/signup.html', {'error': '이메일이 이미 존재합니다 ;( '})
            else:
                user = UserModel.objects.create_user(
                    email=email, password=password)
                user.username = username
                user.save()
                return redirect('/welcome/signin')


def sign_in_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signin.html')
    elif request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        username = request.POST.get('username', None)
        exist_user = get_user_model().objects.filter(email=email)[0]
        if exist_user.is_deleted:
            return render(request, 'user/signin.html', {'error': '탈퇴한 계정입니다 ;( '})
        me = auth.authenticate(request, email=email,
                               password=password, username=username)
        if me is not None:  
            auth.login(request, me)
            return redirect('/')
        else:
            return render(request, 'user/signin.html', {'error': '회원정보가 일치하지 않습니다 ;( '})


@login_required
def logout(request):
    auth.logout(request)  # 인증되어있는 정보를 없애기
    return redirect("/")


def test(request):
    return render(request, "user/start_base.html")

