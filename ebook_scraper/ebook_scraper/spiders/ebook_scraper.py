import scrapy


class EbookScraperSpider(scrapy.Spider):
    name = "ebook_scraper"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        print("=====================================================[Parsing the response from the start URL...]=================================================================")

        ebooks = response.css("article")

        for ebook in ebooks:
            title = ebook.css("h3 a::attr(title)").get()
            price = ebook.css(".price_color::text").get()
            availability = ebook.css(".availability::text").get().strip()

            yield {
                "title": title,
                "price": price,
                "availability": availability,
            }

