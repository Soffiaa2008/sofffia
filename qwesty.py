

health=100
exp=0
food_surply=50
energy=50

notes=[]


def henting():
    global exp,food_surply,energy
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



while True:
    print("------список действий------")
    print("1.охотиться")
    print("2.спать ")
    print("3.поесть")
    print("4.написать заметку ")

    activion=input("напиши номер действия->")
    if activion=="1":
        henting()
    elif activion=="2":
        relax()
    elif activion=="3":
        food()
    elif activion=="4":
        writeNote()
    
    print("\n\n")

    print("здоровье->"+str(health))
    print("энерия->"+str(energy))
    print("опыт->"+str(exp))
    print("eда->"+str(food_surply))

    print("\n\n")