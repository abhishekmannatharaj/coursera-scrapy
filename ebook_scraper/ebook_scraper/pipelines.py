# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os

from dotenv import load_dotenv
from itemadapter import ItemAdapter
from openpyxl import Workbook
from pymongo import MongoClient

load_dotenv()


class EbookScraperPipeline:
    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        pipeline.spider = crawler.spider
        return pipeline

    def open_spider(self, spider):
        self.spider = spider
        self.workbook = Workbook()
        self.sheet = self.workbook.active
        self.sheet.title = "Ebooks Travel"
        self.sheet.append(getattr(spider, "cols", ["title", "price", "availability"]))

        mongo_uri = os.getenv("MONGODB_URI")
        if mongo_uri:
            self.client = MongoClient(mongo_uri, connect=False)
            self.collection = self.client.get_database("ebook").get_collection("travel")
        else:
            self.client = None
            self.collection = None

    def process_item(self, item, spider):
        self.sheet.append([item['title'], item['price'], item['availability']])

        if self.collection is not None:
            self.collection.insert_one(ItemAdapter(item).asdict())
        return item

    def close_spider(self, spider):
        try:
            self.workbook.save("ebooks_travel.xlsx")
        except PermissionError:
            spider.logger.warning("Could not save Excel file because it is open in Excel. Close the workbook and try again.")
        if self.client is not None:
            self.client.close()