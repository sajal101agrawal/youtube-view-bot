# import os,shutil, time, random
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException, TimeoutException,ElementNotInteractableException,NoSuchElementException,WebDriverException
# from selenium.webdriver.common.keys import Keys
# from selenium import webdriver 
# from .models import task
# lines = []
 
# class scrapping_bot():

#     def __init__(self,brazzers_bot = False):
#         self.base_path = os.getcwd()

#     def get_random_prx(self):
#         global lines
#         if not lines : 
#             with open('proxy-data-for-keywordlit-test.txt', 'r') as file: lines = file.readlines()
            
#         if lines :
#             return random.choice(lines)
#         else :
#             with open('proxy-data-for-keywordlit-test.txt', 'r') as file: lines = file.readlines()
#             return random.choice(lines)
    
#     def driver_arguments(self):
#         self.options.add_argument('--lang=en')  
#         # self.options.add_argument('log-level=3')  
#         # self.options.add_argument('--mute-audio') 
#         self.options.add_argument("--enable-webgl-draft-extensions")
#         # self.options.add_argument('--mute-audio')
#         self.options.add_argument("--ignore-gpu-blocklist")
#         self.options.add_argument('--disable-dev-shm-usage')
#         # self.options.add_argument('--headless')

#         prefs = {"credentials_enable_service": True,
#                 'profile.default_content_setting_values.automatic_downloads': 1,
#             'download.prompt_for_download': False, 
#             'download.directory_upgrade': True,
#             'safebrowsing.enabled': True ,
#             "profile.password_manager_enabled": True}
#         self.options.add_experimental_option("prefs", prefs)
#         self.options.add_argument('--no-sandbox')
#         self.options.add_argument('--start-maximized')    
#         self.options.add_argument('--disable-dev-shm-usage')
#         self.options.add_argument("--ignore-certificate-errors")
#         self.options.add_argument("--enable-javascript")
#         self.options.add_argument("--enable-popup-blocking")
    
#     def get_driver(self):
#         self.get_local_driver()
#         return
        
#         for _ in range(30):
#             from undetected_chromedriver import Chrome, ChromeOptions

#             """Start webdriver and return state of it."""
#             self.options = ChromeOptions()
#             self.driver_arguments()
#             self.options.add_argument('--headless')
            
#             try:
#                 self.driver = Chrome(options=self.options,version_main=123)
#                 break
#             except Exception as e:
#                 print(f"Error: {e}")
        
#         return self.driver

#     def proxy_driver(self):
#         from seleniumwire import webdriver
#         proxy_options = {
#                 'proxy': {
#                     'https': self.get_random_prx().replace('\n',''),
#                 }
#             }
#         chrome_options = webdriver.ChromeOptions()
#         prefs = {"credentials_enable_service": True,
#                 'profile.default_content_setting_values.automatic_downloads': 1,
#             'download.prompt_for_download': False, 
#             'download.directory_upgrade': True,
#             'safebrowsing.enabled': True ,
#             "profile.password_manager_enabled": True}
#         chrome_options.add_experimental_option("prefs", prefs)
#         chrome_options.add_argument('--lang=en')  
#         chrome_options.add_argument('--no-sandbox')
#         chrome_options.add_argument('--mute-audio') 
#         chrome_options.add_argument("--enable-webgl-draft-extensions")
#         chrome_options.add_argument("--ignore-gpu-blocklist")
#         chrome_options.add_argument('--disable-dev-shm-usage')
#         chrome_options.add_argument('--start-maximized')
#         chrome_options.add_argument("--ignore-certificate-errors")
#         chrome_options.add_argument("--enable-javascript")
#         chrome_options.add_argument("--enable-popup-blocking")
#         chrome_options.add_experimental_option("useAutomationExtension", False)
#         chrome_options.add_argument('--remote-debugging-pipe')
#         chrome_options.add_argument('--disable-dev-shm-usage')
#         chrome_options.add_argument('--headless')
#         self.driver = webdriver.Chrome(seleniumwire_options=proxy_options, options=chrome_options)
            
