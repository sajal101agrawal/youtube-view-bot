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
import pyautogui

lines = []
 
class scrapping_bot():

    def __init__(self):
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
        # self.options.add_argument('--headless')

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
            # chrome_options.add_argument('--headless')
            chrome_options.add_argument('--mute-audio') 
            chrome_options.add_argument("--enable-javascript")
            chrome_options.add_argument("--enable-popup-blocking")
# ------------------------------TO REDUCE BANDWIDTH -----------------------------------------------------------------
            chrome_options.add_experimental_option("prefs", {
                "profile.managed_default_content_settings.images": 2,  # Disable images
                "profile.managed_default_content_settings.media_stream": 2,  # Disable media streaming
                # "profile.managed_default_content_settings.javascript": 2,        # Disable JavaScript
                "profile.managed_default_content_settings.fonts": 2,              # Disable fonts
                "profile.managed_default_content_settings.cookies": 2,            # Block third-party cookies
                "profile.default_content_setting_values.notifications": 2,        # Block notifications
                "profile.managed_default_content_settings.stylesheets": 2,
                "profile.managed_default_content_settings.plugins": 2,
                "profile.managed_default_content_settings.cache": 1,
                "profile.managed_default_content_settings.webgl": 2,
                "profile.managed_default_content_settings.webrtc": 2,
                "profile.managed_default_content_settings.favicon": 2,
                "profile.managed_default_content_settings.third_party_cookies": 2,
                "profile.block_third_party_cookies": True,
                "profile.default_content_settings.popups": 0
            })

            # Set a smaller browser window size to reduce resource load
            # chrome_options.add_argument('--window-size=800,600')
# ------------------------------TO REDUCE BANDWIDTH -----------------------------------------------------------------
            chrome_options.add_argument('--proxy-server=http://%s' % proxy)
            chrome_options.add_argument('--disable-gpu')  # Disable hardware acceleration
            print('The chrome option with proxy --proxy-server=http://%s :' % proxy)
            self.driver = webdriver.Chrome(options=chrome_options,seleniumwire_options=sw_options)
            # self.driver.request_interceptor = lambda request: request.modify(upstream_kbps=50, downstream_kbps=500)
            
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
        
    # def work(self,link : str):
    #     if not link : return False
    #     self.get_driver()
    #     self.driver.get(link)
    #     body = self.find_element('body','body',By.TAG_NAME)
    #     if body :
    #         body.send_keys(Keys.SPACE)        
    #         self.random_sleep(a=5,b=9,reson='watching youtube videos')
    #     self.CloseDriver()        
    #     if not body : return False
    #     return True

