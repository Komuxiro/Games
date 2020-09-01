# Крестики- нолики / Tic Tac Toe
import random


# создадим игровое поле
def drawBoard(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


# разрешаем игроку ввести букву, которую он выбирает.
# возвращаем список, в котором буква игрока - первый элемент, а буква компа - второй
def inputPlaterLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Вы выбираете X или O?')
        letter = input().upper()

    # первый элемент списка - буква игрока, второй элемент - компьютера
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


# случайный выбор игрока который ходит первым
def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'Компьютер'
    else:
        return 'Человек'


def makeMove(board, letter, move):
    board[move] = letter


# Учитывая заполнение игрового поля и буквы игрока, функция вернет True, если игрок выйграл
# используем сокращенния 'bo'/'le' вместо 'board'/'letter'
def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # через верх
            (bo[4] == le and bo[5] == le and bo[5] == le) or  # через центр
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # через низ
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # вниз по левой стороне
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # вниз по центру
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # вниз по правой стороне
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # по диагонали
            (bo[9] == le and bo[5] == le and bo[1] == le))  # по диагонали


# Создадим копию игрового поля и вернем его
def getBoardCopy(board):
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy


# вернем true, если сделан ход в свободную клетку
def isSpaceFree(board, move):
    return board, move == ' '


# разрешаем игроку сделать ход
def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('Ваш следующий ход. (1-9)')
        move = input()
    return int(move)


# возвращаем допустимый ход, учитывая список сделанных ходов и список заполненных клеток
# возвращает значение None если больше нет допустимых ходов
def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


# учитываем заполнение игрового поля и букву компьютера, определяем допустимый ход и возвращаем его
def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # алгоритм для ИИ, сначала проверяем - победи ли мы, сделав следующий ход
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    # проверяем - победит ли игрок сделав следующий ход и блокируем его
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    # пробуем занять один из углов если есть свободные
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # пробуем занять центр, если он свободен
    if isSpaceFree(board, 5):
        return 5

    # делаем ход по одной стороне
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


# возвращаем true, если клекта на игровом поле занята, в противном случае false
def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print('Игра "Крестики-нолики"')

# перезагрузка игрового поля
while True:
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlaterLetter()
    turn = whoGoesFirst()
    print('' + turn + ' ходит первым.')
    gameIsPlaying = True
    while gameIsPlaying:
        if turn == 'Человек':
            # ходит игрок
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Ура! Вы выиграли')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Ничья')
                else:
                    turn = 'Компьютер'
        else:  # ход компьютера
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('Компьютер победил! Вы проиграли')
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Ничья')
                    break
                else:
                    turn = 'Человек'
    print('Сыграем еще раз? (да или нет)')
    if not input().lower().startswith('д'):
        break
