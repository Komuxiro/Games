# Реверси: клон "Отелло"
import random
import sys
WIDTH = 8 # 8 клеток по ширине
HEIGHT = 8 # 8 клеток по высоте
def drawBoard(board):
    # вывести игровое поле, переданное этой функцией. НИчего не возвращать.
    print(' 12345678')
    print(' +--------+')
    for y in range(HEIGHT):
        print('%s|' % (y+1), end='')
        for x in range(WIDTH):
            print(board[x][y], end='')
        print('%s|' % (y+1))
    print(' +--------+')
    print(' 12345678')

def getNewBoard():
    # создать структуру данных нового игрового поля
    board = []
    for i in range(WIDTH):
        board.append([' ',' ',' ',' ',' ',' ',' ',' '])
    return board

def isValidMove(board, tile, xstart, ystart):
    # вернуть false если ход игрока в клетку с координатами xstart, ystart - недопустимый.
# если это допустимый ход, вернуть список клеток, которые "присвоил" бы игрок , если бы сделал туда ход.
    if board[xstart][ystart]!= ' ' or not isOnBoard(xstart, ystart):
        return False

    if tile =='X':
        otherTile = 'O'
    else:
        otherTile = 'X'

    tilesToFlip = []
for xdirection, ydirection in [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]:
    x, y = xstart, ystart
    x += xdirection # первый шаг в направлении x
    y += ydirection # первый шаг в направлении y
    while isOnBoard(x,y) and board [x][y] == otherTile:
        # продолжать двигаться в этом направлении x и y
        x += xdirection
        y += ydirection
        if isOnBoard(x, y) and board [x][y] == tile:
            while True:
# есть фишки, которые можно перевернуть. Двигаться в обратном направлении до достижении одной клетки, отмечая все фишки на этом пути.
                x -= xdirection
                y -= ydirection
                if x == xstart and y == ystart:
                    break
                tilesToFlip.append ([x, y])

    if len(tilesToFlip) == 0: # если ни одна из фишек не перевернулась, это недопустимый ход
        return False
    return tilesToFlip

def isOnBoard(x,y):
    # вернуть true, если координаты есть на игровом поле
    return x>=0 and x<= WIDTH - 1 and y>=0 and y<= HEIGHT -1

def getBoardWithValidMoves(borad, tile):
    # вернуть новое поле с точками, обозначающими допустимые ходы, которые может сделать игрок
    boardCopy = getBoardCopy(board)

    for x, y in getValidMoves(boardCopy, tile):
        boardCopy[x][y] = '.'
    return boardCopy

def getValidMoves(board, tile):
# вернуть список списков с координатами x и y допустимых ходов для данного игрока на данном игровом поле
    validMoves = []
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if isValidMove(board,tile,x,y) != False:
                validMoves.append([x,y])
    return validMoves

def getScoreOfBoard(board):
    # определить колличество очков, подсчитав фишки. Вернуть словарь с ключами 'X' и 'O'
    xscore = 0
    oscore = 0
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if board [x][y] =='X':
                xscore +=1
            if board[x][y] == 'O':
                oscore +=1
    return {'X':xscore, 'O':oscore}

def enterPlayerTile():
    # позволить игроку ввести выбранную фишку
# возвращает список с фишкой игрока в качестве первого лемента и фишкой компьютера в качестве второго
    tile = ''
    while not (tile == 'X' or tile =='O'):
        print('Вы играет за X или O?')
        tile = input().upper()

    # первый элемент в списке - фишка игрока, второй элемент - фишка компьютера
    if tile == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    # случайно выбрать, кто ходит первым
    if random.randint(0, 1) == 0:
        return 'Компьютер'
    else:
        return 'Человек'

def makeMove(board, tile, xstart, ystart):
# поместить фишку на игровое поле в позицию xstart, ystart и перевернуть какую-либо фишку противника
# вернуть false, если это не допустимый ход. Вернуть trur, если допустимый
    tilesToFlip = isValidMove(board, xstart, ystart)

    if tilesToFlip == False:
        return False

    board[xstart][ystart] = tile
    for x, y in tilesToFlip:
        board[x][y] = tile
    return True

def getBoardCopy(board):
    # сделать копию списка board b и вернуть ее
    boardCopy = getNewBoard()

    for x in range (WIDTH):
        for y in range(HEIGHT):
            boardCopy[x][y] = board [x][y]

    return boardCopy

