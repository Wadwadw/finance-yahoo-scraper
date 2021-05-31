import scrapy


class NewsScrapeSpider(scrapy.Spider):
    name = 'news_scrape'
    allowed_domains = ['www.finance.yahoo.com']

    def start_requests(self):
        with open(r'C:\Games\test\yahoo\yahoo\companies.txt', 'r') as file:
            for line in file:
                company_name = line.strip('\n')
                yield scrapy.Request(url=f'https://finance.yahoo.com/quote/{company_name}/news?p={company_name}', callback=self.parse, meta={"company_name": company_name})

    def parse(self, response):

        for news in response.xpath("//div[@class='Cf']/div/h3"):
            yield {
                'company': response.meta.get("company_name"),
                'title': news.xpath(".//a[contains(@class, 'js-content-viewer')]/text()").get(),
                'link': 'https://www.finance.yahoo.com'+news.xpath(".//a[contains(@class, 'js-content-viewer')]/@href").get(),
            }

