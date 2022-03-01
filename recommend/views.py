from django.shortcuts import render

# Create your views here.
from user.models import UserModel


def user_view(request):
    if request.method == 'GET':
        user_list = UserModel.objects.all().exclude()
