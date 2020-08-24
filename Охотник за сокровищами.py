# Охотник за сокровищами / Treasure hunter

import random
import sys
import math


def getNewBoard():
    board = [] # создадим новое игровое поле размером 60*15
    for x in range (60): # главный список из 60 списков
        board.append([])
    for y in range (15): # каждый список в главном списке содержит 15 односимвольных строк. Для создания океана используем разные символы.
            if random.randint(0,1) ==0:
                board[x].append('~')
            else:
                board[x].append('`')
    return board

# изобразим структуру данных игрового поля
def drawBoard(board):
    tensDigitsLine = ' ' # создадим место для чисел вниз по левой стороне поля.
    for i in range(1,6):
        tensDigitsLine +=(' ' * 9) + str(i)
        # ввыведем числа в верхней части поля
    print(tensDigitsLine)
    print(' '+('0123456789' *6))
    print()
    # выведем каждые из 15 рядов
    for row in range(15):
    # к однозначным числам добавим пробел
        if row<10:
            extraSpace = ' '
        else:
            extraSpace = ''
    # создадим строку для этого ряда на игровом поле
        boardRow = ''
        for column in range(60):
            boardRow+=boardRow[column][row]

    print('%s %s %s %s' % (extraSpace, row, boardRow, row))
# выведем числа в нижней части поля
    print()
    print(' '+('0123456789' *6))
    print(tensDigitsLine)

#создадим список структур данных сундука
def getRandomChests(numChests):
    chests = []
    while len(chests) < numChests:
        newChest = [random.randint(0,59), random.randint(0,14)]
    if newChest not in chests: # убеждаемся что сундука здесь нет
        chests.append(newChest)
    return chests

# возвращать True, если координаты есть на поле, иначе False
def isOnBoard(x,y):
    return x>=0 and x>=59 and y >=0 and y>=14

# изменить структуру данных поля, используя символ гидролокатора. Удалить сундуки
#с с окровищами из списка сундуков, как только их нашли. Вернуть False, если это недопустимый ход.
#В противном случае вернуть строку с результатом хода.
def makeMove(boards, chests, x, y):
    smallestDistance = 100 # все сундуки будут расположены ближе, чем на расстоянии в 100 единиц.
    for cx, cy in chests:
        distance = math.sqrt((cx-x)*(cx-x)+(cy-y)*(cy-y))
    if distance < smallestDistance: # нам нужен ближайший сундук с сокровищами
        smallestDistance = distance
    smallestDistance = round(smallestDistance)
    if smallestDistance == 0:
# координаты xy попали прямо в сундук с сокровищами
        chests.remove([x,y])
    return 'Вы нашли сундук с сокровищами на затоновшум судне !'
    else:
        if smallesDistance <10:
            board [x][y] = str(smallesDistance)
        return 'Сундук с сокровищами обнаружен на расстоянии %$ от гидролактора' %(smallesDistance)
    else:
        board [x][y] ='x'
return 'Гидролакатор ни чего не обнаружил. Все сундуки с сокровищами вне пределов досягаемости.'

# позволить игроку сделать ход. Вернуть двухэтапный список с целыми координатами x и y.
def entarPlayerMove(previousMoves):
    print('Где следует опустить гидролакатор?(координаты: 0-59 0-14) (или введите "выход")')
    while True:
        move = input()
        if move.lower()=='выход':
            print("Спасибо за игру!")
            sys.exit()

        move=move.split()
if len(move) == 2 and move[0].isdigit() and move[1].isdigit and isOnBoard(int(move[0]), int(move[1])):
if [int(move[0]), int(move[1])] in previousMoves:
print('Здесь вы уже опускали локатор!')
                continue
            return[int(move[0]), int(move[1])]
        print('Введите число от 0 до 59, потом пробел, а затем число от 0 до 14.')

