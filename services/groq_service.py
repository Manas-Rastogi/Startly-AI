
# import os
# import json

# from dotenv import load_dotenv
# from groq import Groq

# load_dotenv()


# class GroqService:

#     def __init__(self):
#         api_key = os.getenv("GROQ_API_KEY")

#         if not api_key:
#             raise ValueError("GROQ_API_KEY is missing from .env")

#         self.client = Groq(api_key=api_key)
#         self.model = "openai/gpt-oss-120b"

#     # Common JSON generation method
#     def generate_json(self, prompt):

#         response = self.client.chat.completions.create(
#             model=self.model,
#             messages=[
#                 {
#                     "role": "system",
#                     "content": """
#                     You are an expert startup research analyst.
#                     Return only valid JSON.
#                     Never invent facts or fabricate sources.
#                     """
#                 },
#                 {
#                     "role": "user",
#                     "content": prompt
#                 }
#             ],
#             temperature=0.1,
#             response_format={"type": "json_object"}
#         )

#         content = response.choices[0].message.content

#         if not content:
#             raise ValueError("Groq returned an empty response")

#         try:
#             return json.loads(content)
#         except json.JSONDecodeError as e:
#             raise ValueError(f"Groq returned invalid JSON: {e}")

#     # Analyze funding articles
#     def analyze_startups(self, articles):

#         prompt = f"""
#         Analyze these startup funding news results.

#         Extract only companies that have actually received funding.

#         Return JSON in this exact structure:

#         {{
#             "startups": [
#                 {{
#                     "startup_name": "",
#                     "category": "",
#                     "city": "",
#                     "country": "",
#                     "funding_amount": "",
#                     "funding_stage": "",
#                     "funding_date": "",
#                     "website": "",
#                     "description": "",
#                     "source_url": ""
#                 }}
#             ]
#         }}

#         RULES:

#         1. Extract only funded startups.
#         2. Do not include investors or funding firms.
#         3. Do not invent company details.
#         4. Use null when information is unavailable.
#         5. Avoid duplicate startups.
#         6. Use exact source URLs from input.
#         7. Keep only actual funding announcements.

#         FUNDING SEARCH RESULTS:

#         {json.dumps(articles, default=str)}
#         """

#         result = self.generate_json(prompt)

#         return result.get("startups", [])

#     # Analyze employees startup-wise
    
# def analyze_employees(self, startups):

#     prompt = f"""
#     You are a professional Startup Employee Intelligence
#     and Technical Hiring Contact Research Analyst.

#     TASK:
#     Analyze ALL supplied startups and identify employees
#     who can influence technical hiring.

#     STARTUPS DATA:
#     {json.dumps(startups, default=str, ensure_ascii=False)}

#     STRICT RULES:

#     1. Analyze every startup independently.
#     2. Return every startup in the response.
#     3. Preserve each startup's exact MongoDB ID.
#     4. Never modify, generate or replace startup IDs.
#     5. Never mix contacts between startups.
#     6. Never invent employee names or designations.
#     7. Prioritize current employees.
#     8. Extract LinkedIn URLs only from supplied evidence.
#     9. Never construct LinkedIn URLs.
#     10. Extract public emails only when explicitly supported.
#     11. Do not confuse investors with employees.
#     12. Remove duplicate contacts.
#     13. Every contact must have an exact source URL.
#     14. Return empty contacts if no reliable contacts exist.
#     15. Return null for unavailable information.

#     TARGET CONTACTS:

#     TECHNICAL LEADERSHIP:
#     - CTO
#     - Technical Co-Founder
#     - Co-Founder
#     - VP Engineering
#     - Head of Engineering
#     - Engineering Manager
#     - Technical Lead

#     HUMAN RESOURCES:
#     - HR Head
#     - HR Manager
#     - Head of People
#     - HR Business Partner
#     - People Operations Manager

#     TALENT ACQUISITION:
#     - Talent Acquisition Head
#     - Talent Acquisition Manager
#     - Technical Recruiter
#     - IT Recruiter
#     - Senior Recruiter
#     - Hiring Manager
#     - Recruitment Manager

#     OTHER:
#     - Employees announcing technical jobs
#     - Internship recruitment employees
#     - Technical referral contacts

#     EMPLOYMENT STATUS:
#     - current
#     - former
#     - unclear

#     CONTACT PRIORITY:

#     HIGH:
#     CTO, Founder, Head of Engineering, HR Head,
#     Talent Acquisition Head, Hiring Manager.

#     MEDIUM:
#     Engineering Manager, HR Manager, Technical Recruiter.

#     LOW:
#     Other relevant employees.

#     EVIDENCE:
#     Explain identity, designation, startup connection
#     and employment status for every contact.

#     OUTPUT:
#     Return ONLY valid JSON in this exact structure:

