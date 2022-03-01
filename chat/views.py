from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from chat.services.chat_room_service import get_an_chat_room_list, get_chat_room_user, confirm_user_chat_room_join
from chat.services.message_service import get_an_message_list

# Create your views here. / views 호출하려면 매핑되는 URLconf 필요
# chat_view 함수를 호출하면 chat.html 을 렌더해주는 함수
# @login_required
def chat_view(request: HttpRequest) -> HttpResponse:
    # 사용자가 있는지 없는지 판단
    user = request.user.is_authenticated
    # 사용자가 있으면 사용자가 속해있는 채팅방 list 표시
    if user:
        # 유저가 참여하고 있는 채팅방 목록(roomJoin 쿼리)
        chat_room_list = get_an_chat_room_list(request.user.id)

        chat_info = {}
        for chat_room in chat_room_list:
            room_id = chat_room.room_id.id
            # 채팅방에 참여중인 유저 list(roomJoin 쿼리)
            chat_user_list = get_chat_room_user(room_id)

            username_list = []
            for chat_user in chat_user_list:
                username = chat_user.user_id.username
                username_list.append(username)

            # chat_info 변수에 딕셔너리 형태로 저장
            chat_info[room_id] = username_list

        if chat_info == {}:
            chat_info = None

        return render(request, "chat/chat.html", {'chat_info': chat_info})
    # 사용자가 없으면 로그인화면
    else:
        return redirect(("/wellcom/sign-in"))


# room 함수를 호출하면 room.html 을 렌더해주는 함수 / dict 형태로 room_name value 를 전송
@login_required
def room_view(request: HttpRequest, room_name: str) -> HttpResponse:
    room_id = int(room_name)
    try:
        confirm_user_chat_room_join(request.user.id, room_id)

        message = get_an_message_list(room_id)
        return render(request, "chat/room.html", {"room_name": room_name, "message": message})

    except:
        return redirect(("/chat"))

