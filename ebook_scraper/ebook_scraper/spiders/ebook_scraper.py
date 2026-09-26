import scrapy

from scrapy.loader import ItemLoader

from ebook_scraper.items import EbookScraperItem


class EbookScraperSpider(scrapy.Spider):
    name = "ebook"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/catalogue/category/books/mystery_3/page-2.html"]
    cols = ["title", "price", "availability"]

    def parse(self, response):
        self.logger.info("Parsing the response from the start URL")

        books = response.css("article.product_pod")

        for book in books:
            loader = ItemLoader(item=EbookScraperItem(), selector=book)
            loader.add_css('title', 'h3 a::attr(title)')
            loader.add_css('price', 'p.price_color::text')
            loader.add_css('availability', 'p.instock.availability::text')

            yield loader.load_item()