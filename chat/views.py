from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from chat.models import RoomJoin
from chat.services.chat_room_service import get_an_chat_room_list, get_chat_room_user, confirm_user_chat_room_join, \
    creat_an_chat_room, creat_an_room_join
from chat.services.message_service import get_an_message_list

from user.models import UserModel

from collections import Counter

# Create your views here. / views 호출하려면 매핑되는 URLconf 필요
# chat_view 함수를 호출하면 chat.html 을 렌더해주는 함수
@login_required
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
                username = chat_user.user_id.email
                username_list.append(username)

            # chat_info 변수에 딕셔너리 형태로 저장
            chat_info[room_id] = username_list

        if chat_info == {}:
            chat_info = None

        return render(request, "chat/chat.html", {'chat_info': chat_info})
    # 사용자가 없으면 로그인화면
    else:
        return redirect(("/welcome/sign-in"))


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


@login_required
def api_create_room(request: HttpRequest, user_id: int) -> HttpResponse:
    user1 = UserModel.objects.get(id=request.user.id)
    user2 = UserModel.objects.get(id=user_id)

    find_room_qs = RoomJoin.objects.filter(user_id__in=[user1.id, user2.id])
    #이러면 1번 유저가 참여한 모든 방, 2번 유저가 모두 참여한 방 가져옴

    find_room_list = []
    for find_room in find_room_qs:
        find_room_list.append(find_room.room_id)

    result = Counter(find_room_list)
    for key,value in result.items():
        if value >= 2:
            return redirect(("/chat/"+str(key.id)))

    room = creat_an_chat_room()
    room_id = room.id
    creat_an_room_join(user1, user2, room)

    return redirect(("/chat/"+str(room_id)))