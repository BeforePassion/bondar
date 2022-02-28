from django.db import models

from core.models import BaseModel
from user.models import UserModel


class PointHistory(BaseModel):
    user_id = models.ForeignKey("user.UserModel", related_name="user_id", on_delete=models.CASCADE, db_column="user_id")
    point = models.IntegerField(default=0)
    history = models.CharField(max_length=255)  # 사용내역
    usage = models.BooleanField(default=True)  # 충전: True / 사용: False
