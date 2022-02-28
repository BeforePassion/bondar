from django.shortcuts import redirect, render

# Create your views here.


def test(request):
    return render(request, "user/start_base.html")

