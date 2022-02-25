from django.db import models

from core.models import BaseModel


class UserProfile(BaseModel):
    user = models.ForeignKey("user.UserModel", on_delete=models.CASCADE)
    original_image_url = models.CharField(max_length=255)
    nst_image_url = models.CharField(max_length=255)
