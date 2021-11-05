import re
from tkinter import *
import tkinter.messagebox as msgbox
from modules import auto_e
from multiprocessing.pool import ThreadPool
import os
import sys

try:
    os.chdir(sys._MEIPASS)
    print(sys._MEIPASS)
except:
    os.chdir(os.getcwd())

root = Tk()
root.title("Auto Edunet")
root.geometry("480x360")
root.resizable(False, False)
root.iconbitmap("resources/edunet.ico")

username_label = Label(root, text="ID: ")
input_username = Entry(root, width=30)
input_username.grid(column=1, row=0, pady=10, sticky=N+E+W+S)
username_label.grid(column=0, row=0, pady=10, sticky=N+E+W+S)

password_label = Label(root, text="Password: ")
input_password = Entry(root, width=30, show="*")
input_password.grid(column=1, row=1, sticky=N+E+W+S, pady=10)
password_label.grid(column=0, row=1, sticky=N+E+W+S, pady=10)

num_label = Label(root, text="재생 하고 싶은 강좌 1 ~ 4(1=오늘,2=어제): ")
input_num = Entry(root, width=30)
input_num.grid(column=1, row=2, sticky=N+E+W+S, pady=10)
num_label.grid(column=0, row=2, sticky=N+E+W+S, pady=10)

num_label = Label(root, text="e학습터 앞 주소 ex)cls1:")
input_num = Entry(root, width=30)
input_num.grid(column=1, row=3, sticky=N+E+W+S, pady=10)
num_label.grid(column=0, row=3, sticky=N+E+W+S, pady=10)

def do():
    username = input_username.get()
    password = input_password.get()
    num = input_num.get()
    pool = ThreadPool(processes=2)
    pool_result = pool.apply_async(auto_e.run, (num, username, password))
    result = BooleanVar()
    result = pool_result.get()
    if result == 1:
        msgbox.showerror("에러", "id나 password가 틀렸습니다")
    if result == 3:
        msgbox.showinfo("성공", "영상 재생에 성공했습니다")
    if result == 2:
        msgbox.showerror("에러", "영상 재생 도중 에러가 발생했습니다.\n다시 시도해 보십시오")
    if result == 4:
        msgbox.showerror("에러", "지역 주소가 올바르시 않습니다")
    
        

btn1 = Button(root, width=20, height=2, text="Launch", command=do)
btn1.grid(column=0, row=4, columnspan=2, sticky=N+E+W+S)

root.mainloop()