#     def get_local_driver(self):
#         """Start webdriver and return state of it."""
#         from selenium import webdriver
#         for _ in range(30):
#             self.options = webdriver.ChromeOptions()
#             self.driver_arguments()
#             try:
#                 self.driver = webdriver.Chrome(options=self.options)
#                 break
#             except Exception as e:
#                 print(e)
        
#         return self.driver
    
#     def find_element(self, element, locator, locator_type=By.XPATH,
#             page=None, timeout=10,
#             condition_func=EC.presence_of_element_located,
#             condition_other_args=tuple()):
#         """Find an element, then return it or None.
#         If timeout is less than or requal zero, then just find.
#         If it is more than zero, then wait for the element present.
#         """
#         try:
#             if timeout > 0:
#                 wait_obj = WebDriverWait(self.driver, timeout)
#                 ele = wait_obj.until(EC.presence_of_element_located((locator_type, locator)))
#                 # ele = wait_obj.until( condition_func((locator_type, locator),*condition_other_args))
#             else:
#                 print(f'Timeout is less or equal zero: {timeout}')
#                 ele = self.driver.find_element(by=locator_type,
#                         value=locator)
#             if page:
#                 print(
#                     f'Found the element "{element}" in the page "{page}"')
#             else:
#                 print(f'Found the element: {element}')
#             return ele
#         except (NoSuchElementException, TimeoutException) as e:
#             if page:
#                 print(f'Cannot find the element "{element}"'
#                         f' in the page "{page}"')
#             else:
#                 print(f'Cannot find the element: {element}')
                
#     def click_element(self, element, locator, locator_type=By.XPATH,
#             timeout=10):
#         """Find an element, then click and return it, or return None"""
#         ele = self.find_element(element, locator, locator_type, timeout=timeout)
        
#         if ele:
#             self.driver.execute_script('arguments[0].scrollIntoViewIfNeeded();',ele)
#             self.ensure_click(ele)
#             print(f'Clicked the element: {element}')
#             return ele

#     def input_text(self, text, element, locator, locator_type=By.XPATH,
#             timeout=10, hide_keyboard=True):
#         """Find an element, then input text and return it, or return None"""
        
#         ele = self.find_element(element, locator, locator_type=locator_type,
#                 timeout=timeout)
        
#         if ele:
#             for i in range(3):
#                 try: 
#                     ele.send_keys(text)
#                     print(f'Inputed "{text}" for the element: {element}')
#                     return ele    
#                 except ElementNotInteractableException :...
                
                
#     def random_sleep(self,a=3,b=7,reson = ""):
#         random_time = random.randint(a,b)
#         print('time sleep randomly :',random_time) if not reson else print('time sleep randomly :',random_time,f' for {reson}')
#         time.sleep(random_time)
        
#     def CloseDriver(self):
#         try: 
#             self.driver.quit()
#             print('Driver is closed !')
#         except Exception as e: ...
        
#     def work(self,link : str):
#         if not link : return False
#         self.get_driver()
#         self.driver.get(link)
#         body = self.find_element('body','body',By.TAG_NAME)
#         if body :
#             body.send_keys(Keys.SPACE)        
#             self.random_sleep(a=5,b=9,reson='watching youtube videos')
#         self.CloseDriver()        
#         if not body : return False
#         return True
        



import os
import time
import random
from contextlib import contextmanager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from seleniumwire import webdriver as sw_webdriver

