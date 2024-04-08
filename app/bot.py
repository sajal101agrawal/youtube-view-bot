import os,shutil, time, random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException,ElementNotInteractableException,NoSuchElementException,WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver 
from .models import task
import os
import requests
from selenium.webdriver.chrome.options import Options
from seleniumwire import webdriver as sw_webdriver


lines = []
 
class scrapping_bot():

    def __init__(self,brazzers_bot = False):
        self.base_path = os.getcwd()

    def get_random_prx(self):
        global lines
        if not lines : 
            with open('proxy-data-for-keywordlit-test.txt', 'r') as file: lines = file.readlines()
            
        if lines :
            return random.choice(lines)
        else :
            with open('proxy-data-for-keywordlit-test.txt', 'r') as file: lines = file.readlines()
            return random.choice(lines)
    
    def driver_arguments(self):
        self.options.add_argument('--lang=en')  
        # self.options.add_argument('log-level=3')  
        # self.options.add_argument('--mute-audio') 
        self.options.add_argument("--enable-webgl-draft-extensions")
        # self.options.add_argument('--mute-audio')
        self.options.add_argument("--ignore-gpu-blocklist")
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--headless')

        prefs = {"credentials_enable_service": True,
                'profile.default_content_setting_values.automatic_downloads': 1,
            'download.prompt_for_download': False, 
            'download.directory_upgrade': True,
            'safebrowsing.enabled': True ,
            "profile.password_manager_enabled": True}
        self.options.add_experimental_option("prefs", prefs)
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--start-maximized')    
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument("--ignore-certificate-errors")
        self.options.add_argument('--ignore-ssl-errors')
        self.options.add_argument("--enable-javascript")
        self.options.add_argument("--enable-popup-blocking")
    
    def get_driver(self):
        # self.proxy_driver()
        self.get_local_driver()
        return
        
        for _ in range(30):
            from undetected_chromedriver import Chrome, ChromeOptions

            """Start webdriver and return state of it."""
            self.options = ChromeOptions()
            self.driver_arguments()
            self.options.add_argument('--headless')
            
            try:
                self.driver = Chrome(options=self.options,version_main=123)
                break
            except Exception as e:
                print(f"Error: {e}")
        
        return self.driver

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

    def get_proxy(self, proxy):
        smartproxy_url = 'https://ip.smartproxy.com/json'
        response = requests.get(smartproxy_url, proxies={'http': proxy, 'https': proxy}, verify=False)
        data = response.json()
        current_ip = data['proxy']['ip']
        print(current_ip)
        return current_ip

    def proxy_driver(self):
        proxy_rand = self.get_random_prx().replace('\n',''),
        if isinstance(proxy_rand, tuple) and len(proxy_rand) > 0:
            proxy_rand = proxy_rand[0].strip()
        print("The proxy random is : ",proxy_rand)
        proxy = self.get_proxy(proxy_rand)
        proxy = proxy
        print("The proxy in proxy driver is :",proxy)

        if proxy:
            # seleniumwire_options = {
            #     "proxy": {
            #         "http": f"http://{proxy}",
            #         "https": f"https://{proxy}",
            #     },
            #     "verify_ssl": False,
            # }

            seleniumwire_options = {
                "proxy": {
                    "http": proxy_rand,
                    "https": proxy_rand,
                },
                "verify_ssl": False,
            }
            return proxy, seleniumwire_options

            chrome_options = Options()
            chrome_options.add_argument('--ignore-certificate-errors')
            chrome_options.add_argument('--ignore-ssl-errors=yes')
            chrome_options.add_argument('--remote-debugging-pipe')
            chrome_options.add_argument('--proxy-server=http://%s' % proxy)

            try:
                self.driver = sw_webdriver.Chrome(seleniumwire_options=seleniumwire_options, options=chrome_options)
                print("Successfully initialized WebDriver with proxy.")
            except Exception as e:
                print("Failed to initialize WebDriver with proxy:", e)
        else:
            print("No proxy found. Unable to set up proxy driver.")


            
    def get_local_driver(self):
        """Start webdriver and return state of it."""
        from seleniumwire import webdriver
        from selenium.webdriver.chrome.options import Options
        # for _ in range(30):
        proxy , sw_options=self.proxy_driver()
        print("THe proxy that I am using is :",proxy)
        print("The sw options are as follows :",sw_options)
        self.options = webdriver.ChromeOptions()
        self.driver_arguments()
        try:
            chrome_options = Options()
            chrome_options.add_argument('--ignore-certificate-errors')
            chrome_options.add_argument('--ignore-ssl-errors=yes')
            chrome_options.add_argument('--remote-debugging-pipe')
            chrome_options.add_argument('--disable-web-security')
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--mute-audio') 
            chrome_options.add_argument("--enable-javascript")
            chrome_options.add_argument("--enable-popup-blocking")
            chrome_options.add_argument('--proxy-server=http://%s' % proxy)
            print('The chrome option with proxy --proxy-server=http://%s :' % proxy)
            self.driver = webdriver.Chrome(options=chrome_options,seleniumwire_options=sw_options)
            # time.sleep(2)
            print("passed this step")
        except Exception as e:
            print(e)
        
        return self.driver
    
    def find_element(self, element, locator, locator_type=By.XPATH,
            page=None, timeout=10,
            condition_func=EC.presence_of_element_located,
            condition_other_args=tuple()):
        """Find an element, then return it or None.
        If timeout is less than or requal zero, then just find.
        If it is more than zero, then wait for the element present.
        """
        try:
            if timeout > 0:
                wait_obj = WebDriverWait(self.driver, timeout)
                ele = wait_obj.until(EC.presence_of_element_located((locator_type, locator)))
                # ele = wait_obj.until( condition_func((locator_type, locator),*condition_other_args))
            else:
                print(f'Timeout is less or equal zero: {timeout}')
                ele = self.driver.find_element(by=locator_type,
                        value=locator)
            if page:
                print(
                    f'Found the element "{element}" in the page "{page}"')
            else:
                print(f'Found the element: {element}')
            return ele
        except (NoSuchElementException, TimeoutException) as e:
            if page:
                print(f'Cannot find the element "{element}"'
                        f' in the page "{page}"')
            else:
                print(f'Cannot find the element: {element}')
                
    def click_element(self, element, locator, locator_type=By.XPATH,
            timeout=10):
        """Find an element, then click and return it, or return None"""
        ele = self.find_element(element, locator, locator_type, timeout=timeout)
        
        if ele:
            self.driver.execute_script('arguments[0].scrollIntoViewIfNeeded();',ele)
            self.ensure_click(ele)
            print(f'Clicked the element: {element}')
            return ele

    def input_text(self, text, element, locator, locator_type=By.XPATH,
            timeout=10, hide_keyboard=True):
        """Find an element, then input text and return it, or return None"""
        
        ele = self.find_element(element, locator, locator_type=locator_type,
                timeout=timeout)
        
        if ele:
            for i in range(3):
                try: 
                    ele.send_keys(text)
                    print(f'Inputed "{text}" for the element: {element}')
                    return ele    
                except ElementNotInteractableException :...
                
                
    def random_sleep(self,a=3,b=7,reson = ""):
        random_time = random.randint(a,b)
        print('time sleep randomly :',random_time) if not reson else print('time sleep randomly :',random_time,f' for {reson}')
        time.sleep(random_time)
        
    def CloseDriver(self):
        try: 
            self.driver.quit()
            print('Driver is closed !')
        except Exception as e: ...
        
    def work(self,link : str):
        if not link : return False
        self.get_driver()
        self.driver.get(link)
        body = self.find_element('body','body',By.TAG_NAME)
        if body :
            body.send_keys(Keys.SPACE)        
            self.random_sleep(a=5,b=9,reson='watching youtube videos')
        self.CloseDriver()        
        if not body : return False
        return True
        

