from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here. / views 호출하려면 매핑되는 URLconf 필요
# chat_view 함수를 호출하면 chat.html 을 렌더해주는 함수
def chat_view(request: HttpRequest, ) -> HttpResponse:

    return render(request, "chat/chat.html")


# room 함수를 호출하면 room.html 을 렌더해주는 함수 / dict 형태로 room_name value 를 전송
def room_view(request: HttpRequest, room_name: str) -> HttpResponse:
    return render(request, "chat/room.html", {"room_name": room_name})
