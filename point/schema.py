from ninja import Schema, ModelSchema
from point.models import PointHistory


class PointSchema(ModelSchema):
    class Config:
        model = PointHistory
        model_fields = ['point', 'history', 'usage']


class NotEnoughPoint(Schema):
    message: str

