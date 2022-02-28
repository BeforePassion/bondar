from django.test import TestCase

from chat.models import Room
from chat.services.chat_room_service import creat_an_chat_room


class TestArticleService(TestCase):
    def test_you_can_creat_an_room(self) -> None:
        # Given

        # When
        room = creat_an_chat_room()
        # Then
        self.assertIsNotNone(room)

    def test_you_can_get_an_room_by_id(self) -> None:
        # Given
        room = creat_an_chat_room()

        # When
        result_room = Room.objects.get(id=room.id)

        # Then
        self.assertEqual(room.id, result_room.id)
