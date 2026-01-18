from dotenv import load_dotenv
import os

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "RecommenderSystem")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

PORT = int(os.getenv("PORT", "8000"))
ENV = os.getenv("ENV", "development")

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB", "movie_recommender")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
