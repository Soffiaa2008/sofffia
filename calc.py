from cProfile import label
from select import select
from tkinter import *

window=Tk()
calculater=""

num1=0
num2=0

selectPlus=False
selectMinus=False
selectYmno=False
selectDelenie=False
selectravno=False


def mathOperation(mode):
    global calculater,num1,num2,selectMinus,selectDelenie,selectPlus,selectravno,selectYmno
    if calculater =="":
        calculater=0
    num1=float(calculater)
    calculater=""
    label.config(text=calculater)

    if mode =="+":
        selectPlus=True 
    if mode =="-":
        selectMinus=True
    if mode =="/":
        selectDelenie=True 
    if mode =="*":
        selectYmno=True

def equals():
    global calculater,num1,num2,selectMinus,selectDelenie,selectPlus,selectravno,selectYmno
    num2=calculater
    num2=float(num2)
    if selectMinus:
        calculater=num1-num2
    elif selectPlus:
        calculater=num1+num2 
    elif selectDelenie:
        if num2 == 0:
            label.config(text="на ноль делить нельзя !!!")
            return
        else:
            calculater=num1/num2 
    elif selectYmno:
        calculater=num1*num2 


    label.config(text=calculater)

    selectPlus=False

def clear():
    global calculater,num1,num2
    calculater =""
    num1=0
    num2=0
    label.config(text=calculater)

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


bPlus=Button(frame,text="+",font=50,command=lambda: mathOperation("+"))
bPlus.place(x=425,y=50,width=50,height=100)

bMinus=Button(frame,text="-",font=50,command=lambda: mathOperation("-"))
bMinus.place(x=425,y=160,width=50,height=100)

bYmno=Button(frame,text="*",font=50,command=lambda :mathOperation("*"))
bYmno.place(x=425,y=270,width=50,height=100)

bDelenie=Button(frame,text="/",font=50,command=lambda :mathOperation("/"))
bDelenie.place(x=425,y=380,width=50,height=100)

bravno=Button(frame,text="=",font=50,command=equals)
bravno.place(x=300,y=425,width=100,height=50)

bclear=Button(frame,text="C",font=50,command=clear)
bclear.place(x=45,y=425,width=100,height=50)









window.mainloop()