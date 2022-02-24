from ninja import Schema


class FileUrlResponse(Schema):
    # user_id:int
    original_image: str
    nst_image: str
