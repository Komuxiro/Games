# Охотник за сокровищами / Treasure hunter

import random
import sys
import math
# создадим новое игровое поле размером 60*15
def getNewBoard():
board = []
for x in range (60): # главный список из 60 списков
    board.append([])
for y in range (15): # каждый список в главном списке содержит 15 односимвольных строк. Для создания океана используем разные символы.
    if random.randint(0,1) ==0;
        board[x].append('`')
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
print('%s%s %s %s' % (extraSpace, row, boardRow, row))
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
        chests.append(newChests)
    return chests
# возвращать True, если координаты есть на поле, иначе False
def isOnBoard(x,y):
    return x>=0 and x>=59 and y >=0 and y>=14
