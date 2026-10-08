1. uv venv + scrapy genspider quote quotes.toscrape.com + playwright install
2. scrapy startproject quotes
3. scrapy genspider quote quotes.toscrape.com


In Scrapy Playwright, because the web page is dynamic, the browser needs time to load elements or process actions. We use async and await to tell your code: "Pause here and wait for this specific action to finish before moving to the next line." If you don't use await, your script will try to run the next command before the browser has even finished finding the input field, which leads to errors.

Here is a basic pattern for interacting with a form:

# 1. Navigate to the page
await page.goto("https://example.com/login")

# 2. Wait for the element and fill it
await page.fill("[name=\"username\"]", "test_user")

# 3. Click the submit button
await page.click("button[type=\"submit\"]")
The await keyword ensures that the script doesn't "race" ahead of the browser. 


 Scrapy Playwright, here is a summary of how those topics fit together:

Page Object & Coroutines: Playwright uses async functions (coroutines). The "Page" object is your primary tool to control the browser tab. You must await every action (like goto or fill) because these are asynchronous tasks that take time to complete.
Logging In & Dynamic Content: Websites often load content after the initial page request. You use page.fill and page.click to interact with forms. If a site has loading screens, you don't just wait for time; you wait for specific elements to appear using page.wait_for_selector().
Infinite Scroll: This is handled by executing JavaScript within the page context to scroll down, then waiting for new content to load before scraping again.
Screenshots & PDFs: These are utility methods (page.screenshot() and page.pdf()) used to capture the state of the page, which is great for debugging or archiving.


Spider Arguments in Scrapy! 

When you want to pass arguments to your spider from the command line, you use the -a flag. Here is the breakdown:

Passing the argument:
You run your spider in the terminal like this:
scrapy crawl book_spider -a category=travel

Accessing the argument in your code:
Scrapy automatically assigns these arguments as attributes to your spider instance. You can access them inside your __init__ method or anywhere else in your spider using self.category.

Example implementation:

class BookSpider(scrapy.Spider):
    name = 'book_spider'

    def __init__(self, category=None, *args, **kwargs):
        super(BookSpider, self).__init__(*args, **kwargs)
        self.start_urls = [f'http://books.toscrape.com/catalogue/category/books/{category}/index.html']