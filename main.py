from tkinter import *
import modules.auto_e

root = Tk()
root.title("Auto Edunet")
root.geometry("480x640")
root.resizable(False, False)


def do(userid, password):
    modules.auto_e.run(userid, password)


f = open("login.txt")
userid = f.readline()
password = f.readline()

btn1 = Button(root, width=20, height=2, text="Launch", command=do(userid, password))
btn1.pack()

root.mainloop()
