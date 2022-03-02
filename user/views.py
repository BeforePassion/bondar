
from django.shortcuts import render, redirect
from django.views import View

from point.models import PointHistory
from userprofile.models import UserProfile
from .models import UserModel
from django.contrib.auth import get_user_model  # 사용자가 데이터베이스 안에 있는지 검사하는 함수
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from .utils import token_generator


def startpage(request):
    if request.method == 'GET':
        return render(request, 'user/intro.html')

def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user :
            if request.user.invalid_user == True: 
                return redirect('/main') 
            elif request.user.invalid_user == False:
                return redirect('/register')
        else:
            return render(request, 'user/signup.html')
    elif request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)


        if email == '' or password == '':
            return render(request, 'user/signup.html', {'error': '빈칸을 채워주세요 :)'}, )

        elif password != password2:
            return render(request, 'user/signup.html', {'error': '인증비밀번호가 맞지 않습니다 ;)'})

        elif UserModel.objects.filter(email=email).exists():
            return render(request, 'user/signup.html', {'error': '이미 사용하고 있는 이메일입니다 ;)'})
        else:
            exist_user = get_user_model().objects.filter(email=email)
            if exist_user:
                return render(request, 'user/signin.html', {'error': '이메일이 이미 존재합니다 ;( '})
            else:
                user = UserModel.objects.create_user(
                    email=email, password=password)
                user.is_active = True
                user.save()

                # email verification tests

                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
                domain = get_current_site(request).domain
                link= reverse('activate', kwargs={'uidb64':uidb64, 'token':token_generator.make_token(user)})

                activate_url = 'https://'+domain+link

                email_subject = 'bondar계정을 인증하세요:)'
                email_body = '안녕하세요 '+user.username+':)' +' 이 링크를 통하여 계정을 인증하세요!\n'+activate_url
                email = EmailMessage(
                    email_subject,
                    email_body,
                    'noreply@bondar.com',
                    [email],
                )
                email.send()

                # messages.success(request,'계정이 생성되었습니다 :)')
                point = PointHistory.objects.create(user_id = user.id)
                point.save()
                return redirect('/sign-in')


def sign_in_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user :
            print(request.user.invalid_user)
            if request.user.invalid_user == True: 
                return redirect('/main')
            elif request.user.invalid_user == False:
                return redirect('/register')
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
            if me.invalid_user == True:
                return redirect('/main')
            else:
                return redirect('/register')
        else:
            return render(request, 'user/signin.html', {'error': '회원정보가 일치하지 않습니다 ;( '})


@login_required
def logout(request):
    auth.logout(request)  # 인증되어있는 정보를 없애기
    return redirect("/sign-in")

class VerificationView(View):
    def get(self, request, uidb64, token):
        return redirect('/sign-in')

def register_user(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user :
            if request.user.invalid_user == True: 
                return redirect('/main')
            elif request.user.invalid_user == False:
                return render(request, 'user/register.html')
        else:
            return redirect('/sign-up')
    
    elif request.method == 'POST':
        user = request.user
        myuser = UserModel.objects.get(id=user.id)
        exist_profile = UserProfile.objects.filter(user=user.id).exists()
        if user.is_authenticated:
            if exist_profile:
                myuser.username = request.POST.get('username')
                myuser.birth = request.POST.get('birth')
                myuser.gender = request.POST.get('gender')
                myuser.target_gender = request.POST.get('target_gender')
                myuser.invalid_user = 1
                myuser.save()
                return redirect('/main')
            else:
                return render(request, 'user/register.html', {'error': '이미지는 필수!'})
        else:
            redirect('/sign-in')
