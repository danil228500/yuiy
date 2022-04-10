# это игра в стаканчики
import random,time
def myPred():
    print('''игрок решил посетить рынок зайдя на рынок. 
    он увидел человека за столом''')
    time.sleep(2)
    print('''на столе перед стояли три стаканчика. он показал маленький шарик
     и накрыл его стаканчиком''')
    time.sleep(2)

def myIst():
    print("""ведущий стал перемещять стаканчики по столу,
    произнося фразу кручу верчу запутать хочю""")
    time.sleep(2)
    print('''он резко остановился и предложил сыграть''')

def myGames():
    select = random.randint(1,3)
    print('''для выбора введите число
    "1","2" или "3"''')
    vybor = input()
    vybor = int(vybor)
    while vybor != 1 and vybor != 2 and vybor != 3:
        print('...')
        vybor = input()
    print('ведущий поднял стаканчик')
    if select == int(vybor):
        print('''улыбнулся "вы выйграли" ведуший''')
    else:
        print('''лукаво улыбнулся "вы проиграли" ведуший''')               

myPred()
doneGames = 'да'
while doneGames == 'да' or doneGames == 'д':
    myIst()
    myGames()
    print('хотите сыграть еще раз?')
    doneGames = input()
