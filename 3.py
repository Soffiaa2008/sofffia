
from tkinter import*
from tkinter import messagebox
import random

def no():
    messagebox.showinfo("","так и знал")
    quit()

def motionMouse(event):
    btnn.place(x=random.randint(0, 500), y=random.randint(0,500))

root=Tk()
root.geometry("600x600")
root.title("опрос")
root.resizable(width=False,height=False)
root["bg"] = "white"
label= Label(root,text="0:?", font="Arial 20 bold", bg="white").pack()
btnn=Button(root,text="нет",font="Arial 20 bold",bg="white")
btnn.place(x=170,y=100)
btnn.bind("<Enter>",motionMouse)
btnn= Button(root,text="да",font="Arial 20 bold",command=no).place(x=350,y=100)

root.mainloop()














































































































































#mihail=13
#koly=13
#if mihail>koly:
    #print("Михаил")
#elif mihail<koly:
    #print("Коля")
#elif mihail==koly:
    #print("Михаил и Коля")