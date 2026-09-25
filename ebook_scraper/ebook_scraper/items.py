# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy
from itemloaders.processors import MapCompose, TakeFirst


def get_price(txt):
    return float(txt.replace("£", "").strip())


class EbookScraperItem(scrapy.Item):

    title: str = scrapy.Field(output_processor=TakeFirst())
    price: float = scrapy.Field(
        input_processor=MapCompose(get_price),
        output_processor=TakeFirst()
    )
    availability: str = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )