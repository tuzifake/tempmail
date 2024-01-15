import colorama
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os
import sys
import random
import string
def color():
    color = f"""
    \033[1;34mRegister Mail.tm using selenium by Dino !
    """
    for a in color:
        sys.stdout.write(a)
        sys.stdout.flush()
        sleep(0.001)

color()
def main():
    hotmail.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div/div/div[2]/div[4]/div[1]/div/button').click()
    sleep(1)
    hotmail.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div/div/div[2]/div[4]/div[2]/div/div/div[2]/button[1]').click()
    sleep(2)
    user_acc = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    hotmail.find_element(By.XPATH,'//*[@id="nuid-3"]').send_keys(user_acc)
    sleep(2)
    user_pass = "1"
    hotmail.find_element(
        By.XPATH, '//*[@id="nuid-4"]').send_keys(user_pass)
    hotmail.find_element(
        By.XPATH, '//*[@id="headlessui-dialog-panel-12"]/div/div/div[2]/span[1]/button').click()
    with open('C:\\Users\\Administrator\\Desktop\\tempmail-main\\tempmail-main\\Register mail.txt', 'a', encoding="utf-8") as account_roblox:
            account_roblox.write(str(user_acc) + "@jcnorris.com")
            account_roblox.write('|' + user_pass+'\n')
while True:
    extension_path = "C:\\Users\\Administrator\\Desktop\\tempmail-main\\tempmail-main\\uBlock.crx"
    ser = Service("C:\\Users\\Administrator\\Desktop\\tempmail-main\\tempmail-main\\chromedriver.exe")
    cai_dat = webdriver.ChromeOptions()
    cai_dat.add_extension(extension_path)
    #cai_dat.add_argument('--headless')  # Run in headless mode
    cai_dat.add_argument('--disable-gpu')  # Disable GPU acceleration (required for headless mode in some cases)
    hotmail = webdriver.Chrome(options=cai_dat, service=ser)
    hotmail.get('https://www.mail.tm/')
    sleep(7)
    main()
