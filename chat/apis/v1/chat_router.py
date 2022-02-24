from django.http import HttpRequest
from django.shortcuts import render
from ninja import Router

router = Router()

@router.post("/")
def chat_view(request: HttpRequest) -> render:
    return render(request, 'chat/chat.html')