from tkinter import *
from modules.auto_e import run

root = Tk()
root.title("Auto Edunet")
root.geometry("480x640")
root.resizable(False, False)


root.mainloop()

f = open("login.txt", 'r')

username = f.readline()
password = f.readline()

run(username, password)