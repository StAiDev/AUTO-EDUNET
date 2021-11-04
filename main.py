from tkinter import *
import tkinter.messagebox as msgbox
from modules import auto_e
from multiprocessing.pool import ThreadPool

root = Tk()
root.title("Auto Edunet")
root.geometry("300x360")
root.resizable(False, False)
root.iconbitmap("resources/edunet.ico")

username_label = Label(root, text="ID: ")
input_username = Entry(root, width=30)
input_username.grid(column=1, row=0, pady=10, sticky=N+E+W+S)
username_label.grid(column=0, row=0, pady=10, sticky=N+E+W+S)

password_label = Label(root, text="Password: ")
input_password = Entry(root, width=30)
input_password.grid(column=1, row=1, sticky=N+E+W+S, pady=10)
password_label.grid(column=0, row=1, sticky=N+E+W+S, pady=10)

def do():
    username = input_username.get()
    password = input_password.get()
    pool = ThreadPool(processes=1)
    pool_result = pool.apply_async(auto_e.run, (username, password))
    result = BooleanVar()
    result = pool_result.get()
    if result:
        msgbox.showinfo("성공", "영상 재생에 성공했습니다")
    else:
        msgbox.showerror("에러", "영상 재생 도중 에러가 발생했습니다.\n다시 시도해 보십시오")
        

btn1 = Button(root, width=20, height=2, text="Launch", command=do)
btn1.grid(column=0, row=2, columnspan=2, sticky=N+E+W+S)

root.mainloop()
