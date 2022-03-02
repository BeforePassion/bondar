from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render


def profile(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        user = request.user
        if user.is_authenticated:
            if user.invalid_user:
                return render(request, "profile/update_profile.html")
            else:
                return redirect('/register')
        else:
            return redirect('/sign-in')


def image_profile(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        user = request.user
        if user.is_authenticated:
            if user.invalid_user:
                return render(request, "profile/update_image.html")
            else:
                return redirect('/register')
        else:
            return redirect('/sign-in')
