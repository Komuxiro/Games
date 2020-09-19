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

def isOnCorner(x,y):
    # вернуть true если указанная позиция находится в одном из 4-х углов
    return (x==0 or x==WIDTH-1) and (y==0 or y==HEIGHT-1)

def getPlayerMove(board,playerTile):
    # позволить игроку ввести свой ход
    # вернуть вход в виде (x,y) (или вернуть строки 'подсказка' или 'выход')
    DIGITSIT08= '1 2 3 4 5 6 7 8'.split()
    while True:
        print('Укажите ход, текст "выход" для завершения игры или "подсказка" для вызова подсказки.')
            move = input().lower()
            if move== 'выход' or move == 'подсказка':
                return move

            if len(move) ==2 and move[0] in DIGITSIT08 and move[1 in DIGITSIT08]:
                x = int(move[0])-1
                y = int(move[1])-1
                if isValidMove(board,playerTile,x,y)==False:
                    continue
                else:
                    break
            else:
                print('Это недопустимый ход.Введите номер столбца (1-8) и номер ряда (1-8).')
                print('К примеру, значение 81 перемещает в верхний правый угол.')

        return [x,y]

def getCornerBestMove(board,computerTile):
    # учитывая данное игровое поле и данную фишку компьютера, определить
    # куда сделать ход и вернуть этот ход в виде списка [x,y]
    possibleMoves = getValidMoves(board, computerTile)
    random.shuffle(possibleMoves) # сделать случайным порядок ходов

    # всегда делать ход в угол, если это возможно
    for x,y in possibleMoves:
        if isOnCorner(x,y):
            return [x,y]

    # найти ход с наибольшим возможным количеством очков
    bestScore = -1
    for x,y in possibleMoves:
        boardCopy = getBoardCopy(board)
        makeMove(boardCopy,computerTile,x,y)
        score = getScoreOfBoard(boardCopy)[computerTile]
        if score > bestScore:
            bestMove = [x,y]
            bestScore = score
    return bestMove

def getWorstMove (board, tile):
    # вернуть ход, который переворачивает  меньше всего фишек
    possibleMoves = getValidMoves(board, tile)
    random.shuffle(possibleMoves)

# найти ход с наименьшим возможным количеством очков
    worstScore = 64
    for x,y in possibleMoves:
        boardCopy = getBoardCopy(board)
        makeMove(boardCopy, tile, x,y)
        score = getScoreOfBoard(boardCopy)[tile]
        if score < worstScore:
            worstScore = [x,y]
            worstScore = score

    return worstScore

def getRandomMove (board, tile):
    possibleMoves = getValidMoves(board, tile)
    return random.choice(possibleMoves)

def isOnSide (x,y):
    return  x==0 or x ==WIDTH -1 or y ==0 or y == HEIGHT-1

def getCornerSideBestMoves(board, tile):
    # вернуть угловой ход , граничный ход или лучший ход
    possibleMoves = getValidMoves(board, tile)
    random.shuffle(possibleMoves) # сделать случайным порядок ходов

    # вседа делать ход в угол, если это возможно
    for x,y in possibleMoves:
        if isOnCorner(x,y):
            return [x,y]

    # если сделать ход не получается, вернуть граничный ход
    for x,y in possibleMoves:
        if isOnCorner(x,y):
            return [x,y]

    return getCornerSideBestMoves(board,tile) #делть то что делал бы обычный ИИ

def printScore(board, playerTile, computerTile):


        if playerValidMoves == [] and computerValidMoves == []:
            return board # ходов нет ни у кого - закончить игру

        elif turn =='Человек': # ход человека
            if playerValidMoves != []:
                    #if showHints:
                    #    validMovesBoard = getBoardWithValidMoves(board, playerTile)
                    #    drawBoard(validMovesBoard)
                    #else:
                    #    drawBoard(board)
                    #printScore(board, playerTile, computerTile)

                    move = getCornerBestMove(board, playerTile)
                    #if move == 'выход':
                    #    print('Спасибо за игру')
                    #    sys.exit() # завершить работу программы
                    #elif move == 'подсказка':
                    #    showHints = not showHints
                    #    continue
                    #else:
                    makeMove(board, playerTile, move[0], move[1])
            turn = 'Компьютер'

        elif turn == 'Компьютер': # ход компьютера
            if computerValidMoves != []:
                #drawBoard(board)
                #printScore(board, playerTile, computerTile)

                #input('Нажмите клавишу Enter для просмотра хода компьютера.')
                move = getWorstMove(board, computerTile)
                makeMove(board, computerTile, move[0], move [1])
            turn = 'Человек'

NUM_GAMES = 250 # параметр определяет сколько партий будет сыграно
xWins = oWins = ties = 0 #  переменные отслеживают победы и ничьи
print('Привестствуем в игре "Реверси"!')

playerTile, computerTile = ['X', 'O'] #enterPlayerTile()

for i in range(NUM_GAMES): #while True:
    finalBoard = playGame(playerTile, computerTile)

    #отобразить итоговый счет
    #drawBoard(finalBoard)
    scores = getScoreOfBoard(finalBoard)
    print('#%s: X набрал %s очков. O набрал %s очков' % (i + 1, scores['X'], scores['O']))
    if scores [playerTile] > scores [computerTile]:
        xWins+=1 #print('Вы победили компьютер, обогнав его на %s очков.' % (scores[playerTile] - scores[computerTile]))
    elif scores[playerTile] < scores[computerTile]:
        oWins+=1 #print('Вы проиграли. Компьюетр победил вас, обогнав на %s очков.' % (scores[computerTile] - scores[playerTile]))
    else:
        ties +=1 #print('Ничья')

    #print('Хотите сыграть еще раз? (да или нет)')
    #if not input().lower().startswith('д'):
        #break
print('Количество выиграшей X: %s (%s%%)' %(xWins, round(xWins/NUM_GAMES *100, 1))) # вывод процента побед
print('Количество выиграшей O: %s (%s%%)' %(oWins, round(oWins/NUM_GAMES *100, 1)))
print('Количество выиграшей: %s (%s%%)' %(ties, round(ties/NUM_GAMES *100, 1)))