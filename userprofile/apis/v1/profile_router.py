from typing import Tuple

from django.http import HttpRequest
from ninja import Form, Router
from user.models import UserModel

from userprofile.models import UserProfile
from userprofile.services.profile_service import update_user, load_image, async_create_image, async_edit_image

from .schemas import FileUrlRequest, FileUrlResponse, ProfileRequest, UserSchema

router = Router(tags=["profile"])


@router.get("/{user_id}", url_name="user", response=FileUrlResponse)
def get_user_image(request: HttpRequest, user_id: int) -> UserProfile:
    result = load_image(user_id)
    return result


@router.post("/{user_id}", url_name="update_user", response=UserSchema)
def update_user_profile(request: HttpRequest, user_id: int, profile_request: ProfileRequest = Form(...)) -> UserModel:
    result = update_user(user_id,
                         profile_request.username, profile_request.birth, profile_request.target_gender)
    return result


@router.post("/file", url_name="file", response={201: FileUrlResponse})
async def create_file_url(request: HttpRequest, file_request: FileUrlRequest = Form(...)) -> Tuple[int, UserProfile]:
    result = await async_create_image(file_request.user_id, file_request.original_image_url, file_request.nst_image_url)
    return 201, result


@router.post("/update_file", url_name="update_file", response=FileUrlResponse)
async def update_file_url(request: HttpRequest, file_request: FileUrlRequest = Form(...)) -> UserProfile:
    # 모델에 유저 이미지 수정하는 서비스불러오기
    result = await async_edit_image(file_request.user_id, file_request.original_image_url, file_request.nst_image_url)
    return result
