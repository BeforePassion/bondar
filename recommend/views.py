from django.shortcuts import render, redirect
from user.models import UserModel
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def i_like_user_view(request):
    if request.method == 'GET':
        # 현재 로그인 한 유저의 아이디 불러오기
        user = UserModel.objects.get(id=request.user.id)
        # 현재 로그인 한 유저가 좋아요 한 계정 전체 불러오기
        i_like_user_list = user.friend.all()
        return render(request, 'recommend/i_like.html', {'i_like_user_list': i_like_user_list})


@login_required
def like_me_user_view(request):
    if request.method == 'GET':
        user_list = UserModel.objects.exclude(id=request.user.id)
        id_list = []
        like_me_friends_id_list = []
        like_me_user_list = []
        for user in user_list:
            user_id = user.id
            id_list.append(user_id)

        for friend_id in id_list:
            friend_list = UserModel.objects.get(id=friend_id)
            friend_like_user_list = friend_list.friend.all()
            for friend_like_user in friend_like_user_list:
                friend_like_user_id = friend_like_user.id
                if friend_like_user_id == request.user.id:
                    like_me_friends_id_list.append(friend_id)

        for like_me_friends_id in like_me_friends_id_list:
            like_me_friend = UserModel.objects.get(id=like_me_friends_id)
            like_me_user_list.append(like_me_friend)
        return render(request, 'recommend/like_me.html', {'like_me_user_list': like_me_user_list})


@login_required
def user_unlike(request, id):
    click_user = UserModel.objects.get(id=id)
    click_user.friends.remove(request.user)
    return redirect('i_like')


@login_required
def both_like_user_view(request):
    if request.method == 'GET':
        from user.models import UserModel

        id_list = []
        like_me_friends_id_list = []

        user = UserModel.objects.get(id=request.user.id)
        i_like_list = user.friend.all()
        for friend in i_like_list:
            id_list.append(friend.id)

        for friend_id in id_list:
            friend_list = UserModel.objects.get(id=friend_id)
            friend_like_user_list = friend_list.friend.all()
            for friend_like_user in friend_like_user_list:
                friend_like_user_id = friend_like_user.id
                if friend_like_user_id == request.user.id:
                    like_me_friends_id_list.append(friend_id)

        set_list = set(id_list) & set(like_me_friends_id_list)
        both_like_id_list = list(set_list)
        both_like_user_list = []
        for id in both_like_id_list:
            both_like_user = UserModel.objects.get(id=id)
            both_like_user_list.append(both_like_user)
    return render(request, 'recommend/both_like.html', {'both_like_user_list': both_like_user_list})
