from tkinter import *
from modules import auto_e
root = Tk()
root.title("Auto Edunet")
root.geometry("480x640")
root.resizable(False, False)

input_username = Entry(root, width=30)
input_username.pack()

input_password = Entry(root, width=30)
input_password.pack()

def do():
    username = input_username.get()
    password = input_password.get()
    auto_e.run(username, password)

btn1 = Button(root, width=20, height=2, text="Launch", command=do)
btn1.pack()

root.mainloop()
