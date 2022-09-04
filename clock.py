from tkinter import *
from time import strftime
#from tkinter.ttk import *
root = Tk()
root.title("Clock")
label= Label(root,font=('ds_digital',80),background="black",foreground='lightpink')
label.pack(anchor="center")
def fetchtime():
    t=strftime('%H:%M:%S %p')
    label.config(text=t)
    label.after(1000,fetchtime)


fetchtime()
root.mainloop()