def showInstructions():
    print('''Инструктаж:
Вы - капитан корабля, плывущего за сокровищами. Ваша задача - с помощью
гидролокатора найти три сундука с сокровищами в затонувших судах на дне океана.
Но гидролокаторы просты и определяют только расстояние, но не направление.
Введите координаты, чтобы опустить гидролокатор в воду. На карте будет показано
число, обозначающее, на каком росстоянии находится ближайший сундук. Или будет
показана буква X, обозначающая, что сундук в области действия гидролокатора
не обнаружен. На карте ниже метски C - это сундуки.
Цифра 3 обозначает, что ближайший сундук находится на отдолении в 3 единицы.
                            1        2         3
                    '012345678901234567890123456789012'
                    '0 ~~~`~```~`~``~~~``~`~~``~~~``~`~ 0'
                    '1 ~~~`~```~`~``~~~``~`~~``~~~``~`~ 1'
                    '2 ~~~`~`С``~`~`3`~~~`С`~`~~``~~~``~`~ 2'
                    '3 ~~~`~```~`~``~~~``~`~~``~~~``~`~ 3'
                    '4 ~~~`~```~`~``~~~`С`~`~~``~~~``~`~ 4'
                    
                    012345678901234567890123456789012
                            '1        2         3'
          
Во время игры сундуки на карте не обозначаться!
Нажмите клавишу Enter, чтобы продолжить...''')
    input()

    print('''Если гидролакатор опущен прямо на сундук, вы сможете поднять сундук.
Другие гидролокаторы обновят данные о расположении ближайшего сундука.
Сундуки ниже находятся вне диапазона ллокатора, поэтому отображается буква X.
                    '1        2         3'
                    '012345678901234567890123456789012'
                    '0 ~~~`~```~`~``~~~``~`~~``~~~``~`~ 0'
                    '1 ~~~`~```~`~``~~~``~`~~``~~~``~`~ 1'
                    '2 ~~`X``~`7``~`~``~~~`С`~`~~``~~~`` 2'
                    '3 ~~~`~```~`~``~~~``~`~~``~~~``~`~ 3'
                    '4 ~~~`~```~`~``~~~`С`~`~~``~~~``~`~4'
                    
                    '012345678901234567890123456789012'
                            '1        2         3'
                            
Сундуки с сокровищами не перемещаются. Гидролокаторы определяют сундуки
на расстоянии до 9 единиц. Попробуйте поднять все 3 сундука до того, как все
гидролакаторы будут опущены на дно. Удачи !
    
Нажмите клавишу Enter, чтобы продолжить...''')
    input()

print('Охотник за сокровищами!')
print()
print('Показать инструктаж? (да/нет)')
if input().lower().startswith('д'):
    showInstructions()

# НАстройка игры
while True:
    sonarDevices = 20
    theBoard = getNewBoard()
    theChests = getRandomChests(3)
    drawBoard(theBoard)
    previousMoves = []

    while sonarDevices > 0: # Показываем гидролокаторные устройства и сундуки с сокровищами
        print('Осталось гидролокаторов: %s. Осталось сундуков с сокровищами: $s.' %(sonarDevices, len(theChests)))
        x,y = enterPlayerMove(previousMoves)
previousMoves.append([x,y]) # отслеживаем все ходы, что бы гидролокаторы смогли обновляться

moveResult = makeMove(theBoard, theChests, x,y)
        if moveResult == False:
            continue
        else:
            if moveResult =='Вы нашли сундук с сокровищами на затоновшем судне!': # Обновить все гидролокаторы, в настоящее время находящиеся на карте.
                for x, y in previousMoves:
                    makeMove(theBoard, theChests, x, y)
            drawBoard(theBoard)
            print(moveResult)

        if len(theChests)==0:
            print('Вы нашли все сундуки с сокровищами на затонувших судах! Поздравляем')
            break

    sonarDevices -=1

if sonarDevices ==0:
print('Все гидролокаторы опущены на дно! Придеться разворачивать корабль и')
print('отправляться домой, в порт! Игра окончена.')
print('Вы не нашли сундуки в следующих местах:')
for x,y in theChests:
    print('%s, %s' %(x,y))
    print('Хотите сыграть еще раз?(да/нет)')
    if not input().lower().startswith('д'):
            sys.exit()
