from django.test import TestCase

from user.models import UserModel
from userprofile.services.profile_service import create_image, edit_image


class TestProfileService(TestCase):
    def test_you_can_create_an_image(self) -> None:
        # Given
        user = UserModel.objects.create(email="email", password="password")
        original_image_url = "test_original_image_url"
        nst_image_url = "test_nst_image_url"

        # When
        file_url = create_image(user_id=user.id, original_image_url=original_image_url, nst_image_url=nst_image_url)

        # Then
        self.assertEqual(file_url.original_image_url, original_image_url)
        self.assertEqual(file_url.nst_image_url, nst_image_url)

    def test_you_can_update_an_image(self) -> None:
        # Given
        user = UserModel.objects.create(email="email", password="password")
        create_image(user_id=user.id, original_image_url="", nst_image_url="")

        # When
        original_image_url = "test_original_image_url"
        nst_image_url = "test_nst_image_url"
        file_url = edit_image(user_id=user.id, original_image_url=original_image_url, nst_image_url=nst_image_url)

        # Then
        self.assertEqual(file_url.original_image_url, original_image_url)
        self.assertEqual(file_url.nst_image_url, nst_image_url)
