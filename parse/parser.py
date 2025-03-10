from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from utils import convert_strings_into_dicts, get_post_with_link, scroll_until_element_is_fully_visible
from config import cookies_string
from selenium.webdriver.common.action_chains import ActionChains
import asyncio


class Parser:
    def __init__(self, url, cookie_string):
        self._default_time_of_sleep = 7
        
        self._posts = []
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

    @property
    def posts(self):
        return self._posts
    
    @posts.setter
    def posts(self, new):
        self._posts = new
    
    async def _get_link(self, post):
        parent_elem = post.find_element(By.XPATH, "..")
        post_link = parent_elem.get_attribute("href")
        return post_link, parent_elem

    async def _get_likes_and_comments_amount(self, post, parent_elem):
        self.actions.move_to_element(post).perform()
        await asyncio.sleep(1)
        stats = parent_elem.find_elements(By.CLASS_NAME, "x1ey2m1c")[-1]
        likes_and_comments = stats.find_elements(By.TAG_NAME, "span")
        likes = likes_and_comments[0].text
        comments = likes_and_comments[3].text
        return likes, comments
    
    async def _get_caption(self, post):
        
        scroll_until_element_is_fully_visible(self.actions, post)

        await asyncio.sleep(3)
        
        all_h1s = self.driver.find_elements(By.TAG_NAME, "h1")[1:]
        for h1 in all_h1s:
            print(h1.text)
        close_btn = self.driver.find_element(By.CSS_SELECTOR, "body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x160vmok.x10l6tqk.x1eu8d0j.x1vjfegm > div > div")
        scroll_until_element_is_fully_visible(self.actions, close_btn)

        await asyncio.sleep(2)

    async def _get_all_available_posts(self):
        print("searching for posts")
        all_available_posts = self.driver.find_elements(By.CSS_SELECTOR, "._aagu")
        duplicate_element_found = False
        for post in all_available_posts:
            if True:
                post_link, parent_elem = await self._get_link(post)
                print(f"POST FOUND, LINK - {post_link}")
                post_in_posts = get_post_with_link(self.posts, post_link)
                if post_in_posts:
                    duplicate_element_found = True
                    break
                
                likes, comments = await self._get_likes_and_comments_amount(post, parent_elem)
                
                caption = await self._get_caption(post)
                
                self._posts.append({"link":post_link, "likes":likes, "comments":comments})
            
        return duplicate_element_found
        
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