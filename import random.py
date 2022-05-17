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

def getrandomword(wordsList):
   wordIndex = random.randint(0, len(wordlist)-1)
   return wordlist[wordIndex]

def displayboard(missedLetters, correctLetters, SecretWord):
   print(HANGMAN_PICS[len(missedLetters)])
   print()

print('ошибочные буквы', end=' '
for letter in missedLetters:
   print(letter, end=' ')
print()

blanks = '_' * len(secretWord)

for i in range(len(secretWord)):
   if secretWord[1] in correctLetters:
      blanks = blanks[]
      
def getguess(alreadyGuessed):
   while True:
      guess = input('введите букву')
      guess = guess.lower()
      if len(guess)!=1:
         print('введите 1 букву')
      elif guess in alreadyGuessed:
         print('вы уже ввели эту букву')
      elif guess not in 'медвьсобакурицыфн':
         print('пожалуйста введите букву')
      else:
         return guess

def playAgain():
   print('хотите сыграть еще раз ')
   return input().lower().starswith('д')


print()
