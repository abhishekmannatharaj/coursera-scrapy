# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy
from itemloaders.processors import MapCompose, TakeFirst, Join


def get_price(txt):
    return float(txt.replace("£", "").strip())

def convert_to_rupees(price):
    return price * 100  # Assuming 1 GBP = 100 INR for demonstration purposes

def get_quantity(txt):
    return int(
        txt.replace('(','').split()[0]
    )


class EbookScraperItem(scrapy.Item):

    title: str = scrapy.Field(output_processor=TakeFirst())
    price: float = scrapy.Field(
        input_processor=MapCompose(get_price, convert_to_rupees),
        output_processor=TakeFirst()
    )
    availability: str = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
    quantity: str = scrapy.Field(
        input_processor=MapCompose(get_quantity),
        output_processor=TakeFirst()
    )