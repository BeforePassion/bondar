from django.db import models

from core.models import BaseModel


class UserProfile(BaseModel):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_image = models.CharField(max_length=255)
    nst_image = models.CharField(max_length=255)
    pass