#     {{
#         "startups": [
#             {{
#                 "startup_id": "EXACT_ORIGINAL_MONGODB_ID",
#                 "startup_name": "",
#                 "company_website": null,
#                 "company_email_domain": null,
#                 "contacts": [
#                     {{
#                         "name": "",
#                         "designation": "",
#                         "department": "",
#                         "contact_category": "",
#                         "contact_priority": "",
#                         "employment_status": "unclear",
#                         "linkedin_profile_url": null,
#                         "public_email": null,
#                         "generated_email_candidates": [],
#                         "source_url": "",
#                         "evidence": "",
#                         "hiring_relevance": ""
#                     }}
#                 ],
#                 "research_status": "completed"
#             }}
#         ]
#     }}

#     IMPORTANT:
#     - Include ALL supplied startups.
#     - Return the original startup_id exactly.
#     - Do not skip startups with zero contacts.
#     - Never invent information.
#     - If data is insufficient use insufficient_data.
#     - Return valid JSON only.
#     """

#     result = self.generate_json(prompt)

#     return result





import os
import json

from dotenv import load_dotenv
from groq import Groq

load_dotenv()


class GroqService:

    def __init__(self):

        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError("GROQ_API_KEY is missing from .env")

        self.client = Groq(api_key=api_key)
        self.model = "openai/gpt-oss-120b"

    # Common JSON generation method
    def generate_json(self, prompt):

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": """
                    You are an expert startup research analyst.
                    Return only valid JSON.
                    Never invent facts or fabricate sources.
                    """
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.1,
            response_format={"type": "json_object"}
        )

        content = response.choices[0].message.content

        if not content:
            raise ValueError("Groq returned an empty response")

        try:
            return json.loads(content)

        except json.JSONDecodeError as e:
            raise ValueError(f"Groq returned invalid JSON: {e}")

    # Analyze funding articles
    def analyze_startups(self, articles):

        prompt = f"""
        Analyze these startup funding news results.

        Extract only companies that have actually received funding.

        Return JSON in this exact structure:

        {{
            "startups": [
                {{
                    "startup_name": "",
                    "category": "",
                    "city": "",
                    "country": "",
                    "funding_amount": null,
                    "funding_stage": null,
                    "funding_date": null,
                    "website": null,
                    "description": "",
                    "source_url": ""
                }}
            ]
        }}

        RULES:

        1. Extract only funded startups.
        2. Do not include investors or funding firms.
        3. Do not invent company details.
        4. Use null when information is unavailable.
        5. Avoid duplicate startups.
        6. Use exact source URLs from input.
        7. Keep only actual funding announcements.

        FUNDING SEARCH RESULTS:

        {json.dumps(articles, default=str, ensure_ascii=False)}
        """

        result = self.generate_json(prompt)

        return result.get("startups", [])

    # Analyze employees for one startup using Tavily results
    def analyze_employees(self, startup_data, search_data):

        startup_id = str(startup_data.get("_id", ""))
        startup_name = startup_data.get("startup_name", "")

        # Limit Tavily search results
        limited_results = []

        for item in search_data[:5]:

            limited_results.append({
                "title": item.get("title"),
                "url": item.get("url"),
                "content": (item.get("content") or "")[:500]
            })

        # Send only required startup information
        limited_startup = {
            "_id": startup_id,
            "startup_name": startup_name,
            "website": startup_data.get("website"),
            "city": startup_data.get("city"),
            "country": startup_data.get("country"),
            "category": startup_data.get("category")
        }

        prompt = f"""
        You are a startup employee research analyst.

        STARTUP INFORMATION:
        {json.dumps(limited_startup, ensure_ascii=False)}

        TAVILY SEARCH RESULTS:
        {json.dumps(limited_results, ensure_ascii=False)}

        ORIGINAL STARTUP ID:
        {startup_id}

        TASK:
        Identify employees who can influence technical hiring.

        TARGET CONTACTS:
        CTO, Founder, Co-Founder, VP Engineering,
        Head of Engineering, Engineering Manager,
        HR Head, HR Manager, Talent Acquisition Manager,
        Technical Recruiter, Hiring Manager.

        STRICT RULES:

        1. Analyze only the given startup.
        2. Never invent employee names or designations.
        3. Use only supplied search evidence.
        4. Never construct LinkedIn URLs.
        5. Use exact source URLs from search results.
        6. Do not include investors.
        7. Remove duplicate contacts.
        8. Use current, former or unclear employment status.
        9. Return empty contacts if no reliable contacts exist.
        10. Preserve the exact startup ID.
        11. Return exactly one startup.

        OUTPUT JSON:

        {{
            "startups": [
                {{
                    "startup_id": "{startup_id}",
                    "startup_name": "{startup_name}",
                    "company_website": null,
                    "company_email_domain": null,
                    "contacts": [
                        {{
                            "name": "",
                            "designation": "",
                            "department": "",
                            "contact_category": "",
                            "contact_priority": "",
                            "employment_status": "unclear",
                            "linkedin_profile_url": null,
                            "public_email": null,
                            "generated_email_candidates": [],
                            "source_url": "",
                            "evidence": "",
                            "hiring_relevance": ""
                        }}
                    ],
                    "research_status": "completed"
                }}
            ]
        }}

        Return valid JSON only.
        """

        result = self.generate_json(prompt)

        return result
