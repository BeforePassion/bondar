from ninja import Schema


class FileUrlRequest(Schema):
    original_file_url: str
    file_url: str
