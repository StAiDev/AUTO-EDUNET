from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import time

username = 'username'
password = 'password'

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')   
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')

driver.get("https://cls1.edunet.net/")
driver.find_element_by_id("login_id_main").send_keys(username)
driver.find_element_by_id("password_main").send_keys(password)
driver.find_element_by_xpath('//*[@id="loginForm_main"]/div/div[1]/div[2]/button').click()
driver.implicitly_wait(3)   