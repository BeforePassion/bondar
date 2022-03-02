from typing import Tuple

from django.db.models import QuerySet

from chat.models import Room, RoomJoin


def creat_an_chat_room() -> Room:
    return Room.objects.create()


def creat_an_room_join(user_id1: int, user_id2: int, room_id: int) -> Tuple[RoomJoin, RoomJoin]:
    room_join1 = RoomJoin.objects.create(user_id=user_id1, room_id=room_id)
    room_join2 = RoomJoin.objects.create(user_id=user_id2, room_id=room_id)
    return room_join1, room_join2


def get_an_chat_room(room_id: int) -> Room:
    return Room.objects.get(id=room_id)


def get_an_chat_room_list(user_id: int) -> QuerySet[RoomJoin]:
    return RoomJoin.objects.filter(user_id=user_id)


def get_chat_room_user(room_id: int) -> QuerySet[RoomJoin]:
    return RoomJoin.objects.filter(room_id=room_id)


def confirm_user_chat_room_join(user_id: int, room_id: int) -> RoomJoin:
    return RoomJoin.objects.get(user_id=user_id, room_id=room_id)