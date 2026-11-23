# from schemas.startup_schema import StartupSchema


# class StartupService:

#     def __init__(
#         self,
#         funding_api_service,
#         groq_service,
#         startup_repository
#     ):

#         self.funding_api = funding_api_service
#         self.groq = groq_service
#         self.repository = startup_repository

#     # Discover and save funded startups
#     def discover_startups(self):

#         print("Fetching funding articles...")

#         articles = self.funding_api.search_funded_startups()

#         if not articles:
#             print("No funding articles found")
#             return

#         print("Analyzing funding articles with Groq...")

#         startups = self.groq.analyze_startups(articles)

#         for startup in startups:

#             validated = StartupSchema(**startup)

#             startup_data = validated.model_dump()

#             if self.repository.startup_exists(
#                 startup_data["startup_name"]
#             ):
#                 print("Startup already exists:", startup_data["startup_name"])
#                 continue

#             self.repository.save_startup(startup_data)

#             print("Startup saved:", startup_data["startup_name"])

    
# def analyze_startup_contacts(self):

#     print("Fetching pending startups from MongoDB...")

#     # Step 1: Fetch all pending startups
#     pending_startups = self.repository.get_pending_startups()

#     print("Pending startups:", len(pending_startups))

#     if not pending_startups:
#         return

#     # Step 2: Prepare complete startup list
#     startups_data = []

#     original_ids = {}

#     for startup in pending_startups:

#         startup_id = str(startup["_id"])

#         original_ids[startup_id] = startup["_id"]

#         startups_data.append({
#             **startup,
#             "_id": startup_id
#         })

#     try:

#         # Step 3: Send ALL startups in ONE Groq API call
#         result = self.groq.analyze_employees(startups_data)

#         if not isinstance(result, dict):
#             print("Invalid Groq response")
#             return

#         startup_results = result.get("startups", [])

#         if not isinstance(startup_results, list):
#             print("Invalid startups response")
#             return

#         print("AI analyzed startups:", len(startup_results))

#         # Step 4: Save AI results into MongoDB
#         for startup_result in startup_results:

#             if not isinstance(startup_result, dict):
#                 continue

#             startup_id = startup_result.get("startup_id")

#             # Validate original startup ID
#             if startup_id not in original_ids:
#                 print("Invalid startup ID:", startup_id)
#                 continue

#             # Get original MongoDB ObjectId
#             original_id = original_ids[startup_id]

#             startup_name = startup_result.get("startup_name")

#             contacts = startup_result.get("contacts", [])

#             saved_count = 0

#             # Step 5: Save contacts
#             for contact in contacts:

#                 if not isinstance(contact, dict):
#                     continue

#                 if not contact.get("name"):
#                     continue

#                 contact_id = self.repository.save_contact(
#                     original_id,
#                     startup_name,
#                     contact
#                 )

#                 if contact_id:
#                     saved_count += 1

#             print(
#                 f"Startup: {startup_name} | "
#                 f"Contacts saved: {saved_count}"
#             )

#             # Step 6: Update analysis status
#             if startup_result.get("research_status") == "completed":

#                 self.repository.mark_contact_analysis_completed(
#                     original_id
#                 )

#                 print("Analysis completed:", startup_name)

#     except Exception as e:

#         print("Startup contact analysis error:", str(e))


#     # Main automation
#     def run_automation(self):

#         print("========== STARTLY AI STARTED ==========")

#         try:
#             self.discover_startups()
#         except Exception as e:
#             print("Startup discovery failed:", e)

#         try:
#             self.analyze_startup_contacts()
#         except Exception as e:
#             print("Employee analysis failed:", e)

#         print("========== STARTLY AI COMPLETED ==========")


# from schemas.startup_schema import StartupSchema


# class StartupService:

#     def __init__(
#         self,
#         funding_api_service,
#         groq_service,
#         startup_repository
#     ):
#         self.funding_api = funding_api_service
#         self.groq = groq_service
#         self.repository = startup_repository

#     # Discover and save funded startups
#     def discover_startups(self):

#         print("Fetching funding articles...")

#         articles = self.funding_api.search_funded_startups()

