from cProfile import label
from tkinter import *

window=Tk()
calculater=""

num1=0
num2=0

buttons=[]
xb=50
yb=300

window.title("калькулятор")
window.geometry("500x500")
window.resizable(width=False,height=False)

frame= Frame(window,bg="lightgray")
frame.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.98)


label=Label(frame,text="0",font=10)
label.place(x=1,y=1,width=488)

def button(num):
    global calculater
    num=str(num)
    calculater+=num
    label.config(text=calculater)


for i in range(10):
    buttons.append(Button(frame,text=i,font=50))
    if i==0:
        buttons[0].place(x=175,y=425,width=100,height=50)
    else:
        buttons[i].place(x=xb,y=yb, width=100,height=50 )
        xb+=125
        if xb>300:
            yb-=125
            xb=50

for i in range(10):
    buttons[i].config(command=lambda i=i:button(i))


bPlus=Button(frame,text="+",font=50)
bPlus.place(x=425,y=50,width=50,height=100)

bMinus=Button(frame,text="-",font=50)
bMinus.place(x=425,y=160,width=50,height=100)

bYmno=Button(frame,text="*",font=50)
bYmno.place(x=425,y=270,width=50,height=100)

bDelenie=Button(frame,text="/",font=50)
bDelenie.place(x=425,y=380,width=50,height=100)

bravno=Button(frame,text="=",font=50)
bravno.place(x=300,y=425,width=100,height=50)










window.mainloop()