from django.db import models

from core.models import BaseModel
from user.models import UserModel


class PointHistory(BaseModel):
    user = models.ForeignKey("user.UserModel", on_delete=models.CASCADE)
    point = models.IntegerField(default=0)
    history = models.CharField(max_length=255)  # 사용내역
    usage = models.BooleanField(default=True)  # 충전: True / 사용: False
