
from time import sleep


while True:
    name=input("введите ваше имя->")
    age=input("введите ваш возраст->")
    scores=0




    print("-------------------------------")
    print("карточка участника")
    print("имя-"+name)
    print("возраст-"+age)
    print("----------------------------")


    print("вопрос 1: сколько будет 2+5*6?")
    v1=int(input("ответ---->"))

    while True:
        if v1==32:
            print("это верно")
            scores+=5
            break
        else:
            print("неверно")
            scores-=5
            v1=int(input("ответ---->"))


    print("----------------------------")
    print("вопрос 2: в каком округе находится москва")
    v2=input("ответ---->")

    while True:
        if v2.lower() =="центральном":
            print("это верно")
            scores+=5
            break
        else:
            print("неверно")
            scores-=5
            v2=(input("ответ---->"))


    print("----------------------------")
    print("вопрос 3:какое самое глубокое озеро?")
    v3=input("ответ---->")

    while True:
        if v3.lower()=="байкал":
            print("это верно")
            scores+=5
            break
        else:
            print("неверно")
            scores-=5
            v3=input("ответ---->")

    print("----------------------------")
    print("вопрос 3:как пишется основная команда(p****)?")
    v4=input("ответ---->")

    while True:
        if v4=="print":
            print("это верно")
            scores+=5
            break
        else:
            print("неверно")
            scores-=5
            v4=input("ответ---->")

    print("----------------------------")
    print("вопрос 5:как пишется команда цыкла?w****")
    v5=input("ответ---->")

    while True:
        if v5=="while":
            print("это верно")
            scores+=5
            break
        else:
            print("неверно")
            scores-=5
            v5=input("ответ---->")


    print("----------------------------")
    print ("вопрос 6:как переводится команда while")
    v6=input("ответ---->")

    while True:
        if v6.lower()=="пока":
            print("это верно")
            scores+=15
            break
        else:
            print("неверно")
            scores-=15
            v6=input("ответ---->")



    print("----------------------------")
    print ("вопрос 7:как пишется команда цыкла?")
    v7=input("ответ---->")

    while True:
        if v7=="for":
            print("это верно")
            scores+=15
            break
        else:
            print("неверно")
            scores-=15
            v7=input("ответ---->")



    print("----------------------------")
    print ("вопрос 8.какими полезными ископаемыми богата болотистая местность?")
    v8=input("ответ---->")

    while True:
        if v8.lower()=="торф":
            print("это верно")
            scores+=5
            break
        else:
            print("неверно")
            scores-=5
            v5=input("ответ---->")


    print("----------------------------")
    print ("вопрос 9.каков будет вывод в консоль:for i in range(1,10,2)?")
    print("----------------------------")
    print("1)1,3,5,7,9,11")
    print("2)1,3,5,7,9")
    print("3)1,3,4,5,7,9")
    print("4)3,5,7,9,11")
    v9=int(input("ответ---->"))

    while True:
        if v9==2:
            print("это верно")
            scores+=15
            break
        else:
            print("неверно")
            scores-=15
            v5=input("ответ---->")






    print("---------------------")
    print("Спасибо что прошел викторину!")
    print(name+" набрал очков-"+str(scores))
    print("---------------------")

    v_reset=input("хочешь еще раз пройти мою викторину?")


    if v_reset.lower()=="да":
        print("окей:) давай начнём сначала !!!")
        sleep(1)
    elif v_reset.lower()=="нет":
        print("окей:) ждём тебя снова")
        break

    print("---------------------")






