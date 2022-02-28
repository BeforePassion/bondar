from datetime import datetime


from django.conf import settings


from django.contrib.auth.models import (
    AbstractBaseUser,
    AbstractUser,
    BaseUserManager,
    PermissionsMixin,
)

from django.core.validators import RegexValidator  # 전화번호 유효성검사


from django.db import models


# Create your models here.
class UserProfileManager(BaseUserManager):
    def create_user(self, email, password=None, username=None):
        if not email:

            raise ValueError("제대로 된 이메일 형식이 아닙니다 ;)")

            raise ValueError("Please provide an email address")


        email = self.normalize_email(email)
        user = self.model(email=email)
        username = self.model.normalize_username(username)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create a new superuser profile"""
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserModel(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255)
    friend = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="friends")
    # point = models.IntegerField(default=0)
    phoneNumberRegex = RegexValidator(regex=r"^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$")  # 정규표현식을 사용한 전화번호 표기방식
    phone = models.CharField(validators=[phoneNumberRegex], max_length=11, unique=True)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        db_table = "user"

    is_deleted = models.BooleanField(default=False, verbose_name="delete or not")

    deleted_at = models.DateTimeField(null=True)

    def delete(self, using=None, keep_parent=False):
        self.is_deleted = True
        self.deleted_at = datetime.now()
        self.save()

    def __str__(self):
        return self.email
