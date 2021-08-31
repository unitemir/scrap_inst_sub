from typing import Set, Any
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time
import random
from bs4 import BeautifulSoup as bs
import sys


class Inst:
    def __init__(self, url_inst, login, password):
        self.url = url_inst
        self.login = login
        self.password = password
        self.data = {'data': {'items': []}}
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def auth_inst(self):
        self.driver.get('https://instagram.com/')
        time.sleep(random.uniform(3,5))
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.NAME, 'username')))
        self.driver.find_element_by_name('username').send_keys(self.login)
        passwd = self.driver.find_element_by_name('password')
        passwd.send_keys(self.password)
        passwd.send_keys(Keys.ENTER)
        time.sleep(5)

    def close_browser(self):
        self.driver.quit()

    def get_friends_list_by_instagram_username(self, inst_username):

        self.driver.implicitly_wait(60)
        self.driver.get(f'https://www.instagram.com/{inst_username}/')

        try:
            followers = self.driver.find_element_by_xpath(
                '/html/body/div[1]/section/main/div/header/section/ul/li[3]')
            foll = followers.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span')
            if int(foll.text) > 500:
                return ['dalbaeb s 500 + podpiskami']
            followers.click()
        except:
            return []

        friends = dict()
        try:
            self.driver.find_element_by_class_name('PZuss')
            pop_up_window = WebDriverWait(
                self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='isgrP']")))
            i = 1
            fr = list()
            while True:
                self.driver.execute_script(
                    'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                    pop_up_window)
                soup = bs(self.driver.page_source, 'html.parser')
                fr.append(len(soup.find_all('li', {"class": "wo9IH"})))
                if i % 10 == 0:
                    if len(set(fr)) == 1:
                        break
                    fr = []
                i += 1
                time.sleep(3)
        except:
            return []
        time.sleep(3)
        for elem in soup.find_all(class_='PZuss'):
            for el in elem.find_all('li'):
                name = el.find(class_='wFPL8').text
                username = el.find('a').get('href')
                friends[name] = username
                print(friends[name])
        # friends: Set[Any] = set(friends)
        return friends
