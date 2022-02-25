from ninja import Schema


class FileUrlRequest(Schema):
    user_id: int
    original_image_url: str
    nst_image_url: str