#         if not articles:
#             print("No funding articles found")
#             return

#         print("Analyzing funding articles with Groq...")

#         startups = self.groq.analyze_startups(articles)

#         for startup in startups:

#             validated = StartupSchema(**startup)
#             startup_data = validated.model_dump()

#             if self.repository.startup_exists(
#                 startup_data["startup_name"]
#             ):
#                 print("Startup already exists:", startup_data["startup_name"])
#                 continue

#             self.repository.save_startup(startup_data)

#             print("Startup saved:", startup_data["startup_name"])

#     # Analyze startup contacts
#     def analyze_startup_contacts(self):

#         print("Fetching pending startups from MongoDB...")

#         pending_startups = self.repository.get_pending_startups()

#         print("Pending startups:", len(pending_startups))

#         if not pending_startups:
#             return

#         startups_data = []
#         original_ids = {}

#         for startup in pending_startups:

#             startup_id = str(startup["_id"])

#             original_ids[startup_id] = startup["_id"]

#             startups_data.append({
#                 **startup,
#                 "_id": startup_id
#             })

#         try:

#             # Send all startups in one Groq API call
#             result = self.groq.analyze_employees(startups_data)

#             if not isinstance(result, dict):
#                 print("Invalid Groq response")
#                 return

#             startup_results = result.get("startups", [])

#             if not isinstance(startup_results, list):
#                 print("Invalid startups response")
#                 return

#             print("AI analyzed startups:", len(startup_results))

#             print("This is Startup data",result)

#             for startup_result in startup_results:

#                 if not isinstance(startup_result, dict):
#                     continue

#                 startup_id = startup_result.get("startup_id")

#                 if startup_id not in original_ids:
#                     print("Invalid startup ID:", startup_id)
#                     continue

#                 original_id = original_ids[startup_id]

#                 startup_name = startup_result.get("startup_name")

#                 contacts = startup_result.get("contacts", [])

#                 if not isinstance(contacts, list):
#                     continue

#                 saved_count = 0

#                 for contact in contacts:

#                     if not isinstance(contact, dict):
#                         continue

#                     if not contact.get("name"):
#                         continue

#                     contact_id = self.repository.save_contact(
#                         original_id,
#                         startup_name,
#                         contact
#                     )

#                     if contact_id:
#                         saved_count += 1

#                 print(
#                     f"Startup: {startup_name} | "
#                     f"Contacts saved: {saved_count}"
#                 )

#                 if startup_result.get("research_status") == "completed":

#                     self.repository.mark_contact_analysis_completed(
#                         original_id
#                     )

#                     print("Analysis completed:", startup_name)

#         except Exception as e:

#             print("Startup contact analysis error:", str(e))

#     # Main automation
#     def run_automation(self):

#         print("========== STARTLY AI STARTED ==========")

#         try:
#             self.discover_startups()
#         except Exception as e:
#             print("Startup discovery failed:", e)

#         try:
#             self.analyze_startup_contacts()
#         except Exception as e:
#             print("Employee analysis failed:", e)

#         print("========== STARTLY AI COMPLETED ==========")


# from schemas.startup_schema import StartupSchema


# class StartupService:

#     def __init__(
#         self,
#         funding_api_service,
#         groq_service,
#         startup_repository
#     ):
#         self.funding_api = funding_api_service
#         self.groq = groq_service
#         self.repository = startup_repository

#     # Discover and save funded startups
#     def discover_startups(self):

#         print("Fetching funding articles...")

#         articles = self.funding_api.search_funded_startups()

#         if not articles:
#             print("No funding articles found")
#             return

#         print("Analyzing funding articles with Groq...")

#         startups = self.groq.analyze_startups(articles)

#         for startup in startups:

#             validated = StartupSchema(**startup)
#             startup_data = validated.model_dump()

#             if self.repository.startup_exists(
#                 startup_data["startup_name"]
#             ):
#                 print(
#                     "Startup already exists:",
#                     startup_data["startup_name"]
#                 )
#                 continue

#             self.repository.save_startup(startup_data)

#             print("Startup saved:", startup_data["startup_name"])

#     # Analyze startup contacts
#     import json


