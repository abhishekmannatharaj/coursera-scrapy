import scrapy
from scrapy.loader import ItemLoader

from ebook_scraper.items import EbookScraperItem


class EbookScraperSpider(scrapy.Spider):
    name = "ebook"
    # allowed_domains = ["books.toscrape.com"]
    # start_urls = ["https://books.toscrape.com/catalogue/category/books/travel_2/index.html"]
    # cols = ["title", "price", "availability"]

    def start_requests(self):
        yield scrapy. FormRequest(
            "http://www.scrapethissite.com/pages/advanced/?gotcha=login",
            formdata={
                        "user": "kyle",
                        "pass": "really_strong"
                    }
            )

    def parse(self, response):
        print(
            "[ Result ]:",
            response. css("div.container div div: :text" ).get()
        )

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.page_count = 0
    #     self.total_pages = 4

    # def start_requests(self):
    #     base_url = self.start_urls[0]
    #     for page in range(1, self.total_pages + 1):
    #         if page == 1:
    #             url = base_url
    #         else:
    #             url = base_url.rsplit("/index.html", 1)[0] + f"/page-{page}.html"
    #         yield scrapy.Request(url=url, callback=self.parse)

    # def parse(self, response):
    #     self.logger.info("Parsing page: %s", response.url)
    #     books = response.css("article.product_pod")

    #     for book in books:
    #         loader = ItemLoader(item=EbookScraperItem(), selector=book)
    #         loader.add_css("title", "h3 a::attr(title)")
    #         loader.add_css("price", "p.price_color::text")
    #         loader.add_css("availability", "p.instock.availability::text")
    #         yield loader.load_item()