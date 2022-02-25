from typing import cast

from asgiref.sync import sync_to_async

from user.models import UserModel
from userprofile.models import UserProfile


def create_image(user_id: int, original_image_url: str, nst_image_url: str) -> UserProfile:
    UserModel.objects.filter(id=user_id).get()
    return UserProfile.objects.create(
        user_id=user_id, original_image_url=original_image_url, nst_image_url=nst_image_url
    )


async def async_create_image(user_id: int, original_image_url: str, nst_image_url: str) -> UserProfile:
    result = await sync_to_async(create_image)(user_id, original_image_url, nst_image_url)
    return cast(UserProfile, result)


def edit_image(user_id: int, original_image_url: str, nst_image_url: str) -> UserProfile:
    UserModel.objects.filter(id=user_id).get()
    userImage = UserProfile.objects.filter(user_id=user_id).get()
    userImage.original_image_url = original_image_url
    userImage.nst_image_url = nst_image_url
    userImage.save(update_fields=['original_image_url', 'nst_image_url'])
    return userImage


async def async_edit_image(user_id: int, original_image_url: str, nst_image_url: str) -> UserProfile:
    result = await sync_to_async(edit_image)(user_id, original_image_url, nst_image_url)
    return cast(UserProfile, result)
