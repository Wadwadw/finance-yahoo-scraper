# Yahoo finance scraper
Test assessment by Introlab. Scraper uses Selenium with Chrome Driver so you should have Google Chrome browser installed.
## Running all the stuff
1. Clone repo: `git clone https://github.com/Wadwadw/finance-yahoo-scraper.git`
2. Create virtualenv, for example: `python3 -m venv venv` or `virtualenv -p python3 venv`
3. Activate it source `venv/bin/activate`
4. Install all the packages `pip install -r requirements.txt`
5. Enter the companies you need into the companies.txt (start each company on a new line)
6. Start scraper script `scrapy crawl data_scrape` if you want scrape news `scrapy crawl news_scrape -o news.csv`
