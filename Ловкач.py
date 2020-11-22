import  pygame, random, sys
from pygame.locals import *

WINDOWWIDTH = 600
WINDOWHEIGTH = 600
TEXTCOLOR = (0,0,0)
BACKGROUNDCOLOR = (255,255,255)
FPS = 60
BADDIEMINSIZE = 10
BADDIEMAXSIZE = 40
BADDIEMINSPEED = 1
BADDIEMAXSPEED = 8
ADDNEWBADDIERATE = 6
PLAYERMOVERATE = 5

def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # нажатие эскейп осуществляет выход
                    terminate()
                return

def playerHasHitBaddie(playerRect, baddies):
    for b in baddies:
        if playerRect.colliderect(b['rect']):
            return  True
    return False

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# настройки pygame окна и указателя мыши
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGTH))
pygame.display.set_caption('Ловкач')
pygame.mouse.set_visible(False)

# настройка шрифтов
font = pygame.font.SysFont(None, 35)

#настройка звуков
gameOverSound = pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('background.mid')

#настройка изображений
playerImage = pygame.image.load('player.png')
playerRect =playerImage.get_rect()
baddieImage = pygame.image.load('baddie.png')

# вывод начального экрана
windowSurface.fill(BACKGROUNDCOLOR)
drawText('Ловкач', font, windowSurface,(WINDOWWIDTH/3), (WINDOWHEIGTH/3))
drawText('Нажмите клавиатуру для начала игры', font, windowSurface, (WINDOWWIDTH/5)-30, (WINDOWHEIGTH/3)+50)
pygame.display.update()
waitForPlayerToPressKey()

topScore = 0
while True:
    #Настройка начала игры
    baddies = []
    score = 0
    playerRect.topleft = (WINDOWWIDTH/0, WINDOWHEIGTH-50)
    moveLeft = moveRight = moveUp = moveDown = False
    reversCheat = slowCheat = False
    baddieAddCounter = 0
    pygame.mixer.music.play(-1,0.0)

    while True: #игровой цикл выполняется пока игра работает
        score += 1 # увеличение колличества очков

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

