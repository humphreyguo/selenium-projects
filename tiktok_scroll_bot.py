from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from getpass import getpass
from time import sleep

class tiktokscroll_bot:
    
    def __init__(self, email) -> None:
        # For running on windows
        s = Service('c:\projects\selenium-projects\chromedriver.exe')
        # For running on linux
        # s = Service('usr/bin/chromedriver')
        self.facebook_email = email
        self.options = Options()
        self.options.add_argument("--start-maximized")
        self.options.add_argument("--disable-notifications")
        self.chrome = webdriver.Chrome(service=s, options=self.options)
        self.ac = ActionChains(self.chrome)
        
    def login(self) -> None:
        self.chrome.get("https://www.tiktok.com/login")
        tiktok_window = self.chrome.window_handles[0]
        facebook_login = self.chrome.find_elements(By.CLASS_NAME, "channel-name-2qzLW")[2]
        facebook_login.click()

        login_window = self.chrome.window_handles[1]
        self.chrome.switch_to.window(login_window)
        email = self.chrome.find_element(By.ID, "email")
        email.send_keys(self.facebook_email)
        
        while True:
            try:
                password = self.chrome.find_element(By.ID, "pass")
            except Exception:
                break
            if not password:
                break
            facebook_password = getpass()
            password.send_keys(facebook_password)
            login = self.chrome.find_element(By.ID, 'loginbutton')
            login.click()
            sleep(3)
            
        print("Logged in successfully")
        
        self.chrome.switch_to.window(tiktok_window)
        
    def scroll(self) -> None:
        video = self.chrome.find_element(By.TAG_NAME, "video")
        video.click()
        while True:
            try:
                duration = self.chrome.execute_script("return document.getElementsByTagName('video')[0].duration")
                sleep(int(duration) + 1)
                self.ac.send_keys(Keys.ARROW_DOWN).perform()
                sleep(1)
                self.ac.reset_actions()
                # sleep(1)
            except KeyboardInterrupt:
                break
            except:
                continue
            
    def close(self) -> None:
        print("Closing bot")
        self.chrome.quit()
        exit(0)
        
if __name__ == '__main__':
    email = "bobby77street@gmail.com"
    bot = tiktokscroll_bot(email)
    bot.login()
    sleep(10)
    bot.scroll()
    bot.close()
    