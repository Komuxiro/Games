# Игра - Царство драконов / Game - Dragon Kingdom

import random
import time


def displayIntro():
    print('''Вы находитесь в землях, заселенных драконами.
Перед собой вы видите две пещеры.
В одной из них - дружелюбный дракон,
который готов поделиться с вами своими сокровищами.
Во второй - жадный и голодный дракон, который мигом вас съест.''')
    print()


def chooseCave():  # спрашиваем в какую пещеру пойдет игрок
    cave = ()  # переменная для пещеры куда зайдет игрок
    while cave != '1' and cave != '2':
        print('В какую пещеру вы войдете? (Нажмите клавишу 1 или 2)')
        cave = input()
    return cave


def checkCave(chosenCave):
    print('Вы приближаетесь к пещере...')
    time.sleep(2)
    print('Ее темнота заставлет вас дрожать от страха...')
    time.sleep(2)
    print('Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и...')
    # print()
    time.sleep(2)
    friendlyCave = random.randint(1, 2)  # определяем пещеру с дружелюбным драконом
    if chosenCave == str(friendlyCave):
        print('...делится с вами своими сокровищами!')
    else:
        print('... моментально вас съедает!')


playAgain = 'Да'
while playAgain == 'Да' or playAgain == 'Д':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    print('Попробуйте еще раз? (Да или Нет)')
    playAgain = input()
