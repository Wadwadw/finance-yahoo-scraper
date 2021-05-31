
import scrapy
from scrapy.spiders import CSVFeedSpider

from ..extractor_data import Extractor_data
from ..items import YahooItem


class TestsSpider(CSVFeedSpider):
    name = 'data_scrape'
    allowed_domains = ['finance.yahoo.com']
    delimiter = ','
    companies = 'companies.txt'
    len_dict = 0
    custom_settings = {
        "FEED_EXPORT_FIELDS":[
            "Date",
            "Open",
            "High",
            "Low",
            "Close",
            "Adj_Close",
            "Volume",
            "three"

        ]
    }
    n = 1


    def start_requests(self):
        ex = Extractor_data()
        ex.run_extractor()
        with open(r'C:\Games\test\yahoo\yahoo\companies.txt', 'r') as files:
            for line in files:
                name_file = line.strip('\n')
                print(f'{name_file=}')
                yield scrapy.Request(url=fr'file:///C:\Games\test\yahoo\yahoo\result\{name_file}_result.csv', callback=self.parse_rows)


    def parse_row(self, response, row):
        try:
            item = YahooItem()
            item['Date'] = row['Date']
            item['Open'] = row['Open']
            item['High'] = row['High']
            item['Low'] = row['Low']
            item['Close'] = row['Close']
            item['Adj_Close'] = row['Adj Close']
            item['Volume'] = row['Volume']
            return item
        except KeyError:
            pass







