from django.db import models

from chat.models.base_model import BaseModel


class Room(BaseModel):
    roomName = models.CharField(max_length=1000)
    user1 = 1
    user2 = 2
    pass
