import pygame
import sys
from pygame.locals import *

# инициализация pygame
pygame.init()

# настройка окна
windowsSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Приветы')

# назначение цветов
BlACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# назначение шрифтов
basicFont = pygame.font.SysFont(None, 48)

# настройка текста
text = basicFont.render('Привет Машка', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowsSurface.get_rect().centerx
textRect.centery = windowsSurface.get_rect().centery

# нанесение на поверхность белого фона
windowsSurface.fill(WHITE)

# нанесение на поверхность зеленого многоугольника
pygame.draw.polygon(windowsSurface, GREEN, ((146, 0,), (291, 106), (236, 277,), (56, 277), (0, 106)))

# нанесение на поверхность синих линий
pygame.draw.line(windowsSurface, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(windowsSurface, BLUE, (120, 60), (60, 120))
pygame.draw.line(windowsSurface, BLUE, (60, 120), (120, 120), 4)

# нанесение на поверхность синего круга
pygame.draw.circle(windowsSurface, BLUE, (300, 50), 20, 0)

# нанесение на поверхность красного элипса
pygame.draw.ellipse(windowsSurface, RED, (300, 250, 40, 80), 1)

# нанесение на поверхность фонового прямоугольника для текста
pygame.draw.rect(windowsSurface, RED,
                 (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

# получение массива пикселей поверхности
pixArray = pygame.PixelArray(windowsSurface)
pixArray[480][380] = BlACK
del pixArray

# нанесение текста на поверхность
windowsSurface.blit(text, textRect)

# отображение окна на экране
pygame.display.update()

# запуск игрового цикла
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
