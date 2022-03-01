from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


def profile(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return render(request, "profile/update_profile.html")
        else:
            return redirect('/sign-in')


def image_profile(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return render(request, "profile/update_image.html")
        else:
            return redirect('/sign-in')