# class StartupService:

#     def __init__(self, groq_service, startup_repository):

#         self.groq_service = groq_service
#         self.repository = startup_repository

#     # Analyze startup contacts
#     async def analyze_startup_contacts(self):

#         print("Fetching pending startups from MongoDB...")

#         pending_startups = self.repository.get_pending_startups()

#         print("Pending startups:", len(pending_startups))

#         if not pending_startups:
#             return

#         analyzed_startups = []

#         for startup in pending_startups:

#             original_id = startup["_id"]
#             startup_id = str(original_id)

#             startup_data = dict(startup)
#             startup_data["_id"] = startup_id

#             try:

#                 print("Analyzing startup:", startup.get("startup_name"))

#                 # AI analyzes one startup at a time
#                 result = await self.groq_service.analyze_employees(
#                     startup_data
#                 )

#                 if isinstance(result, str):
#                     result = json.loads(result)

#                 if not isinstance(result, dict):
#                     print("Invalid AI response")
#                     continue

#                 startup_results = result.get("startup_contacts", [])

#                 if not isinstance(startup_results, list):
#                     print("Invalid startup contacts response")
#                     continue

#                 if not startup_results:
#                     print("No startup contacts returned")
#                     continue

#                 contact_data = startup_results[0]

#                 contacts = contact_data.get("contacts", [])

#                 if not isinstance(contacts, list):
#                     print("Invalid contacts:", startup.get("startup_name"))
#                     continue

#                 startup_name = startup.get("startup_name")

#                 saved_count = 0

#                 # Save every valid contact
#                 for contact in contacts:

#                     if not isinstance(contact, dict):
#                         continue

#                     if not contact.get("name"):
#                         continue

#                     contact_id = self.repository.save_contact(
#                         original_id,
#                         startup_name,
#                         contact
#                     )

#                     if contact_id:
#                         saved_count += 1

#                 print(
#                     f"Startup: {startup_name} | "
#                     f"Contacts received: {len(contacts)} | "
#                     f"Contacts saved: {saved_count}"
#                 )

#                 # Mark completed only when contacts are saved
#                 if saved_count > 0:

#                     self.repository.mark_contact_analysis_completed(
#                         original_id
#                     )

#                     analyzed_startups.append({
#                         **startup_data,
#                         "company_email_domain": contact_data.get(
#                             "company_email_domain"
#                         ),
#                         "contacts": contacts,
#                         "research_status": contact_data.get(
#                             "research_status"
#                         ),
#                         "contacts_analyzed": True
#                     })

#                     print("Contact analysis completed:", startup_name)

#                 else:

#                     print(
#                         "No contacts saved. Startup remains pending:",
#                         startup_name
#                     )

#             except Exception as e:

#                 print(
#                     f"Startup contact analysis error "
#                     f"({startup.get('startup_name')}): {str(e)}"
#                 )

#         return analyzed_startups

#     # Main automation
#     def run_automation(self):

#         print("========== STARTLY AI STARTED ==========")

#         try:
#             self.discover_startups()

#         except Exception as e:
#             print("Startup discovery failed:", str(e))

#         try:
#             self.analyze_startup_contacts()

#         except Exception as e:
#             print("Employee analysis failed:", str(e))

#         print("========== STARTLY AI COMPLETED ==========")






import json

from schemas.startup_schema import StartupSchema


