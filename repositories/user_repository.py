from pymongo.collection import Collection
from bson import ObjectId


class UserRepository:

    def __init__(self, users_collection: Collection):
        self.users_collection = users_collection

    def find_by_email(self, email: str):
        return self.users_collection.find_one(
            {"email": email}
        )

    def create_user(self, user_data: dict) -> str:
        result = self.users_collection.insert_one(user_data)

        return str(result.inserted_id)

    def find_by_id(self, user_id: str):
        if not ObjectId.is_valid(user_id):
            return None

        return self.users_collection.find_one(
            {"_id": ObjectId(user_id)}
        )