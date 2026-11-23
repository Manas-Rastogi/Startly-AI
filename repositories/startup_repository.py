
from datetime import datetime, timezone
from database.connection import startups_collection, contacts_collection


class StartupRepository:

    def __init__(self, database):

        self.startups = database["startups"]
        self.contacts = database["contacts"]

    # Check duplicate startup
    def startup_exists(self, startup_name):

        return self.startups.find_one({
            "startup_name": {
                "$regex": f"^{startup_name}$",
                "$options": "i"
            }
        }) is not None

    # Save new startup
    def save_startup(self, startup):

        startup["contact_analysis"] = False
        startup["search_completed"] = False
        startup["created_at"] = datetime.now(timezone.utc)

        result = self.startups.insert_one(startup)

        return result.inserted_id

    # Get pending startups
    def get_pending_startups(self):

        print("Total startups:", self.startups.count_documents({}))

        pending = list(
            self.startups.find({
                "contact_analysis": {"$ne": True}
            })
        )

        print("Pending startups:", len(pending))

        return pending

    # Save Tavily search data
    def save_search_data(self, startup_id, search_data):

        result = self.startups.update_one(
            {"_id": startup_id},
            {
                "$set": {
                    "search_data": search_data,
                    "search_completed": True,
                    "search_completed_at": datetime.now(timezone.utc)
                }
            }
        )

        return result.modified_count > 0 or result.matched_count > 0

    # Save employee contacts
    def save_contact(self, startup_id, startup_name, contact):

        if not isinstance(contact, dict):
            return None

        name = contact.get("name")

        if not name:
            return None

        # Support Groq field names
        email = (
            contact.get("public_email")
            or contact.get("email")
        )

        linkedin = (
            contact.get("linkedin_profile_url")
            or contact.get("linkedin_url")
            or contact.get("linkedin")
        )

        # Normalize contact data
        contact_data = contact.copy()

        contact_data["name"] = name
        contact_data["email"] = email
        contact_data["linkedin_url"] = linkedin

        contact_data["startup_id"] = startup_id
        contact_data["startup_name"] = startup_name

        contact_data["created_at"] = datetime.now(timezone.utc)

        # Check duplicates within the same startup
        conditions = []

        if email:
            conditions.append({
                "email": email
            })

        if linkedin:
            conditions.append({
                "linkedin_url": linkedin
            })

        # Fallback: name and designation
        if not conditions:

            conditions.append({
                "name": name,
                "designation": contact.get("designation")
            })

        duplicate_filter = {
            "startup_id": startup_id,
            "$or": conditions
        }

        existing = self.contacts.find_one(duplicate_filter)

        if existing:

            print("Duplicate contact skipped:", name)

            return None

        result = self.contacts.insert_one(contact_data)

        print("Contact saved:", name)

        return result.inserted_id

    # Mark contact analysis completed
    def mark_contact_analysis_completed(self, startup_id):

        result = self.startups.update_one(
            {"_id": startup_id},
            {
                "$set": {
                    "contact_analysis": True,
                    "contact_analysis_at": datetime.now(timezone.utc)
                }
            }
        )

        return result.modified_count > 0

    # Get all startups
    def get_all_startups(self):

        return list(self.startups.find())

    # Get contacts by startup ID
    def get_contacts_by_startup_id(self, startup_id):

        return list(
            self.contacts.find({
                "startup_id": startup_id
            })
        )

    # Get startups with contacts
    def get_startups_with_contacts(self):

        startups = self.get_all_startups()

        result = []

        for startup in startups:

            contacts = self.get_contacts_by_startup_id(
                startup["_id"]
            )

            startup["_id"] = str(startup["_id"])

            for contact in contacts:

                contact["_id"] = str(contact["_id"])
                contact["startup_id"] = str(contact["startup_id"])

            startup["contacts"] = contacts

            result.append(startup)

        return result
