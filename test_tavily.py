from services.funding_api import FundingApiService

service = FundingApiService()

articles = service.search_funded_startups()

for article in articles:

    print("Title:", article.get("title"))

    print("URL:", article.get("url"))

    print("Content:", article.get("content"))

    print("-" * 50)