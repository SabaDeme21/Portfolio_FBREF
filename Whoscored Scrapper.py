from bs4 import BeautifulSoup
import random
import time
import undetected_chromedriver as uc
import pandas as pd
import requests
import os
from selenium.webdriver.common.keys import Keys

class Who_Scored_Scraper:
    def agents(self):
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7; rv:101.0) Gecko/20100101 Firefox/101.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Version/14.0.3 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 Edge/96.0.1054.62",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 OPR/80.0.4170.72",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; Trident/7.0; ASL 1.0; .NET4.0E; .NET4.0C; InfoPath.3) like Gecko",
            "Mozilla/5.0 (Linux; Android 10; Pixel 4 XL Build/QD1A.190805.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.115 Mobile Safari/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (Android 10; Mobile; rv:85.0) Gecko/85.0 Firefox/85.0",
            "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.12.388 Version/12.17",
            "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.0 Chrome/73.0.3683.90 Mobile Safari/537.36",
            "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
            "Mozilla/5.0 (compatible; Bingbot/2.0; +http://www.bing.com/bingbot.htm)"
        ]

        self.rendom_agent = random.choice(self.user_agents)
        print(self.rendom_agent)
    
    def setup_driver(self):
        self.option = uc.ChromeOptions()
        self.option.add_argument(f"user-agent={self.rendom_agent}")
        self.option.add_argument("--no-sandbox")
        self.option.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = uc.Chrome(options=self.option)

    def selenium_run(self, url):
        self.driver.get(url)
        time.sleep(random.uniform(2, 3))
        print(self.driver.current_url)
        time.sleep(random.uniform(2, 3))
        self.driver.maximize_window()

    """def human_typing(self, element, country):
        for char in country:
            element.send_keys(char)
            time.sleep(random.uniform(0.01, 0.03))
        element.send_keys(Keys.ENTER)

    def search_bar(self):
        self.search_input_bar = self.driver.find_element(by='xpath', value='//*[@id="header-wrapper"]/div/div/div/div[1]/div/div[2]/div/input')
        time.sleep(random.uniform(0.04, 0.05))
        self.human_typing(self.search_input_bar, "Spain")"""
    
    def butiful(self):
        self.soup = BeautifulSoup(self.driver.page_source, "lxml")
        self.tab = self.soup.find("div", class_='ml12-lg-3 ml12-m-3 ml12-s-4 ml12-xs-5 semi-attached-table')
        #print(self.tab)

        self.headers = []
        for row in self.tab.find_all('th'):
            self.headers.append(row.get("data-property"))
        
        print(self.headers)

        self.data = []

        for row in self.tab.find_all('tr'):  # find all rows
            cells = row.find_all('td')       # find all cells in this row
            if not cells:
                continue  # skip if this row has no td (like header rows)

            row_data = [cell.text.strip() for cell in cells]
            self.data.append(row_data)

        #print(self.data)

    def run(self, url):
        try:
            self.agents()
            self.setup_driver()
            self.selenium_run(url)
            self.butiful()

            input("Enter Quit:")
        except Exception as e:
            print(f"Error:{e}")
        finally:
            self.driver.quit()       

if __name__ == "__main__":
    clas = Who_Scored_Scraper()
    clas.run("https://www.whoscored.com/regions/206/tournaments/4/spain-laliga")