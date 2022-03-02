from django.db.models import QuerySet

from chat.models import Message


def creat_an_message(user_id: int, room_id: int, message: str) -> Message:
    return Message.objects.create(user_id=user_id, room_id=room_id, message=message)


def get_an_message_list(room_id: int) -> QuerySet[Message]:
    return Message.objects.filter(room_id=room_id)
