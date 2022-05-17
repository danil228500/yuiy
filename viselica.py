from operator import truediv
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
     ===''']
words = 'медведь собака курица рыба фонарь кобра'.split()

def vyborSlova(slovo):
    # вЫБИРАЕМ слово
    IndexS = random.randint(0,len(slovo)-1)
    return slovo[IndexS]

def kartina(errorS,yesS,secretS):
    print(HANGMAN_PICS[len(errorS)])
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

errorG = ''
yesG = ''
gameOver=False
sicretS = vyborSlova(words)

while   True:
    kartina(errorG,yesG,sicretS)

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
            kartina(errorG,yesG,sicretS)
            print('вы исчерпали все попытки\nнеугадоно букв:'+str(len(errorG))+'\nи угадоно букв:'+str(len(yesG))+'\nсекретное слово было:'+sicretS)
            gameOver = True

    if gameOver:
        if playagain():
            errorG = ''
            yesG = ''
            gameOver=False
            sicretS = vyborSlova(words)
        else:
            break       