#-------------------------------------------NEW CODE ----------------------------------------------------------------------------

# import os
# import time
# import random
# from contextlib import contextmanager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
# from selenium.webdriver.common.keys import Keys
# from selenium import webdriver
# from seleniumwire import webdriver as sw_webdriver
# import subprocess
# import re
# import requests
# from selenium.webdriver.chrome.options import Options

# class scrapping_bot:
#     def __init__(self):
#         self.base_path = os.getcwd()
#         self.lines = []

#     # ------------------------------------- Proxy form Smart proxy end point -----------------------------------------------
  

#     def get_proxy(self,proxy):
#         # Define the URL for smartproxy.com
#         smartproxy_url = 'https://ip.smartproxy.com/json'

#         # Get the response from smartproxy.com to get the current IP
#         response = requests.get(smartproxy_url, proxies={'http': proxy, 'https': proxy}, verify=False)
#         data = response.json()

#         # Extract the current IP address
#         current_ip = data['proxy']['ip']

#         print(current_ip)

#         return current_ip



#     # ------------------------------------- Proxy form Smart proxy end point -----------------------------------------------

#     def get_random_prx(self):
#         if not self.lines:
#             with open('proxy-data-for-keywordlit-test.txt', 'r') as file:
#                 self.lines = file.readlines()
#         if self.lines:
#             #return random.choice(self.lines)
#             return random.choice(self.lines)

