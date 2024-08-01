# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class ScrapPipeline:
    def __init__(self) -> None:
        self.connection()
        self.tab()
    def connection(self):
        self.connection=sqlite3.connect("database.db")
        self.curr=self.connection.cursor()
    def tab(self):
         self.curr.execute("""DROP TABLE IF EXISTS data""")
         self.curr.execute("""create table data(
             title text,
             price INT)""")
          
    def process_item(self, item, spider):
        self.put(item)
        return item
    def put(self,item):
        self.curr.execute("""insert into data values(?,?)""",(
            item["title"],
            item["price"]
        ))
        self.connection.commit()
       