#------------------------------------------------------new code ------------------------------------------------------------------

    def set_lowest_video_quality(self):
            try:
                # Inject JavaScript to set video quality to lowest
                # self.driver.execute_script('''
                #     var video = document.querySelector('video');
                #     if (video) {
                #         video.playbackRate = 0.25; // Optionally adjust playback rate
                #         video.setPlaybackQuality('tiny'); // Set to lowest quality
                #     }
                # ''')

                self.driver.execute_script('''
                    var video = document.querySelector('video');
                    if (video) {
                        var availableQualities = video.getAvailableQualityLevels();
                        if (availableQualities && availableQualities.length > 0) {
                            // Find the lowest quality available (e.g., 'tiny', 'small', etc.)
                            var lowestQuality = availableQualities[availableQualities.length - 1];  // Assuming lowest quality is at the end of the array
                            video.setPlaybackQuality(lowestQuality);
                        }
                    }
                ''')
                print('Changed video quality to lowest')
            except Exception as e:
                print(f'Error changing video quality: {e}')


    # def simulate_user_activity(self,a=6,b=10):
    #     # Simulate user activity during video playback
    #     try:
    #         random_duration = random.randint(a, b)  # Random duration between 6 to 10 seconds
    #         print(f'Simulating user activity for {random_duration} seconds...')
            
    #         # Simulate random user actions during the specified duration
    #         end_time = time.time() + random_duration
    #         while time.time() < end_time:
    #             # Simulate random scrolling
    #             pyautogui.scroll(random.randint(-100, 100))

    #             # Simulate random mouse clicks
    #             if random.random() < 0.33:  # 20% chance of mouse click
    #                 pyautogui.click()

    #             # Simulate random key presses
    #             if random.random() < 0.15:  # 10% chance of key press
    #                 random_key = random.choice(['left', 'right', 'up', 'down', 'enter', 'space'])
                    
    #                 if random_key == 'm':  # Mute audio (key: 'm')
    #                     pyautogui.press('m')
    #                     print('Muted audio')

    #                 else:
    #                     pyautogui.press(random_key)

    #             # Simulate random volume adjustments
    #             if random.random() < 0.1:  # 10% chance of volume adjustment
    #                 # Adjust volume up (key: 'volumeup')
    #                 if random.random() < 0.5:
    #                     pyautogui.press('volumeup')
    #                     print('Volume up')

    #                 # Adjust volume down (key: 'volumedown')
    #                 else:
    #                     pyautogui.press('volumedown')
    #                     print('Volume down')

    #             # Randomly click a video link after a certain delay
    #             if time.time() < end_time - 3:  # Click a link if at least 3 seconds remaining
    #                 if random.random() < 0.05:  # 5% chance of clicking a link
    #                     video_links = self.driver.find_elements(By.TAG_NAME, 'a')
    #                     if video_links:
    #                         random_link = random.choice(video_links)

    #                         random_link.click()
    #                         print('Clicked a random video link')

    #             time.sleep(0.5)  # Wait a short interval between actions

    #         print('User activity simulation completed.')
    #     except Exception as e:
    #         print('Error during user activity simulation:', e)

    def simulate_user_activity(self, a=6, b=10):
        # Simulate user activity during video playback
        try:
            random_duration = random.randint(a, b)  # Random duration between a and b seconds
            print(f'Simulating user activity for {random_duration} seconds...')
            
            # Simulate random user actions during the specified duration
            end_time = time.time() + random_duration
            while time.time() < end_time:
                # Simulate random scrolling (scroll up or down by a random amount)
                self.scroll_random()

                # Simulate random mouse clicks (click a random element with a certain probability)
                if random.random() < 0.33:  # 33% chance of clicking
                    self.click_random_element()

                # Simulate random key presses (press a random key with a certain probability)
                if random.random() < 0.15:  # 15% chance of key press
                    self.press_random_key()

                # Simulate random volume adjustments (adjust volume up or down with a certain probability)
                if random.random() < 0.1:  # 10% chance of volume adjustment
                    self.adjust_volume()

                # Randomly click a video link after a certain delay
                if time.time() < end_time - 3:  # Click a link if at least 3 seconds remaining
                    if random.random() < 0.05:  # 5% chance of clicking a link
                        self.click_random_video_link()

                time.sleep(0.5)  # Wait a short interval between actions

            print('User activity simulation completed.')
        except Exception as e:
            print('Error during user activity simulation:', e)


    def scroll_random(self):
        # Simulate random scrolling (scroll up or down by a random amount)
        scroll_amount = random.randint(-100, 100)
        self.driver.execute_script(f'window.scrollBy(0, {scroll_amount});')

    def click_random_element(self):
        # Simulate clicking a random element on the page
        elements = self.driver.find_elements(By.XPATH, '//*[not(ancestor::a)]')  # Exclude links to avoid accidental navigation
        if elements:
            random_element = random.choice(elements)

            # Scroll to the random element
            self.driver.execute_script('arguments[0].scrollIntoView(true);', random_element)
            # Wait for the element to be clickable
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, random_element)))

            random_element.click()
            print('Clicked a random element')

    def press_random_key(self):
        # Simulate pressing a random key (can be any key including letters, arrows, space, etc.)
        random_key = random.choice(['ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Enter', 'Space'])
        body = self.driver.find_element(By.TAG_NAME, 'body')
        body.send_keys(random_key)
        print(f'Pressed key: {random_key}')

    def adjust_volume(self):
        # Simulate adjusting volume by sending volume up or volume down keys
        if random.random() < 0.5:  # 50% chance of volume up
            self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_UP)
            print('Volume up')
        else:  # 50% chance of volume down
            self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_DOWN)
            print('Volume down')

    def click_random_video_link(self):
        # Simulate clicking a random video link on the page
        video_links = self.driver.find_elements(By.TAG_NAME, 'a')
        if video_links:
            random_link = random.choice(video_links)

            # Scroll to the random video link
            self.driver.execute_script('arguments[0].scrollIntoView(true);', random_link)
            # Wait for the element to be clickable
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.TAG_NAME, 'a')))

            random_link.click()
            print('Clicked a random video link')
    