class StartupService:

    def __init__(
        self,
        funding_api_service,
        groq_service,
        startup_repository
    ):
        self.funding_api = funding_api_service
        self.groq_service = groq_service
        self.repository = startup_repository

    # =====================================
    # 1. DISCOVER STARTUPS
    # =====================================

    def discover_startups(self):

        print("Fetching funding articles...")

        articles = self.funding_api.search_funded_startups()

        if not articles:
            print("No funding articles found")
            return

        startups = self.groq_service.analyze_startups(articles)

        if not startups:
            print("No startups extracted")
            return

        for startup in startups:

            try:
                validated = StartupSchema(**startup)
                startup_data = validated.model_dump()

                startup_name = startup_data["startup_name"]

                if self.repository.startup_exists(startup_name):
                    print("Startup already exists:", startup_name)
                    continue

                self.repository.save_startup(startup_data)

                print("Startup saved:", startup_name)

            except Exception as e:
                print("Startup saving error:", str(e))

    # =====================================
    # 2. ANALYZE STARTUP CONTACTS
    # =====================================

    async def analyze_startup_contacts(self):

        print("Fetching pending startups...")

        pending_startups = self.repository.get_pending_startups()

        print("Pending startups:", len(pending_startups))

        analyzed_startups = []

        for startup in pending_startups:

            original_id = startup["_id"]
            startup_id = str(original_id)

            startup_name = startup.get("startup_name")

            startup_data = dict(startup)
            startup_data["_id"] = startup_id

            try:

                print("\nAnalyzing startup:", startup_name)

                # STEP 1: Check saved search results

                if startup.get("search_completed"):

                    search_data = startup.get("search_data", [])

                    print("Using saved Tavily results:", startup_name)

                else:

                    # STEP 2: Search employees using Tavily

                    query = f"""
                    "{startup_name}" founder CTO employees
                    HR manager talent acquisition recruiter
                    engineering manager hiring manager
                    LinkedIn employee profiles
                    """

                    search_data = self.funding_api.search_employees(query)

                    if not search_data:

                        print("No search results:", startup_name)
                        continue

                    # STEP 3: Save Tavily results

                    self.repository.save_search_data(
                        original_id,
                        search_data
                    )

                    print("Tavily results saved:", startup_name)

                # STEP 4: Send startup AND search data to Groq
                                           
                result = self.groq_service.analyze_employees(
                    startup_data,
                    search_data
                )

                if isinstance(result, str):
                    result = json.loads(result)

                if not isinstance(result, dict):
                    print("Invalid Groq response:", startup_name)
                    continue

                # STEP 5: Get startup result

                startup_results = result.get("startups", [])

                contact_data = next(
                    (
                        item for item in startup_results
                        if isinstance(item, dict)
                        and str(item.get("startup_id")) == startup_id
                    ),
                    None
                )

                if not contact_data:

                    print("Startup ID mismatch:", startup_name)
                    continue

                # STEP 6: Extract contacts

                contacts = contact_data.get("contacts", [])

                if not isinstance(contacts, list) or not contacts:

                    print("No reliable contacts found:", startup_name)
                    print(
                        "Website:",
                        contact_data.get("company_website")
                    )
                    print(
                        "Email domain:",
                        contact_data.get("company_email_domain")
                    )

                    # Do not mark completed without saved contacts.
                    continue

                # STEP 7: Save contacts

                saved_count = 0

                for contact in contacts:

                    if not isinstance(contact, dict):
                        continue

                    if not contact.get("name"):
                        continue

                    if not contact.get("source_url"):
                        continue

                    contact_id = self.repository.save_contact(
                        original_id,
                        startup_name,
                        contact
                    )

                    if contact_id:
                        saved_count += 1

                print(
                    f"{startup_name} | "
                    f"Received: {len(contacts)} | "
                    f"Saved: {saved_count}"
                )

                # STEP 8: Mark completed only after successful saving

                if saved_count > 0:

                    self.repository.mark_contact_analysis_completed(
                        original_id
                    )

                    analyzed_startups.append({
                        **startup_data,
                        "contacts": contacts,
                        "contacts_analyzed": True
                    })

                else:

                    print(
                        "No contacts successfully saved:",
                        startup_name
                    )

            except Exception as e:

                print(
                    f"Error processing {startup_name}: {str(e)}"
                )

        return analyzed_startups

    # =====================================
    # 3. MAIN AUTOMATION
    # =====================================

    async def run_automation(self):

        print("========== STARTLY AI STARTED ==========")

        try:
            self.discover_startups()

        except Exception as e:
            print("Discovery error:", str(e))

        try:
            await self.analyze_startup_contacts()

        except Exception as e:
            print("Analysis error:", str(e))

        print("========== STARTLY AI COMPLETED ==========")


    # Get startups with contacts
    def get_startups_with_contacts(self):

      return self.repository.get_startups_with_contacts()