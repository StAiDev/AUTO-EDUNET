from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
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


def check(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


driver.maximize_window()
driver.get("https://cls1.edunet.net/")
time.sleep(1)
driver.find_element(by=By.ID, value="login_id_main").send_keys(username)
driver.find_element(by=By.ID, value="password_main").send_keys(password)
driver.find_element(by=By.ID, value="password_main").send_keys(Keys.ENTER)
time.sleep(2)
try:
    driver.find_element_by_xpath('//*[@id="mCSB_2_container"]/ul/li/a').click()
except:
    print("id 또는 pw가 맞지 않습니다")
    driver.quit()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="content-main"]/div[2]/div[2]/div/div[1]/div[4]/a').click()
time.sleep(1)
driver.execute_script("window.scrollTo(0, 700)")
time.sleep(0.7)
i = 1
while True:
    target = driver.find_element_by_xpath(f'//*[@id="content-main"]/div[2]/div[2]/div[2]/ul/li[{i}]/div[1]/div[1]/div/div[3]/div/a/span[2]')
    target.click()
    time.sleep(0.9)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(0.3)
    if driver.current_url.startswith("https://cls1.edunet.net/cyber/content/play.do"):
        while True:
            if check('/html/body/div[4]/div[2]/div/div/div/div/div/div/div/div[4]') is True:
                driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/div/div/div/div/div[4]/button[1]').send_keys(Keys.ENTER)
                time.sleep(0.6)
                driver.find_element_by_xpath('//*[@id="mep_0"]/div/div[2]/div[4]/div').click()
            elif check('//*[@id="mep_0"]/div/div[2]/div[4]/div') is True:
                driver.find_element_by_xpath('//*[@id="mep_0"]/div/div[2]/div[4]/div').click()
                time.sleep(0.5)
    else:
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    i += 1
