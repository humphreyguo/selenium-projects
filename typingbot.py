from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import re

# Program slightly modifies original code here: 
# https://hackernoon.com/980-wpm-typing-bot-with-python-just-using-12-lines-of-code-ig2qj326c
# This program was just used purely as a learning experience

def get_text(chrome):
    text = ""
    for i in range(chrome.execute_script('return document.querySelectorAll(".line").length')):
        text += chrome.execute_script(f"return document.querySelectorAll(\".line\")[{str(i)}].innerHTML")

    text = re.sub(r'<[^>]*>','',text)
    text = re.sub('⏎', Keys.ENTER, text)
    return text

if __name__ == "__main__":
    chrome = webdriver.Chrome('/usr/bin/chromedriver')
    chrome.get('https://thetypingcat.com/typing-speed-test/1m')

    sleep(5)

    ac = ActionChains(chrome)
    ac.send_keys('a').perform()
    text = get_text(chrome)

    for line in text:
        ac.send_keys(line).perform()
        ac.send_keys(Keys.ENTER).perform()
    