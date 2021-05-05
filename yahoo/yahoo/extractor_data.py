import os
import time
import logging
import sqlite3 as sq
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait


logger = logging.getLogger("selenium.webdriver.remote.remote_connection")

logger.setLevel(logging.WARNING)

import requests
import pandas as pd
options = webdriver.ChromeOptions()
options.add_argument('headless')
class Extractor_data():
    def __init__(self):
        self.companies = r'C:\Games\test\yahoo\yahoo\companies.txt'


    def run_extractor(self):
        with open(f'{self.companies}', 'r') as file:
            driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
            for line in file:
                try:
                    name_company = line.strip('\n')
                    driver.get(f"https://finance.yahoo.com/quote/{name_company}/history?p={name_company}")
                    range_range = WebDriverWait(driver, 3).until(
                        lambda d: d.find_element_by_xpath("//div[contains(@class, 'dateRangeBtn')]/div"))
                    range_range.click()
                    time.sleep(1)
                    max_date = WebDriverWait(driver, 3).until(lambda d: d.find_element_by_xpath("//button[@data-value='MAX']"))
                    max_date.click()
                    time.sleep(0.5)
                    download = driver.find_element_by_xpath("((//section[@data-test='qsp-historical']/div/div)[2]/span)[2]/a")

                    f = open(fr'C:/Games/test/yahoo/yahoo/{name_company}.csv', 'wb')

                    url = requests.get(download.get_attribute('href'))
                    f.write(url.content)
                    f.close()

                except TimeoutException:
                    pass

            driver.close()
            self.reverse_csv()
            with open('companies.txt', 'r') as f:
                for line in f:
                    name_company = line.strip('\n')
                    self.three_days_before_change(name_company=name_company)
            self.delete_files()



    def reverse_csv(self):
        with open('companies.txt', 'r') as file:
            for line in file:
                name = line.strip('\n')
                df = pd.read_csv(fr'C:\Games\test\yahoo\yahoo\{name}.csv', header=0)
                data = df.iloc[::-1]
                data.to_csv(fr'C:\Games\test\yahoo\yahoo\reversed_files\{name}_reversed.csv', index=False)


    def three_days_before_change(self, name_company):
        n = 0
        df = pd.read_csv(fr'C:\Games\test\yahoo\yahoo\{name_company}_reversed.csv', header=0)
        data_set = []
        for i in df['Close']:
            try:
                data = df['Close'][n] / df['Close'][n + 3]
                data_set.append(data)
                n += 1
            except KeyError:
                pass
        for i in range(1,4):
            data_set.append('None')
        try:
            df.insert(7, '3_days_before_change', data_set)
            df.to_csv(fr'C:\Games\test\yahoo\yahoo\result\{name_company}_result.csv', index=False, )
        except ValueError:
            pass


    def delete_files(self):
        with open(self.companies, 'r') as file:
            for line in file:
                name_company = line.strip('\n')
                os.remove(fr'C:\Games\test\yahoo\yahoo\{name_company}.csv')
                os.remove(fr'C:\Games\test\yahoo\yahoo\{name_company}_reversed.csv')


#
# run = Extractor_data()
#
# extract_data = run.run_extractor()

