from ninja import Schema


class FileUrlRequest(Schema):
    # user_id: int
    original_file_url: str
    nst_file_url: str
