import pygame, sys, random
from pygame.locals import *

# установим pygame
pygame.init()
mainClock = pygame.time.Clock()

#настроим окно
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Обнаружение столкновений')

# настроим цвет
WHITE = (255,255,255)
BlACK = (0,0,0)
GREEN = (0,255,0)

# создадим структуру данных игрока и еды
foodCounter = 0
NEWFOOD= 40
FOODSIZE = 20
player = pygame.Rect(300,100,50,50)
foods = []
for i in range (20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH-FOODSIZE), random.randint(0, WINDOWHEIGHT-FOODSIZE), FOODSIZE, FOODSIZE))

# создадим переменные перемещения
moveleft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 4


# запуск игрового цикла
while True:
    # проверка события
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # изменение переменных клавиатуры
            if event.key == K_LEFT or event.key == K_a:
                moveRight = False
                moveleft = True
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = True
                moveleft = False
            if event.key == K_UP or event.key == K_w:
                moveUp = True
                moveDown = False
            if event.key == K_DOWN or event.key == K_s:
                moveUp = False
                moveDown = True
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_LEFT or event.key == K_a:
                    moveleft = False
                if event.key == K_RIGHT or event.key == K_d:
                    moveRight = False
                if event.key == K_UP or event.key == K_w:
                    moveUp = False
                if event.key == K_DOWN or event.key == K_s:
                    moveDown = False
                if event.key == K_x:
                    player.top = random.randint(0, WINDOWHEIGHT - player.height)
                    player.left = random.randint(0, WINDOWWIDTH - player.width)

            if event.type == MOUSEBUTTONUP:
                foods.append(pygame.Rect(event.pos[0], event.pos[1], FOODSIZE, FOODSIZE))

    foodCounter +=1
    if foodCounter>=NEWFOOD:
        # добавление новой еды
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH-FOODSIZE), random.randint(0, WINDOWHEIGHT-FOODSIZE), FOODSIZE, FOODSIZE))

        # создадим на поверхности белый фон
        windowSurface.fill(WHITE)

        # перемещение игрока
        if moveDown and player.bottom < WINDOWHEIGHT:
            player.top += MOVESPEED
        if moveUp and player.top > 0:
            player.top -= MOVESPEED
        if moveleft and player.left >0:
            player.left -= MOVESPEED
        if moveRight and player.right < WINDOWWIDTH:
            player.right += MOVESPEED

        # отображение игрока на поверхности
        pygame.draw.rect(windowSurface, BlACK, player)

        # проверим не пересекся ли игрок с каким-либо блоком еды
        for food in foods[:]:
            if player.colliderect(food):
                foods.remove(food)

        #отображение еды
        for i in range (len(foods)):
            pygame.draw.rect(windowSurface, GREEN, foods[i])

        # вывод на экран
        pygame.display.update()
        mainClock.tick(40)