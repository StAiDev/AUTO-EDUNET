from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]


text = "Test String"
driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')

driver.get("http://shinyang.shop/steve/test.html")