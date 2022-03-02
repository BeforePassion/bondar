from ninja import Schema
from ninja.orm import create_schema

from user.models import UserModel

UserSchema = create_schema(
    UserModel, fields=['id', 'username', 'birth', 'target_gender'])
