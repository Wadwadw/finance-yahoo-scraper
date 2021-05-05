# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3 as sq
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SQLitePipeline(object):
    collection_name = 'news'

    def open_spider(self, spider):
        self.connection = sq.connect('yahoo.db')
        self.c = self.connection.cursor()

        try:
            self.c.execute('''
                CREATE TABLE news(
                    company TEXT,
                    title TEXT,
                    link TEXT
                    
                )
            ''')
        except sq.OperationalError:
            pass

        self.connection.commit()

    def close_spider(self, spider):

        self.connection.close()

    def process_item(self, item, spider):
        self.c.execute('''
            INSERT INTO news (company,title,link) VALUES(?,?,?)
        
        ''', (
            item.get('company'),
            item.get('title'),
            item.get('link'),



        ))
        self.connection.commit()