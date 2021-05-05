# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class YahooItem(scrapy.Item):
    Date = Field()
    Open = Field()
    High = Field()
    Low = Field()
    Close = Field()
    Adj_Close = Field()
    Volume = Field()
    n = Field()
    three = Field()

