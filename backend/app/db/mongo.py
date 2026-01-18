import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB", "movie_recommender")

if not MONGO_URI:
    raise RuntimeError("MONGO_URI not set in environment variables")

client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)

try:
    client.admin.command("ping")
    print("✅ MongoDB connected successfully")
except ConnectionFailure:
    raise RuntimeError("❌ Could not connect to MongoDB")

db = client[MONGO_DB]
search_logs = db["search_logs"]
