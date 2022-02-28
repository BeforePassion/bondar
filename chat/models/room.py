from chat.models.base_model import BaseModel


class Room(BaseModel):
    class Meta:
        db_table = "room"
