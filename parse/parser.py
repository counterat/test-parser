from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from utils import convert_strings_into_dicts
from config import cookies_string
from selenium.webdriver.common.action_chains import ActionChains
import asyncio


posts = [
    
]

class Parser:
    def __init__(self, url, cookie_string):
        self._default_time_of_sleep = 7
        
        self.url = url
        self.cookie_string = cookie_string     
        
        #Setting up browser below   
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.actions = ActionChains(self.driver)
    
    def _apply_cookies(self):
        cookies_dict = convert_strings_into_dicts(self.cookie_string)
        for name, value in cookies_dict.items():
            self.driver.add_cookie({"name":name, "value":value})

    async def _get_all_available_posts(self):
        print("searching for posts")
        all_available_posts = self.driver.find_elements(By.CSS_SELECTOR, "._aagu")
        for post in all_available_posts:
            parent_elem = post.find_element(By.XPATH, "..")
            print(parent_elem, parent_elem.get_attribute("href"))
            
    
    async def sleep_some_time(self):
        await asyncio.sleep(self._default_time_of_sleep)
    
    async def main(self):
        self.driver.get(self.url)
        self._apply_cookies()
        
        await asyncio.sleep(self._default_time_of_sleep)
        self.driver.refresh()
        await asyncio.sleep(self._default_time_of_sleep)
        
        self.body = self.driver.find_element(By.TAG_NAME, "body")
        await self._get_all_available_posts()
        await asyncio.sleep(self._default_time_of_sleep)
        await asyncio.sleep(1000)

parser = Parser("https://www.instagram.com/adidas/", cookies_string)

""" print("IN")

time.sleep(5)
driver.refresh()
time.sleep(5)


all_posts = driver.find_elements(By.CLASS_NAME, "_aagu")
for post in all_posts:
    print("post")
    actions.move_to_element(post).perform()
    time.sleep(1)
    stats = driver.find_element(By.CLASS_NAME, "x1ey2m1c")
    
time.sleep(1000)

 """