from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from rest_framework.test import APIClient

from core.mongo_db import get_default_db
from profiles.models import Profile
from profiles.services import ProfileService


class ProfileTestClass(TestCase):
    def setUp(self):
        self.profile = Profile(first_name="John", last_name="Doe", birth_date="", email="<EMAIL>", gender="male")

    def test_check_email(self):
        self.assertFalse(self.profile._check_email())


class ProfileClientMock:
    def __init__(self) -> None:
        db = get_default_db()
        self.profile_table = db["profiles_test"]


class ProfileServiceMock(ProfileService):
    def __init__(self) -> None:
        super().__init__()
        self.profile_table = ProfileClientMock().profile_table


class ProfileViewTestClass(TestCase):
    def setUp(self):
        self.create_url = reverse("profiles:create_profile")
        self.get_all_profile_url = reverse("profiles:all_profiles")
        self.client = APIClient()

    def test_create_profile_init(self):
        response = self.client.post(self.create_url, {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_profile(self):
        with patch("profiles.views.ProfileService", return_value=ProfileServiceMock()) as mock_collection:
            response = self.client.post(self.create_url, {"email": "test@test.com"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(mock_collection.call_count, 1)

    def tearDown(self):
        ProfileClientMock().profile_table.drop()
