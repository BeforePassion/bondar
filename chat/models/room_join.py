from django.db import models

from chat.models.base_model import BaseModel
from chat.models.room import Room
from user.models import UserModel


class RoomJoin(BaseModel):

    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="roomJoin", db_column="user_id")
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="roomJoin", db_column="room_id")

    class Meta:
        db_table = "roomJoin"
