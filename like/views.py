from django.shortcuts import render, redirect
from user.models import UserModel
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def user_follow(request):
    if request.method == 'POST':
        me = request.user
        click_user = UserModel.objects.get(id=me.id)
        if me in click_user.followee.all():
            click_user.friend.remove(request.user)
        else:
            click_user.friend.add(request.user)
        return redirect('/main')
    elif request.method == 'GET':
        return render(request, 'main.html')