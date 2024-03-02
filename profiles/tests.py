from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from rest_framework.test import APIClient

from core.mongo_db import get_default_db
from profiles.models import Profile
from profiles.selectors import ProfileSelector
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


class ProfileSelectorMock(ProfileSelector):
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
            with patch("profiles.services.ProfileSelector", return_value=ProfileSelectorMock()) as mock_selector:
                response_one = self.client.post(self.create_url, {"email": "test@test.com"})
                response_two = self.client.post(self.create_url, {"email": "test@test.com"})

        self.assertEqual(response_one.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_two.status_code, status.HTTP_201_CREATED)
        self.assertEqual(mock_collection.call_count, 2)
        self.assertEqual(mock_selector.call_count, 2)
        self.assertEqual(ProfileClientMock().profile_table.count_documents({}), 1)

    def test_list_profile(self):
        with patch("profiles.views.ProfileSelector", return_value=ProfileSelectorMock()) as mock_selector:
            response = self.client.get(self.get_all_profile_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(mock_selector.call_count, 1)
        self.assertEqual(response.data.get("profiles"), [])

    def test_list_profile_with_profile(self):
        profile = Profile(email="test@test.com")
        ProfileClientMock().profile_table.insert_one(profile.to_dict())

        with patch("profiles.views.ProfileSelector", return_value=ProfileSelectorMock()) as mock_selector:
            response = self.client.get(self.get_all_profile_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(mock_selector.call_count, 1)
        self.assertEqual(
            response.data.get("profiles"),
            [
                {
                    "birth_date": "",
                    "email": "test@test.com",
                    "email_verified": False,
                    "first_name": "",
                    "gender": "",
                    "last_name": "",
                }
            ],
        )

    def tearDown(self):
        ProfileClientMock().profile_table.drop()
