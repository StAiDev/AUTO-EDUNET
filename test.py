from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]


text = "Test String"
driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')

driver.get("http://shinyang.shop/steve/test.html")
driver.find_element_by_xpath('/html/body/form/input[1]').send_keys(text)