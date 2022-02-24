from django.db import models

from core.models import BaseModel


class PointHistory(BaseModel):
    # user
    point = models.IntegerField(default=0)
    history = models.CharField(max_length=255)
    usage = models.BooleanField(default=True)  # 충전: True / 사용: False