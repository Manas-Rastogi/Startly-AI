from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")

if not MONGODB_URL:
    raise ValueError("MongoDB URL not found!")

if not MONGODB_URL.startswith("mongodb+srv://"):
    raise ValueError("Invalid MongoDB Atlas connection URL!")

print("MongoDB URL loaded successfully!")
print("Using Atlas:", MONGODB_URL.startswith("mongodb+srv://"))

client = MongoClient(
    MONGODB_URL,
    serverSelectionTimeoutMS=10000
)

db = client["startly_ai"]

users_collection = db["users"]
startups_collection = db["startups"]
contacts_collection = db["contacts"]

client.admin.command("ping")

print("MongoDB Atlas connected successfully!")