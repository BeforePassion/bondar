from typing import Tuple

from userprofile.models import UserProfile
from userprofile.services.profile_service import async_create_image
from .schemas import FileUrlResponse, FileUrlRequest
from ninja import Router, Form
from django.http import HttpRequest

router = Router()


@router.post("/file", url_name='file', response={201: FileUrlResponse})
async def create_file_url(request: HttpRequest, file_request: FileUrlRequest = Form(...)) -> Tuple[int, UserProfile]:
    # 모델에 유저 이미지 저장하는 서비스불러오기
    result = await async_create_image(file_request.original_file_url, file_request.nst_file_url)
    return 201, result
