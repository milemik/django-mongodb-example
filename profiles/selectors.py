from typing import Mapping

from core.mongo_db import get_default_db


class ProfileSelector:
    def __init__(self) -> None:
        db = get_default_db()
        self.profile_table = db["profiles"]

    def get_user_by_email(self, email: str) -> Mapping[str, any]:
        return self.profile_table.find_one({"email": email})

    def get_all_profiles(self) -> list:
        response = self.profile_table.find({}, {"_id": 0})
        return list(response)
