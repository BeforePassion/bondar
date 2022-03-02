from django.shortcuts import render, redirect
from user.models import UserModel
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def user_view(request):
    if request.method == 'GET':
        # 현재 로그인 한 유저의 아이디 불러오기
        user = UserModel.objects.get(id=request.user.id)
        # 현재 로그인 한 유저가 좋아요 한 계정 전체 불러오기
        i_like_list = user.friend.all()
        i_hate_list = user.hate.all()
        like_num = []
        hate_num = []
        # 빈 리스트에 현재 로그인 한 유저가 좋아요 한 계정의 id값을 담기
        for hate_user in i_hate_list:
            num_hate = hate_user.id
            hate_num.append(num_hate)
        for like_user in i_like_list:
            num_like = like_user.id
            like_num.append(num_like)
        sum_list = hate_num + like_num
        sum_list.append(request.user.id)
        set_list = list(set(sum_list))
        # exclude로 id값이 담긴 리스트를 통해 현재 로그인 한 유저가 좋아요 한 계정을 제외한 유저를 유저 리스트에 담기
        user_list = UserModel.objects.all().exclude(id__in=set_list)
        return render(request, 'main.html', {'user_list': user_list})


@login_required
def user_like(request, id):
    click_user = UserModel.objects.get(id=id)
    click_user.friends.add(request.user)
    return redirect('/main')


@login_required
def user_hate(request, id):
    click_user = UserModel.objects.get(id=id)
    click_user.hates.add(request.user)
    return redirect('/main')
