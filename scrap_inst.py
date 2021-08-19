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
            print(datetime.today().strftime(f'%H:%M:%S | Выполняется авторизация в Instagram.'))
            self.driver.get(self.url)
            time.sleep(random.uniform(3, 5))
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.NAME, 'username')))
            self.driver.find_element_by_name('username').send_keys(self.login)
            passwd = self.driver.find_element_by_name('password')
            passwd.send_keys(self.password)
            passwd.send_keys(Keys.ENTER)
            time.sleep(5)
            print(datetime.today().strftime(f'%H:%M:%S | Авторизация в Instagram выполнена.'))

        def scrap_followers(self, url):
            self.driver.get(url)
            followers = self.driver.find_element_by_xpath('//html/body/div[1]/section/main/div/header/section/ul/li[3]')
            followers.click()
            self.driver.implicitly_wait(60)
            print(datetime.today().strftime(f'%H:%M:%S | Начал поиск друзей.'))
            friends = set()
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
                    time.sleep(random.uniform(2, 5))
            except:
                print('nenashel')
                pass
            time.sleep(random.uniform(3, 5))
            for elem in soup.find_all(class_='PZuss'):
                for el in elem.find_all('li'):
                    for e in el.find_all('a'):
                        friends.add(e.get('href'))
            friends = list(set(friends))
            print(friends)
            print(len(friends))
