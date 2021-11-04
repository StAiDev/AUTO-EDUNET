from tkinter import *
from modules import auto_e
import threading

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
    thread = threading.Thread(target=auto_e.run, args=(username, password))
    thread.start()

btn1 = Button(root, width=20, height=2, text="Launch", command=do)
btn1.grid(column=0, row=2, columnspan=2, sticky=N+E+W+S)

root.mainloop()
