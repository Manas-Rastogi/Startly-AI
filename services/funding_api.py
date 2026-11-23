# import os

# from dotenv import load_dotenv
# from tavily import TavilyClient


# load_dotenv()


# class FundingApiService:

#     def __init__(self):

#         api_key = os.getenv("TAVILY_API_KEY")

#         self.client = TavilyClient(
#             api_key=api_key
#         )

#     def search_funded_startups(self):

#         queries = [
#             "Recently funded Indian technology startups SaaS AI fintech deeptech funding announcements"
#         ]

#         all_results = []

#         for query in queries:

#             print("Searching:", query)

#             response = self.client.search(
#                 query=query,
#                 topic="news",
#                 max_results=10
#             )

#             results = response.get("results", [])

#             all_results.extend(results)

#         return all_results


import os

from tavily import TavilyClient


class FundingApiService:

    def __init__(self):

        api_key = os.getenv("TAVILY_API_KEY")

        if not api_key:
            raise ValueError("TAVILY_API_KEY is missing")

        self.client = TavilyClient(
            api_key=api_key
        )

    # =====================================
    # 1. SEARCH FUNDED STARTUPS
    # =====================================

    def search_funded_startups(self):

        queries = [
            "Recently funded Indian technology startups SaaS AI fintech deeptech funding announcements"
        ]

        all_results = []

        for query in queries:

            print("Searching funding news:", query)

            try:

                response = self.client.search(
                    query=query,
                    topic="news",
                    max_results=10
                )

                results = response.get("results", [])

                all_results.extend(results)

            except Exception as e:

                print("Funding search error:", str(e))

        return all_results

    # =====================================
    # 2. SEARCH STARTUP EMPLOYEES
    # =====================================

    def search_employees(self, query):

        print("Searching startup employees:", query)

        try:

            response = self.client.search(
                query=query,
                topic="general",
                search_depth="advanced",
                max_results=10
            )

            results = response.get("results", [])

            print("Employee search results:", len(results))

            return results

        except Exception as e:

            print("Employee search error:", str(e))

            return []
