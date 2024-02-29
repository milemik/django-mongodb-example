from common.mongodb import get_default_db, DB_SELECT_TYPE


class ProfileSelector:
    def __init__(self) -> None:
        self.db = get_default_db()

    @staticmethod
    def get_user_by_email(db: DB_SELECT_TYPE, email: str) -> None:
        return db.find_one({"email": email})
