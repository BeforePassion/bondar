from django.shortcuts import render


def test(reqeust):
    return render(reqeust, "profile/test.html")
