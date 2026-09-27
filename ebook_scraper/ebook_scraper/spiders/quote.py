import json
import scrapy


#proxy: 192.42.116.117 fakeip
class QuoteSpider(scrapy.Spider):
    name =  'quote'
    start_urls = ['https://quotes.toscrape.com/api/quotes?page=1' ]

    def parse(self, response):
        dt = json. loads( response.body )

        yield dt

        if dt['has_next']:
            yield scrapy. Request(
                f"https://quotes. toscrape.com/api/quotes?page={dt[ 'page' ]+1}"

            )