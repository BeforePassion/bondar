from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def test(reqeust: HttpRequest) -> HttpResponse:
    return render(reqeust, "profile/profile.html")
