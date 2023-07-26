# backend/services/database.py

from pymongo import MongoClient
from config import MONGODB_CONNECTION_STRING

client = MongoClient(MONGODB_CONNECTION_STRING)
db = client.get_default_database()  # This will get the database you specified in the connection string