#         else:
#             with open('proxy-data-for-keywordlit-test.txt', 'r') as file:
#                 self.lines = file.readlines()
#             #return random.choice(self.lines)
#             return random.choice(self.lines)

#     def get_driver(self):
#         self.get_local_driver()
#         return self.driver

#     def driver_arguments(self, options):
#         options.add_argument('--lang=en')
#         options.add_argument("--enable-webgl-draft-extensions")
#         options.add_argument("--ignore-gpu-blocklist")
#         options.add_argument('--disable-dev-shm-usage')
#         options.add_argument('--start-maximized')
#         options.add_argument("--ignore-certificate-errors")
#         options.add_argument("--enable-javascript")
#         options.add_argument("--enable-popup-blocking")

#         prefs = {"credentials_enable_service": True,
#                  'profile.default_content_setting_values.automatic_downloads': 1,
#                  'download.prompt_for_download': False,
#                  'download.directory_upgrade': True,
#                  'safebrowsing.enabled': True,
#                  "profile.password_manager_enabled": True}
#         options.add_experimental_option("prefs", prefs)
#         options.add_argument('--no-sandbox')
#         options.add_argument('--disable-dev-shm-usage')

#     def get_local_driver(self):
#         for _ in range(30):
#             options = webdriver.ChromeOptions()
#             self.driver_arguments(options)
#             # options.add_argument('--headless')  # Enable headless mode
#             try:
#                 self.driver = webdriver.Chrome(options=options)
#                 # self.driver = webdriver.Chrome(executable_path=r"C:\Users\Adil Anwar\Downloads\chromedriver.exe",options=options)
#                 break
#             except Exception as e:
#                 print(e)



#     def proxy_driver(self):
#         # Get random proxy
#         proxy_rand= self.get_random_prx()
#         proxy =  self.get_proxy(proxy_rand.strip())  #self.get_random_prx()
#         proxy = proxy.strip()
#         if proxy:
#             # Construct proxy options

#             seleniumwire_options = {
#                 "proxy": {
#                     "http": f"http://{proxy}",
#                     "https": f"https://{proxy}",
#                     # "no_proxy": "localhost,127.0.0.1",  # If needed
#                 },
#                 "verify_ssl": False,  # If needed
#             }

#             print("The Proxy used is ", str(seleniumwire_options))
            
#             # Set up Chrome options
#             chrome_options = Options()
#             chrome_options.add_argument('--ignore-certificate-errors')
#             chrome_options.add_argument('--ignore-ssl-errors=yes')
#             chrome_options.add_argument('--remote-debugging-pipe')
#             chrome_options.add_argument('--proxy-server=http://%s' % proxy)

