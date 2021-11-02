from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time

f = open("login.txt", 'r')

username = f.readline()
password = f.readline()

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')   
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')

driver.maximize_window()
driver.get("https://cls1.edunet.net/")
driver.find_element(by=By.ID, value="login_id_main").send_keys(username)
driver.find_element(by=By.ID, value="password_main").send_keys(password)
driver.find_element(by=By.ID, value="password_main").send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element(by=By.XPATH, value='//*[@id="mCSB_2_container"]/ul/li/a').click()
time.sleep(1000)
driver.find_element(by=By.XPATH, value='//*[@id="content-main"]/div[2]/div[2]/div/div[1]/div[2]/a').click()
