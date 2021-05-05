import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from scrapy.selector import Selector
import scrapy


class NewsScrapeSpider(scrapy.Spider):
    name = 'news_scrape'
    allowed_domains = ['www.finance.yahoo.com']
    # start_urls = ['https://finance.yahoo.com/quote/ZUO/news?p=ZUO']
    # def __init__(self):
    #     driver = webdriver.Chrome(ChromeDriverManager().install())
    #     with open(r'C:\Games\test\yahoo\yahoo\companies.txt', 'r') as file:
    #         for line in file:
    #             self.company_name = line.strip('\n')
    #             driver.get(f'https://finance.yahoo.com/quote/{self.company_name}/news?p={self.company_name}')
    #             self.html = driver.page_source

    def start_requests(self):
        with open(r'C:\Games\test\yahoo\yahoo\companies.txt', 'r') as file:
            for line in file:
                company_name = line.strip('\n')
                yield scrapy.Request(url=f'https://finance.yahoo.com/quote/{company_name}/news?p={company_name}', callback=self.parse, meta={"company_name": company_name})

    def parse(self, response):

        for news in response.xpath("//div[@class='Cf']/div/h3"):
            # import pdb; pdb.set_trace()
            yield {
                'company': response.meta.get("company_name"),
                'title': news.xpath(".//a[contains(@class, 'js-content-viewer')]/text()").get(),
                'link': 'https://www.finance.yahoo.com'+news.xpath(".//a[contains(@class, 'js-content-viewer')]/@href").get(),
            }

