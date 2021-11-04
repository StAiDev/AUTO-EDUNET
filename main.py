from tkinter import *
from modules import auto_e
import threading

root = Tk()
root.title("Auto Edunet")
root.geometry("480x640")
root.resizable(False, False)
root.iconbitmap("resources/edunet.ico")


input_username = Entry(root, width=30)
input_username.pack()

input_password = Entry(root, width=30)
input_password.pack()

def do():
    username = input_username.get()
    password = input_password.get()
    thread = threading.Thread(target=auto_e.run, args=(username, password))
    thread.start()

btn1 = Button(root, width=20, height=2, text="Launch", command=do)
btn1.pack()

root.mainloop()
