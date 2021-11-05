import re
from tkinter import *
import tkinter.messagebox as msgbox
from modules import auto_e
from multiprocessing.pool import ThreadPool
import os
import sys
import tkinter.ttk as ttk
from win10toast import ToastNotifier

t = ToastNotifier()
try:
    os.chdir(sys._MEIPASS)
    print(sys._MEIPASS)
except:
    os.chdir(os.getcwd())

root = Tk()
root.title("Auto Edunet")
root.geometry("300x240")
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

value = ["오늘", "1일전", "2일전", "3일전"]

time_label = Label(root, text="시청할 강좌")
input_time = ttk.Combobox(root, values = value, state="readonly")
input_time.set("오늘")
input_time.grid(column=1, row=2, sticky=N+E+W+S, pady=10)
time_label.grid(column=0, row=2, sticky=N+E+W+S, pady=10)

values = ["서울", "부산", "대구", "인천", "광주", "대전", "울산", "세종", "경기", "강원", "충북", "충남", "전북", "전남", "경북", "경남", "제주", "기타"]
matches = ["cls1", "cls2", "cls3", "cls4", "cls5", "cls5", "cls2", "cls10", "cls7", "cls3", "cls4", "cls10", "cls11", "cls11", "cls9", "cls8", "cls9", "cls7"]


loca_label = Label(root, text="e학습터 지역")
input_loca = ttk.Combobox(root, values = values, state="readonly")
input_loca.set("서울")
input_loca.grid(column=1, row=3, sticky=N+E+W+S, pady=10)
loca_label.grid(column=0, row=3, sticky=N+E+W+S, pady=10)

def do():
    username = input_username.get()
    password = input_password.get()
    time = [i for i in range(len(value)) if input_time.get() in value[i]][0]
    find = [j for j in range(len(values)) if input_loca.get() in values[j]]
    loca = matches[int(find[0])]
    pool = ThreadPool(processes=2)
    pool_result = pool.apply_async(auto_e.run, (loca, time + 1, username, password))
    result = pool_result.get()
    if result == 1:
        msgbox.showerror("에러", "id나 password가 틀렸습니다")
    if result == 3:
        msgbox.showinfo("성공", "영상 재생에 성공했습니다")
    if result == 2:
        msgbox.showerror("에러", "영상 재생 도중 에러가 발생했습니다.\n다시 시도해 보십시오")
    if result == 4:
        msgbox.showerror("에러", "지역이 올바르지 않습니다")
    
        

btn1 = Button(root, width=20, height=2, text="Launch", command=do)
btn1.grid(column=0, row=4, columnspan=2, sticky=N+E+W+S)

root.mainloop()