#             # options = webdriver.ChromeOptions()
#             # #self.driver_arguments(chrome_options)
#             # options.add_argument('--mute-audio')
#             # options.add_argument('--remote-debugging-pipe')
#             # options.add_argument("--ignore-ssl-errors=yes")
#             # options.add_argument('--ignore-certificate-errors')
#             #chrome_options.add_argument('--headless')
            
#             # Set up Chrome WebDriver with proxy options
#             try:
#                 self.driver = sw_webdriver.Chrome(seleniumwire_options=seleniumwire_options, options=chrome_options)
#                 print("Successfully initialized WebDriver with proxy.")
#             except Exception as e:
#                 print("Failed to initialize WebDriver with proxy:", e)
#         else:
#             print("No proxy found. Unable to set up proxy driver.")

#     def random_sleep(self, a=10, b=17, reason=""):
#         random_time = random.randint(a, b)
#         print(f'time sleep randomly : {random_time}' if not reason else f'time sleep randomly : {random_time} for {reason}')
#         time.sleep(random_time)


#     @contextmanager
#     def open_driver(self):
#         # self.get_driver()
#         try:
#             self.proxy_driver()  # Apply the proxy settings
#             yield self.driver
#         finally:
#             self.random_sleep(reason='watching youtube videos')
#             self.driver.quit()
#             print('Driver is closed!')

#     def work(self, link: str):
#         if not link:
#             return False
#         with self.open_driver() as driver:
#             # self.proxy_driver()  # Call proxy_driver here
#             driver.get(link)
#             body = self.find_element('body', 'body', By.TAG_NAME)
#             if body:
#                 body.send_keys(Keys.SPACE)
#                 self.random_sleep(reason='watching youtube videos')
#                 return True
#         return False


#     # def proxy_driver(self):
#     #     proxy_options = {
#     #         'proxy': {
#     #             'https': self.get_random_prx(),#.replace('\n', ''), 
#     #         }
#     #     }
#     #     print("The Proxy used is ",str(proxy_options))
#     #     chrome_options = webdriver.ChromeOptions()
#     #     self.driver_arguments(chrome_options)
#     #     chrome_options.add_argument('--mute-audio')
#     #     chrome_options.add_argument('--remote-debugging-pipe')
#     #     chrome_options.add_argument('--headless')
#     #     self.driver = sw_webdriver.Chrome(seleniumwire_options=proxy_options, options=chrome_options)

#     def find_element(self, element, locator, locator_type=By.XPATH,
#                      page=None, timeout=10,
#                      condition_func=EC.presence_of_element_located,
#                      condition_other_args=tuple()):
#         try:
#             if timeout > 0:
#                 wait_obj = WebDriverWait(self.driver, timeout)
#                 ele = wait_obj.until(EC.presence_of_element_located((locator_type, locator)))
#             else:
#                 ele = self.driver.find_element(by=locator_type, value=locator)
#             if page:
#                 print(f'Found the element "{element}" in the page "{page}"')
#             else:
#                 print(f'Found the element: {element}')
#             return ele
#         except (NoSuchElementException, TimeoutException) as e:
#             if page:
#                 print(f'Cannot find the element "{element}" in the page "{page}"')
#             else:
#                 print(f'Cannot find the element: {element}')

#     def click_element(self, element, locator, locator_type=By.XPATH, timeout=10):
#         ele = self.find_element(element, locator, locator_type, timeout=timeout)
#         if ele:
#             self.driver.execute_script('arguments[0].scrollIntoViewIfNeeded();', ele)
#             self.ensure_click(ele)
#             print(f'Clicked the element: {element}')
#             return ele

#     def input_text(self, text, element, locator, locator_type=By.XPATH, timeout=10, hide_keyboard=True):
#         ele = self.find_element(element, locator, locator_type=locator_type, timeout=timeout)
#         if ele:
#             for i in range(3):
#                 try:
#                     ele.send_keys(text)
#                     print(f'Inputted "{text}" for the element: {element}')
#                     return ele
#                 except ElementNotInteractableException:
#                     pass

#     def ensure_click(self, element):
#         try:
#             element.click()
#         except ElementNotInteractableException:
#             self.random_sleep()
#             element.click()


