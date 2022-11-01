
from random import randint

health=100
exp=0
food_surply=50
energy=50

notes=[]


def henting():
    global exp,food_surply,energy,health
    r=randint(1,15)
        
    if energy <= 20:
        print("силы тебя покидают!!!")
        return
    
    
    if food_surply > 975:
        print("слижком много еды,ты это не унесёшь")
        return
    
    
    if r==2:
        print("я не смог поохотиться,на меня напали волки")
        health-=20
        energy-=10
        exp+=15
        food_surply-=10
    elif r==3:
        print("я никого не нашел,придется питаться ягодами")
        exp+=3
        health+=15
        food_surply+=10
    elif r==4:
        print("я нашел чей-то сухпаёк,он был свежий")
        exp+=30
        food_surply+=55
        energy+=10
    else:
        exp +=50
        food_surply+=25
        energy-=20
        print("me->Хорошо поохотился!")


def relax():
    global exp,health,energy
    energy+=50
    exp=100
    health=100
    print("me->я так выспался:)")

def food():
    global exp,energy,food_surply
    food_surply-=30
    energy+=30
    exp+=10
    print("me->я наелся:)")


def writeNote():
    global exp 
    exp+=10
    print("что будем писать?")
    ans=input("ответ->")
    notes.append(ans)
    print("я: записал!")

def readNotes():
    print
    print("записи-")
    for n in notes:
        print(n)

def stroll():
    global exp,energy,food_surply,health
    r=randint(1,5)
    if energy <=30 :
        print("тебе нужно отдохнуть,твои силы иссякли")
        return
    
    if health > 85:
        print("слишком много здоровья ")
        return
    exp+=10
    if r==1:
        print("я-> на меня напали разбойники :(")
        energy-=30
        if food_surply<=1000:food_surply-=20
        health-=20
    elif r==2:
        print("ого-го, сколько тут еды:0")
        food_surply+=50
        health+=15
        energy-=20
    elif r==3:
        print("на меня напали,но я не упал духом и выйграл эту схватку!!!")
        food_surply+=30
        energy-=20
    else:
        print("я->я погулял отлично")
        energy-=20
        health+=15

while True:
    print("------список действий------")
    print("1.охотиться")
    print("2.спать ")
    print("3.поесть")
    print("4.написать заметку ")
    print("5 .прочитать заметку")
    print("6 .пойти погулять")

    activion=input("напиши номер действия->")
    if activion=="1":
        henting()
    elif activion=="2":
        relax()
    elif activion=="3":
        food()
    elif activion=="4":
        writeNote()   
    elif activion=="5":
        readNotes()
    elif activion=="6":
        stroll()
    else:
        print("\n ввидите другое число")

    if health>100:
         health=100
         print("я себя чувствую очень хорошо!!!")
    if energy>100: energy=100       
    
    
    print("\n\n")

    print("здоровье->"+str(health))
    print("энерия->"+str(energy))
    print("опыт->"+str(exp))
    print("eда->"+str(food_surply))
    
    if health <=0:
        print("игра оконченна:(((")
        break
    
    print("\n\n")






























