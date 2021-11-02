from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import time

username = 'username'
password = 'password'

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

try:
    driver = webdriver.Chrome(f'{chrome_ver}/chromedriver.exe')   
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'{chrome_ver}/chromedriver.exe')
    

driver.get("https://cls1.edunet.net/")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="login_id_main"]').send_keys(str(username))
driver.find_element_by_xpath('//*[@id="password_main"]').send_keys(str(password))
driver.find_element_by_xpath('//*[@id="loginForm_main"]/div/div[1]/div[2]/button').click()
time.sleep(10)