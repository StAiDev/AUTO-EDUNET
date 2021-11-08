import re
from tkinter import *
import tkinter.messagebox as msgbox
from modules import auto_e
from multiprocessing.pool import ThreadPool
import os
import sys
import tkinter.ttk as ttk
from win10toast import ToastNotifier
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-p', '--processer', required=False, default="2", metavar='', help='사용할 프로세서의 수')
parser.add_argument('-l', '--login', required=False, type=str, default=["", ""], nargs="+", metavar='', help='아이디')
args = parser.parse_args()


t = ToastNotifier()
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

if os.path.isfile("./save.txt"):
    try:
        f = open("./save.txt", 'r')
        lines = f.readlines()
        input_username.insert(0, lines[0].strip())
        input_password.insert(0, lines[1].strip())
        f.close()
    except:
        pass

elif args.login:
    input_username.insert(0, args.login[0])
    input_password.insert(0, args.login[1])

save_check = IntVar()
save_checkbtn = Checkbutton(root, text="암호 저장", variable = save_check)
save_checkbtn.grid(column=3, row=1, sticky=N+E+W+S, pady=10)
save_checkbtn.select()

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

mute_check = IntVar()
mute_checkbtn = Checkbutton(root, text="음소거", variable = mute_check)
mute_checkbtn.grid(column=0, row=4, sticky=N+E+W+S, columnspan=2, pady=10)
mute_checkbtn.select()

value1 = ["1번째 클래스", "2번째 클래스", "3번째 클래스"]

clss_label = Label(root, text="클래스")
input_clss = ttk.Combobox(root, values = value1, state="readonly")
input_clss.set("1번째 클래스")
input_clss.grid(column=1, row=5, sticky=N+E+W+S, pady=10)
clss_label.grid(column=0, row=5, sticky=N+E+W+S, pady=10)

processes = int(args.processer)

def do():
    username = input_username.get()
    password = input_password.get()
    time = [i for i in range(len(value)) if input_time.get() in value[i]][0]
    find = [j for j in range(len(values)) if input_loca.get() in values[j]]
    clss = [k for k in range(len(value1)) if input_clss.get() in value1[k]][0]
    save = save_check.get()
    if save:
        f = open("./save.txt", 'w')
        f.write(username + "\n" + password)
        f.close()
    elif os.path.isfile("./save.txt"):
        os.remove("./save.txt")
    loca = matches[int(find[0])]
    mute = mute_check.get()

    pool = ThreadPool(processes=processes)
    pool_result = pool.apply_async(auto_e.run, (clss + 1, loca, time + 1, username, password, mute))
    result = pool_result.get()
    print(processes)
    if result == 1:
        msgbox.showerror("에러", "id나 password가 틀렸습니다")
    if result == 3:
        msgbox.showinfo("성공", "영상 재생에 성공했습니다")
    if result == 2:
        msgbox.showerror("에러", "영상 재생 도중 에러가 발생했습니다.\n다시 시도해 보십시오")
    if result == 4:
        msgbox.showerror("에러", "지역이 올바르지 않습니다")
    
        

btn1 = Button(root, width=20, height=2, text="Launch", command=do)
btn1.grid(column=0, row=6, columnspan=2, sticky=N+E+W+S)

root.mainloop()
