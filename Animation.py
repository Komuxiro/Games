import pygame, sys, time
from pygame.locals import *

# установим pygame
pygame.init()

#настроим окно
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Анимация')

# создадим переменные направления
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESPEED = 4

# настроим цвет
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# создание структуры данных блока
b1 = {'rect': pygame.Rect(300,80,50,100), 'color': RED, 'dir':UPRIGHT}
b2 = {'rect': pygame.Rect(200,200,20,20), 'color': GREEN, 'dir':UPLEFT}
b3 = {'rect': pygame.Rect(100,150,60,60), 'color': BLUE, 'dir':DOWNLEFT}
boxes = [b1,b2,b3]

# запуск игрового цикла
while True:
    # проверим наличие события quit
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # создадим на поверхности белый фон
    windowSurface.fill(WHITE)

    for b in boxes:
        # перемещение структуры данных блока
        if b['dir'] == DOWNLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == DOWNRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == UPLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top -= MOVESPEED
        if b['dir'] == UPRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top -= MOVESPEED

    # проверим, переместился ли блок за пределы окна
        if b['rect'].top <0:
            # прохождение блока через верхнюю границу
            if b['dir'] == UPLEFT:
                b[dir] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b[dir] = DOWNRIGHT
        if b['rect'].bottom > WINDOWHEIGHT:
            # прохождение блока через нижнюю границу
            if b['dir'] == DOWNLEFT:
                b[dir] = UPLEFT
            if b['dir'] == DOWNRIGHT:
                b[dir] = UPRIGHT
        if b['rect'].left < 0:
            # прохождение блока чере левую границу
            if b['dir'] == DOWNLEFT:
                b[dir] = DOWNRIGHT
            if b['dir'] == UPLEFT:
                b[dir] = UPRIGHT
        if b['rect'].right > WINDOWWIDTH:
            # прохождение блока через правуюграницу
            if b['dir'] == DOWNRIGHT:
                b[dir] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b[dir] = UPLEFT

        # создание блока на поверхности
        pygame.draw.rect(windowSurface, b['color'], b['rect'])

    # вывод окна экрана
    pygame.display.update()
    time.sleep(0.02)