#------------------------------------------------------NEW CODE-------------------------------------------------------------------


    def work(self, link: str):
        if not link:
            return False
        
        self.get_driver()
        
        try:
            # self.driver.set_network_conditions(
            #     offline=False,  # Ensure the network is not offline
            #     latency=5000,  # Set latency (ms) to introduce delay
            #     download_throughput=500 * 1024,  # Set download speed (bytes/s)
            #     upload_throughput=500 * 1024  # Set upload speed (bytes/s)
            # )
            self.driver.get(link)
            body = self.find_element('body', 'body', By.TAG_NAME)
            
            if body:
                print(body.text)
                body.send_keys(Keys.SPACE)
                time.sleep(3)
                # self.change_video_quality()
                # self.random_sleep(a=6, b=10, reson='watching youtube videos')

#------------------------------------------NEW CODE----------------------------------------------------------------------------
                # self.set_lowest_video_quality()  # Set video quality to lowest
                # Randomly simulate user activity during video playback
                self.simulate_user_activity(a=6,b=10)
#------------------------------------------NEW CODE----------------------------------------------------------------------------
                self.CloseDriver()
                return True
            else:
                self.CloseDriver()
                return False
        except Exception as e:
            print('Error during work:', e)
            self.CloseDriver()
            return False

    def change_video_quality(self):
        try:
        # Simulate opening settings menu using 'k' key
            self.driver.find_element(By.CSS_SELECTOR, ".ytp-settings-button").send_keys(Keys.SHIFT + 'k')
            time.sleep(0.5)  # Wait for the settings menu to open

            # Simulate navigating to the quality submenu using arrow keys
            self.driver.switch_to.active_element.send_keys(Keys.ARROW_DOWN)  # Navigate down to quality submenu
            time.sleep(0.5)  # Wait for the submenu to open
            self.driver.switch_to.active_element.send_keys(Keys.ARROW_DOWN)  # Navigate to the quality option
            time.sleep(0.5)  # Wait for the option to be highlighted
            self.driver.switch_to.active_element.send_keys(Keys.ENTER)  # Select the quality option
            self.driver.switch_to.active_element.send_keys(Keys.ARROW_DOWN)  # Navigate to the quality option
            time.sleep(0.5)  # Wait for the option to be highlighted
            self.driver.switch_to.active_element.send_keys(Keys.ARROW_DOWN)  # Navigate to the quality option
            time.sleep(0.5)  # Wait for the option to be highlighted
            self.driver.switch_to.active_element.send_keys(Keys.ENTER)  # Select the quality option
            self.driver.switch_to.active_element.send_keys(Keys.ARROW_UP)
            time.sleep(0.5)  # Wait for the next option to be highlighted
            self.driver.switch_to.active_element.send_keys(Keys.ENTER)  # Select the highlighted quality
            print("Changed video quality to lowest")

        except Exception as e:
            print(f"Error changing video quality: {e}")

    def ensure_click(self, element):
        try:
            element.click()
        except ElementNotInteractableException:
            # self.random_sleep()
            element.click()


