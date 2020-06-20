# Игра для угадывания чисел / Number guessing game
import random

guessesTaken = 0  # переменная которая будет считать колличество попыток

print('Привет! Как тебя зовут?')
myName = input()
number = random.randint(1, 20)  # вызываем функцию randint, указывая диапазон загадываемых чисел
print('Что ж, ' + myName, 'я загадал число от 1 до 20.')

for guessesTaken in range(6):  # указываем колличество циклов которое дается игроку на угадывание числа
    print('Попробуй угадать. У тебя 6 попыток')
    guess = int(input())  # число которое вводит игрок

    if guess < number:
        print('Твое число слишко маленькое')
    elif guess > number:
        print('Твое число слишком большое')
    elif guess == number:
        guessesTaken = str(guessesTaken + 1)
        print('Отлично, ' + myName + '! Ты справился за ' + guessesTaken + ' попытки!')
        break

if guess != number:
    number = str(number)
    print('Увы ты не справился. Я загадал число' + number + '.')
