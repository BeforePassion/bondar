from django.shortcuts import render

# Create your views here.
from user.models import UserModel


def ilike(request):
    if request.method == 'GET':
        user_list = UserModel.objects.all().exclude(id=request.user.id)
        return render(request, 'recommend/ilike.html')
