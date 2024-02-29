import re
from dataclasses import dataclass

from rest_framework.exceptions import ValidationError


@dataclass
class Profile:
    email: str
    first_name: str = ""
    last_name: str = ""
    birth_date: str = ""
    gender: str = ""
    email_verified: bool = False

    def _check_email(self) -> bool:
        """Will return True if email is OK, else will return False"""
        if not self.email:
            return False
        return bool(re.match(r"[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+", self.email))

    def full_check(self):
        if not self._check_email():
            raise ValidationError(f"Email must be defined!")

    def to_dict(self) -> dict:
        return self.__dict__
