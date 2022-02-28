from typing import Tuple

from django.http import HttpRequest
from ninja import Form, Router

from userprofile.models import UserProfile
from userprofile.services.profile_service import async_create_image, async_edit_image

from .schemas import FileUrlRequest, FileUrlResponse

router = Router(tags=["images"])


@router.post("/file", url_name="file", response={201: FileUrlResponse})
async def create_file_url(request: HttpRequest, file_request: FileUrlRequest = Form(...)) -> Tuple[int, UserProfile]:
    result = await async_create_image(file_request.user_id, file_request.original_image_url, file_request.nst_image_url)
    return 201, result


@router.put("/update-file", url_name="update-file", response=FileUrlResponse)
async def create_file_url(request: HttpRequest, file_request: FileUrlRequest = Form(...)) -> UserProfile:
    # 모델에 유저 이미지 수정하는 서비스불러오기
    result = await async_edit_image(file_request.user_id, file_request.original_image_url, file_request.nst_image_url)
    return result