class scrapping_bot:
    def __init__(self):
        self.base_path = os.getcwd()
        self.lines = []

    def get_random_prx(self):
        if not self.lines:
            with open('proxy-data-for-keywordlit-test.txt', 'r') as file:
                self.lines = file.readlines()
        if self.lines:
            return random.choice(self.lines)
        else:
            with open('proxy-data-for-keywordlit-test.txt', 'r') as file:
                self.lines = file.readlines()
            return random.choice(self.lines)

    def get_driver(self):
        self.get_local_driver()
        return self.driver

    def driver_arguments(self, options):
        options.add_argument('--lang=en')
        options.add_argument("--enable-webgl-draft-extensions")
        options.add_argument("--ignore-gpu-blocklist")
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--start-maximized')
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--enable-javascript")
        options.add_argument("--enable-popup-blocking")

        prefs = {"credentials_enable_service": True,
                 'profile.default_content_setting_values.automatic_downloads': 1,
                 'download.prompt_for_download': False,
                 'download.directory_upgrade': True,
                 'safebrowsing.enabled': True,
                 "profile.password_manager_enabled": True}
        options.add_experimental_option("prefs", prefs)
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

    def get_local_driver(self):
        for _ in range(30):
            options = webdriver.ChromeOptions()
            self.driver_arguments(options)
            options.add_argument('--headless')  # Enable headless mode
            try:
                self.driver = webdriver.Chrome(options=options)
                break
            except Exception as e:
                print(e)

    def proxy_driver(self):
        proxy_options = {
            'proxy': {
                'https': self.get_random_prx().replace('\n', ''),
            }
        }
        chrome_options = webdriver.ChromeOptions()
        self.driver_arguments(chrome_options)
        chrome_options.add_argument('--mute-audio')
        chrome_options.add_argument('--remote-debugging-pipe')
        chrome_options.add_argument('--headless')
        self.driver = sw_webdriver.Chrome(seleniumwire_options=proxy_options, options=chrome_options)

    def find_element(self, element, locator, locator_type=By.XPATH,
                     page=None, timeout=10,
                     condition_func=EC.presence_of_element_located,
                     condition_other_args=tuple()):
        try:
            if timeout > 0:
                wait_obj = WebDriverWait(self.driver, timeout)
                ele = wait_obj.until(EC.presence_of_element_located((locator_type, locator)))
            else:
                ele = self.driver.find_element(by=locator_type, value=locator)
            if page:
                print(f'Found the element "{element}" in the page "{page}"')
            else:
                print(f'Found the element: {element}')
            return ele
        except (NoSuchElementException, TimeoutException) as e:
            if page:
                print(f'Cannot find the element "{element}" in the page "{page}"')
            else:
                print(f'Cannot find the element: {element}')

    def click_element(self, element, locator, locator_type=By.XPATH, timeout=10):
        ele = self.find_element(element, locator, locator_type, timeout=timeout)
        if ele:
            self.driver.execute_script('arguments[0].scrollIntoViewIfNeeded();', ele)
            self.ensure_click(ele)
            print(f'Clicked the element: {element}')
            return ele

    def input_text(self, text, element, locator, locator_type=By.XPATH, timeout=10, hide_keyboard=True):
        ele = self.find_element(element, locator, locator_type=locator_type, timeout=timeout)
        if ele:
            for i in range(3):
                try:
                    ele.send_keys(text)
                    print(f'Inputted "{text}" for the element: {element}')
                    return ele
                except ElementNotInteractableException:
                    pass

    def random_sleep(self, a=3, b=7, reason=""):
        random_time = random.randint(a, b)
        print(f'time sleep randomly : {random_time}' if not reason else f'time sleep randomly : {random_time} for {reason}')
        time.sleep(random_time)

    def ensure_click(self, element):
        try:
            element.click()
        except ElementNotInteractableException:
            self.random_sleep()
            element.click()

    @contextmanager
    def open_driver(self):
        self.get_driver()
        try:
            yield self.driver
        finally:
            self.driver.quit()
            print('Driver is closed!')

    def work(self, link: str):
        if not link:
            return False
        with self.open_driver() as driver:
            driver.get(link)
            body = self.find_element('body', 'body', By.TAG_NAME)
            if body:
                body.send_keys(Keys.SPACE)
                self.random_sleep(reason='watching youtube videos')
                return True
        return False
