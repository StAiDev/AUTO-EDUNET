from tkinter import *
from modules.auto_e import run
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time
from pathos.multiprocessing import ProcessingPool as Pool

root = Tk()
root.title("Auto Edunet")
root.geometry("480x640")
root.resizable(False, False)



f = open("login.txt", 'r')

username = f.readline()
password = f.readline()

def do():
    root.mainloop()
    run(username, password)
    print("suc")

do()