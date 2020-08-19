import random

NUM_DIGITS = 3  # колличество цифр в ответе
MAX_GUESES = 10  # колличество попыток


# возвращает строку случайных чисел, длин которой NUM_DIGITS
def getSecretNum():
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


# возвращает строку с подсказками пользователю - тепло/холодно/горячо
def getClues(guess, secretNum):
    if guess == secretNum:
        return 'Вы угадали'
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Горячо')
        elif guess[i] in secretNum:
            clues.append('Тепло')
    if len(clues) == 0:
        return 'Холодно'

    clues.sort()
    return ' '.join(clues)


# возвращает значение True если num - строка, состоит только из цифр, а противном случае - False
def isOnlyDigits(num):
    if num == '':
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False
        return True


print('Я загадаю %s-x число, которое вы должны отгадать.' % (NUM_DIGITS))
print('Я дам несколько подсказок...')
print('Когда я говорю:  Это означает:')
print(' Холодно         Ни одна цифра не отгадана')
print(' Тепло           Отгадана одна цифра, но не отгадана ее позиция')
print(' Горячо          Одна цифра и ее позиция отгаданы')

while True:
    secretNum = getSecretNum()
    print('Итак, я загадал число. У тебя есть %s попыток, чтобы отгадать его.' % (MAX_GUESES))

    guessesTaken = 1
    while guessesTaken <= MAX_GUESES:
        guess = ''
        while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
            print('Попытка #%s:' % (guessesTaken))
            guess = input()
        print(getClues(guess, secretNum))
        guessesTaken += 1

        if guess == secretNum:
            break
        if guessesTaken > MAX_GUESES:
            print('Попыток больше не осталось. Я загадал число %s' % (secretNum))

    print('Хотите сыграть еще раз? (да/нет)')
    if not input().lower().startswith('д'):
        break
