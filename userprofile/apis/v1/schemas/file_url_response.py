from ninja import Schema


class FileUrlResponse(Schema):
    user_id: int
    original_image_url: str
    nst_image_url: str
