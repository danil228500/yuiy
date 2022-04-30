k = input('введите кол. шариков')
k = int(k)
if k in (1,2,4,7):
    print('NO')
else:
    print('YES')
    myPred()
doneGames = 'да'
while doneGames == 'да' or doneGames == 'д':
    print('хотите сыграть еще раз?')
    doneGames = input()