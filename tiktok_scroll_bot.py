from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchCookieException, NoSuchElementException
from getpass import getpass
from time import sleep

class tiktokscroll_bot:
    
    def __init__(self, email) -> None:
        self.facebook_email = email
        self.options = Options()
        self.options.add_argument("--start-maximized")
        self.options.add_argument("--disable-notifications")
        self.chrome = webdriver.Chrome(options=self.options)
        self.ac = ActionChains(self.chrome)
        
    def login(self) -> None:
        self.chrome.get("https://www.tiktok.com/login")
        tiktok_window = self.chrome.window_handles[0]
        facebook_login = self.chrome.find_elements_by_class_name("channel-name-2qzLW")[2]
        facebook_login.click()

        login_window = self.chrome.window_handles[1]
        self.chrome.switch_to.window(login_window)
        email = self.chrome.find_element_by_id('email')
        email.send_keys(self.facebook_email)
        
        while True:
            try:
                password = self.chrome.find_element_by_id('pass')
            except Exception:
                break
            if not password:
                break
            facebook_password = getpass()
            password.send_keys(facebook_password)
            login = self.chrome.find_element_by_id('loginbutton')
            login.click()
            sleep(3)
        
        self.chrome.switch_to.window(tiktok_window)
        
    def scroll(self) -> None:
        video = self.chrome.find_element_by_tag_name('video')
        video.click()
        # sleep(20) # Do the captcha
        # while True:
        #     duration = self.chrome.execute_script("return document.getElementsByTagName('video')[0].duration")
        #     print(duration)
        for _ in range(5):
            duration = self.chrome.execute_script("return document.getElementsByTagName('video')[0].duration")
            sleep(int(duration) + 1)
            self.ac.send_keys(Keys.ARROW_DOWN).perform()
        # print(video)
        # print(len(video))
        # video.click()
        
        
if __name__ == '__main__':
    # email = input("Please enter your facebook email: ")
    email = "bobby77street@gmail.com"
    bot = tiktokscroll_bot(email)
    bot.login()
    sleep(10)
    bot.scroll()
    