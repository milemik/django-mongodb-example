from django.test import TestCase, override_settings
from django.urls import reverse
from rest_framework import status

from rest_framework.test import APIClient

from profiles.models import Profile


class ProfileTestClass(TestCase):
    def setUp(self):
        self.profile = Profile(first_name="John", last_name="Doe", birth_date="", email="<EMAIL>", gender="male")

    def test_check_email(self):
        self.assertFalse(self.profile._check_email())


class ProfileViewTestClass(TestCase):
    def setUp(self):
        self.create_url = reverse("profiles:create_profile")
        self.get_all_profile_url = reverse("profiles:all_profiles")
        self.client = APIClient()

    def test_create_profile_init(self):
        response = self.client.post(self.create_url, {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
