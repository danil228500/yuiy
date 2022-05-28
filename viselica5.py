import random
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''','''
  +---+
  0   |
      |
      |
     ===''','''
  +---+
  0   |
  |   |
      |
     ===''','''
  +---+
  0   |
 /|   |
      |
     ===''','''
  +---+
  0   |
 /|\  |
      |
     ===''','''
  +---+
  0   |
 /|\  |
 /    |
     ===''','''
  +---+
  0   |
 /|\  |
 / \  |
     ===''','''
  +---+
  0]  |
 /|\  |
 / \  |
     ===''','''
  +---+
 [0]  |
 /|\  |
 / \  |
     ===''','''
  +---+
 [0]  |
 /|\] |
 / \  |
     ===''','''
  +---+
 [0]  |
[/|\] |
 / \  |
     ===''']
words = {'животные':'медведь собака курица рыба кобра феникс'.split(),
         'обьекты':'фонарь ноутбук пистолет робот деньги лазер машина гантеля читы'.split(),
         'еда':'чебупель шаурма дошик бэпешка шоколадка арбуз абобус суп человек таракан'.split()}

def vyborSlova(slovo):
    # вЫБИРАЕМ слово
    sicretS = random.choice(list(slovo.keys()))

    IndexS = random.randint(0,len(slovo)-1)
    return [slovo[sicretS][IndexS],sicretS]

def kartina(errorS,yesS,secretS,hm):
    print(hm[len(errorS)])
    print()

    print('ошибочные буквы',end=' ')
    for letter in errorS:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretS)
    
    for i in range(len(secretS)):
        if secretS[i] in yesS:
            blanks = blanks[0:i] + secretS[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')
            
    print()

def getguess(alreadyGuessed):
   while True:
      guess = input('введите букву')
      guess = guess.lower()
      if len(guess)!=1:
         print('введите 1 букву')
      elif guess in alreadyGuessed:
         print('вы уже ввели эту букву')
      elif guess not in 'абвгдежзийклмнопрсутфхцчшщъыьэюя':
         print('пожалуйста введите букву')
      else:
         return guess
def playagain():
    print('хотите играть еще?')
    while True:
        otvet = input().lower()
        if (otvet == 'да') or (otvet == 'д') or (otvet == 'yes') or (otvet == 'y'):
            return True
        elif (otvet == 'нет') or (otvet == 'н') or (otvet == 'no') or (otvet == 'n'):
            return False
        else:
            print('я вас не понял введите другую букву!')

def vybrsloznasti():
    print('ведите "Л" чтобы выбрать легкую сложнасть')
    print('введите "С" чтобы выбрать среднию сложнасть')
    print('введите "Т" чтобы выбрать тяжолую сложнасть')
    while True:
        us =input().upper()
        print(us)
        if len(us) != 1:
            print('введите только одну букву')
        elif us not in 'ЛСТ':
            print('введите л с или т')
        else:
            return us

def delV(urovenS,hangP):
    if urovenS == 'С':
        del hangP[10]
        del hangP[9]
    elif urovenS == 'Т':
        del hangP[10]
        del hangP[9]
        del hangP[8]
        del hangP[7]

hm = HANGMAN_PICS

bs = vybrsloznasti()
delV(bs,hm)


        
errorG = ''
yesG = ''
gameOver=False
sicretS,sS = vyborSlova(words)

while True:
    print(bs)
    if bs == 'Л':
        print('категория: '+sS)
    kartina(errorG,yesG,sicretS,hm)

    bukva = getguess(errorG+yesG)

    if bukva in sicretS:
        yesG = yesG + bukva

        win = True
        for i in range(len(sicretS)):
            if sicretS[i] not in yesG:
                win = False
                break
        if win:
            kp = errorG+yesG
            print('Поздравляю ты отгодал слово - "'+sicretS+'"! вы угадали за '+str(len(kp))+' количество шагов.')
            gameOver=True        
    else:
        errorG = errorG + bukva
        
        if len(errorG) == len(HANGMAN_PICS) - 1:
            kartina(errorG,yesG,sicretS,hm)
            print('вы исчерпали все попытки\nнеугадоно букв:'+str(len(errorG))+'\nи угадоно букв:'+str(len(yesG))+'\nсекретное слово было:'+sicretS)
            gameOver = True

    if gameOver:
        if playagain():
            hm = HANGMAN_PICS

            bs = vybrsloznasti()
            delV(bs,hm)

            errorG = ''
            yesG = ''
            gameOver=False
            sicretS,sS = vyborSlova(words)
        else:
            break