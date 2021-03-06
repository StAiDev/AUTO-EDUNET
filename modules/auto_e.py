from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
import os
import time


def run(clss, loca, num ,username, password, mute):
    t = ToastNotifier()
    chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
    options = webdriver.ChromeOptions()
    if mute:
        options.add_argument("--mute-audio")
    options.add_argument("disable-gpu")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    try:
        service = Service(f'./{chrome_ver}/chromedriver.exe')
    except:
        service = Service(f'./{chrome_ver}/chromedriver')
    service.creationflags = CREATE_NO_WINDOW
    try:
        chromedriver_autoinstaller.install(True)
        driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=options)   
    except:
        chromedriver_autoinstaller.install(True)
        driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver', options=options)
    def check(xpath):
            try:
                driver.find_element(by=By.XPATH, value=xpath)
            except NoSuchElementException:
                return False
            return True

    driver.maximize_window()
    try:
        driver.get(f"https://{loca}.edunet.net/")
    except:
        driver.quit()
        return 4
    time.sleep(1)
    driver.find_element(by=By.ID, value="login_id_main").send_keys(username)
    driver.find_element(by=By.ID, value="password_main").send_keys(password)
    driver.find_element(by=By.ID, value="password_main").send_keys(Keys.ENTER)
    time.sleep(2)
    if driver.current_url == f"https://{loca}.edunet.net/cyber/cm/mcom/pmco000b00.do":
        clss_elem = driver.find_element(by=By.XPATH, value=f'//*[@id="mCSB_2_container"]/ul/li[{str(clss)}]/a')
        clss_elem.click()
    else:
        driver.quit()
        return 1
    time.sleep(2)
    driver.find_element(by=By.XPATH, value=f'//*[@id="content-main"]/div[2]/div[2]/div/div[{num}]/div[4]/a').click()
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 400);")
    time.sleep(0.7)
    i = 1
    while True:
        target = driver.find_element(by=By.XPATH, value=f'//*[@id="content-main"]/div[2]/div[2]/div[2]/ul/li[{i}]')
        target.click()
        time.sleep(0.9)
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(0.6)
        if driver.current_url.startswith("https://cls1.edunet.net/cyber/content/play.do"):
            try:
                driver.find_element(by=By.XPATH, value='//*[@id="mep_0"]/div/div[2]/div[4]/div').click()
                time.sleep(1)
                driver.find_element(by=By.XPATH, value='//*[@id="mep_0"]/div/div[2]/div[4]/div').click()
            except:
                pass
            while True:
                
                if check('/html/body/div[4]/div[2]/div/div/div/div/div/div/div'):
                    if driver.find_element(by=By.XPATH, value='/html/body/div[4]/div[2]/div/div/div/div/div/div/div/div[3]/div/div').text == "????????? ?????????????????????. ????????? ?????? ?????????.":  
                        print("success!")
                        driver.quit()
                        return 3
                    else:
                        try:
                            i += 1
                            driver.find_element(by=By.XPATH, value='/html/body/div[4]/div[2]/div/div/div/div/div/div/div/div[4]/button[1]').click()
                            time.sleep(2)
                            driver.find_element(by=By.XPATH, value='//*[@id="mep_0"]/div/div[3]/div[3]/div[3]/div[2]/button[1]').click()
                            time.sleep(2)
                            driver.find_element(by=By.XPATH, value='//*[@id="mep_0"]/div/div[2]/div[4]/div').click()
                        except:
                            pass
        else:
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        i += 1
