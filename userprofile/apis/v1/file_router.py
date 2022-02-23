from .schemas import FileUrlResponse, FileUrlRequest
from ninja import Router, Form
from django.http import HttpRequest

router = Router()


@router.post("/file-url", url_name='file-url', response=FileUrlResponse)
def file_url(request: HttpRequest, file_request: FileUrlRequest = Form(...)) -> dict:
    # 모델에 유저 이미지 저장하는 서비스불러오기
    return
