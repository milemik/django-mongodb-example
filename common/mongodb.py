from typing import Mapping

from pymongo.database import Database
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from django.conf import settings

uri = f"mongodb+srv://{settings.MONGODB_USER}:{settings.MONGODB_PASSWORD}@{settings.MONGODB_URL}/?retryWrites=true&w=majority&appName={settings.MONGODB_APP_NAME}"

# Create a new client and connect to the server
CLIENT = MongoClient(uri, server_api=ServerApi("1"))

# Send a ping to confirm a successful connection
try:
    CLIENT.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

DB_SELECT_TYPE = Database[Mapping[str, any]]


def get_default_db() -> DB_SELECT_TYPE:
    return CLIENT[settings.MONGODB_DB_NAME]
