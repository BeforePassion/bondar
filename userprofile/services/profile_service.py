from typing import cast

from asgiref.sync import sync_to_async
from userprofile.models import UserProfile


def create_image(original_file_url: str, nst_file_url: str) -> UserProfile:
    # User.objects.filter(id=user_id).get()
    return UserProfile.objects.create(
        original_image=original_file_url, nst_image=nst_file_url)


async def async_create_image(original_file_url: str, nst_file_url: str) -> UserProfile:
    result = await sync_to_async(create_image)(original_file_url, nst_file_url)
    return cast(UserProfile, result)


def editUser(user_id: int) -> None:
    # User.objects.filter(id=user_id).get()
    return
