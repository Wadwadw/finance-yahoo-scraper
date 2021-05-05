
import scrapy
import pandas as pd
from scrapy.spiders import CSVFeedSpider

from ..extractor_data import Extractor_data
from ..items import YahooItem
from ..test import get_url_download, reverse_csv, three_days_before_change






class TestsSpider(CSVFeedSpider):
    name = 'data_scrape'
    allowed_domains = ['finance.yahoo.com']
    # start_urls = ['https://query1.finance.yahoo.com/v7/finance/download/PD?period1=1554940800&period2=1620000000&interval=1d&events=history&includeAdjustedClose=true']
    delimiter = ','
    # headers = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
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
        # time.sleep(1)
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


        # return item

        # fields = ['date', 'open', 'high', 'low', 'close', 'adj close', 'volume']
        # with open('PD.csv', 'a+') as f:
        #     f.write('{}\n'.format('\t'.join(str(field) for field in fields)))
        #     for item in row:
        #         f.write("{}\n".format('\t'.join(str(item[field] for field in fields))))

    # def parse_row(self, response, row):
        # for url in get_url_download():
        #     print(url
        # print(get_url_download())





