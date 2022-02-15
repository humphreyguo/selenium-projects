from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from getpass import getpass
from time import sleep
from random import randint

EMAIL = "bobby77street@gmail.com"
PHONE = "0435902779"
FIRST_NAME = "Robert"
LAST_NAME = "Smith"
PLAYERS = ["Shawn Blore","Luke Brooks","Adam Doueihi","Luke Garner","Oliver Gildart","Jackson Hastings","William Kei","Asu Kepaoa","Daine Laurie","Luciano Leilua","Jacob Liddle","Jock Madden","Ken Maumalo","Thomas Mikaele","Zane Musgrove","David Nofoaluma","Joe Ofahengaue","Tyrone Peachey","Alex Seyfarth","Jake Simpkin","Tuki Simpkins","Tommy Talau","James Tamou","Kelma Tuilagi","Alex Twal","Starford To'a","Stefano Utoikamanu"]

def submit_details(chrome, player):
    first_name_input = chrome.find_element(By.NAME, "First_Name__c")
    last_name_input = chrome.find_element(By.NAME, "Last_Name__c")
    email_input = chrome.find_element(By.NAME, "Email__c")
    phone_input = chrome.find_element(By.NAME, "Phone__c")
    fave_player_input = chrome.find_element(By.NAME, "GTKY_Favourite_Wests_Tigers_player__c")
    donation_question = Select(chrome.find_element(By.NAME, "Foundation_Donation__c"))
    communication_question = Select(chrome.find_element(By.NAME, "Hit_Up_communication__c"))
    
    first_name_input.send_keys(FIRST_NAME)
    last_name_input.send_keys(LAST_NAME)
    email_input.send_keys(EMAIL)
    phone_input.send_keys(PHONE)
    fave_player_input.send_keys(player)
    donation_question.select_by_value('No')
    communication_question.select_by_value('No')
    
    submit = chrome.find_element(By.ID, "saveForm")
    submit.click()
    
    sleep(3)
    
def fetch_page(chrome):
    submission_count = 0
    while True:
        chrome.get("https://weststigers.secure.force.com/apex/b3f__formcomplete?id=a0F98000000CsAXEA0&Forms_Submission__cId=[XXXXX&fbclid=IwAR2n2pJAD0xgNKuRRKf4MrLnTN1HvmwRF-qiQmMfwhuWCM0t9DbQPDvbXaQ")
        sleep(3)
        player = PLAYERS[randint(0, 26)]
        submit_details(chrome, player)
        submission_count += 1
        print(f"Submitting form number {submission_count}")

if __name__ == '__main__':
    s = Service('c:\projects\selenium-projects\chromedriver.exe')
    opts = Options()
    opts.add_argument("--start-maximized")
    opts.add_argument("--disable-notifications")
    chrome = webdriver.Chrome(service=s, options=opts)
    fetch_page(chrome)
