from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time
import random
from bs4 import BeautifulSoup as bs
import json
import sys

import config

class Inst:
    def __init__(self, url_inst, login, password):
        self.url = url_inst
        self.login = login
        self.password = password
        self.data = {'data': {'items': []}}
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def auth_inst(self):
        print(datetime.today().strftime(f'%H:%M:%S | Выполняется авторизация в Instagram.'))
        self.driver.get(self.url)
        time.sleep(random.randrange(3, 5))
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.NAME, 'username')))
        self.driver.find_element_by_name('username').send_keys(self.login)
        passwd = self.driver.find_element_by_name('password')
        passwd.send_keys(self.password)
        passwd.send_keys(Keys.ENTER)
        time.sleep(5)
        try:
            self.driver.find_element_by_class_name('cmbtv').click()
        except NoSuchElementException:
            sys.exit('GG')
        time.sleep(10)
        print(datetime.today().strftime(f'%H:%M:%S | Авторизация в Instagram выполнена.'))

    def scrap_followers(self, url):
        self.driver.get(url)
        elemnt = self.driver.find_element_by_xpath('//html/body/div[1]/section/main/div/header/section/ul/li[3]')
        elemnt.click()
        soup = bs(self.driver.page_source, 'html.parser')
        print(soup)
        # head = []
        # for elem in soup.select('-nal3'):
        #     for el in elem.find_all('span'):
        #         head.append(el)
