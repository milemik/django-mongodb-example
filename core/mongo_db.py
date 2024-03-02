from core.settings import DB_SELECT_TYPE, CLIENT, MONGODB_DB_NAME


def get_default_db() -> DB_SELECT_TYPE:
    return CLIENT[MONGODB_DB_NAME]
