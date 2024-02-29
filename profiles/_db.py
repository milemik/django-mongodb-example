from common.mongodb import get_default_db


class ProfileCollection:
    def __init__(self) -> None:
        db = get_default_db()
        self.profile_table = db["profiles"]
