from ninja import Schema


class ProfileRequest(Schema):
    username: str
    birth: str
    target_gender: str
