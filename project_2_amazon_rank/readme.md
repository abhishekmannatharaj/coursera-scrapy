# have to study on playwright to bypass Amazon
scrapy shell -s USER_AGENT="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" "https://www.amazon.com/s?k=python+3.10"


# 🚀 Alternative Approach:

If You Still Get BlockedIf Amazon's edge network continues to block your requests despite using clean 
headers, they are triggering the Javascript validation challenge we observed earlier.The most efficient alternative inside a local development project is installing the standard requests wrapper tool along with an entry-level unblocking proxy string. For instance, you can sign up for a free tier account at a proxy service like ScrapeOps or ScraperAPI and structure your target endpoint URL like this inside your script:

PROXY_API_KEY = "YOUR_FREE_API_KEY"
'''Instead of hitting Amazon directly, route the query securely through the proxy node'''
start_urls = [f"https://proxy-service.com{PROXY_API_KEY}&url=https://www.amazon.com/s?k=python+for+beginners"]


