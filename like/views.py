from random import random

from django.shortcuts import render, redirect

from userprofile.models import UserProfile
from user.models import UserModel
from django.contrib.auth.decorators import login_required


# Create your views here.
# @login_required
# def user_list(request):
#     if request.method == 'GET':
#         random_num = random.randint(1, UserModel.objects.all.count())
#         user = UserModel.objects.exclude(id=random_num)
#         user_img = UserProfile.objects.filter(user_id=user.id)
#         return render(request, 'main.html', {'user': user, 'user_img': user_img})
@login_required
def user_view(request):
    if request.method == 'GET':
        # 사용자를 불러오기, exclude와 request.user.username 를 사용해서 '로그인 한 사용자'를 제외하기
        user = UserModel.objects.get(id=request.user.id)
        i_like_list = user.friend.all()
        like_num = []
        for user in i_like_list:
            num = user.id
            like_num.append(num)
        user_list = UserModel.objects.all().exclude(id__in=like_num)
        return render(request, 'main.html', {'user_list': user_list})


@login_required
def user_follow(request, id):
    me = request.user
    click_user = UserModel.objects.get(id=id)
    click_user.friends.add(request.user)
    return redirect('/main')

# def unlike
# if me in click_user.friends.all():
#     click_user.friends.remove(request.user)

# @login_required
# def user_follow(request):
#     if request.method == 'POST':
#         me = request.user
#         click_user = UserModel.objects.get(id=me.id)
#         if me in click_user.followee.all():
#             click_user.friend.remove(request.user)
#         else:
#             click_user.friend.add(request.user)
#         return redirect('/main')
#     elif request.method == 'GET':
#         return render(request, 'main.html')