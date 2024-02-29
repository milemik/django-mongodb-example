from django.test import TestCase

from profiles.models import Profile


class ProfileTestClass(TestCase):
    def setUp(self):
        self.profile = Profile(first_name="John", last_name="Doe", birth_date="", email="<EMAIL>", gender="male")

    def test_check_email(self):
        self.assertFalse(self.profile._check_email())
