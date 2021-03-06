# Виселица/Hangman
import random

HANGMAN_PICS = ['''
+---+
    |
    |
    |
   ===''', '''
+---+
    |
    |
    |
   ===''', '''
+---+
0   |
|   |
    |
   ===''', '''
 +--+
 0  |
/|  |
    |
   ===''', '''
 +--+
 0  |
/|\ |
    |
   ===''', '''
 +--+
 0  |
/|\ |
/   |
   ===''', '''
 +--+
 0  |
/|\ |
/ \ |
   ===''']
words = {'Цвета': 'красный оранжеый жедтый зеленый синий голубой фиолетовый черный'.split(),
         'Фигуры': 'квадрат треугольник прямоугольник круг эллипс ромб трапеция'.split(),
         'Животные': 'аист акула бабуин барсук бобр бык верблюд волк воробей ворон выдра голубь гусь жаба зебра' \
                     ' змея индюк кит кобра коза козел койот корова кошка кролик крыса курица лама ласка лебедь' \
                     ' лев лосось лось лягушка медведь моллюск моль мул муравей мышь норка носорог обезьяна овца окунь' \
                     ' олень орел осел панда паук питон попугай пума семга скунс собака сова тигр тритон тюлень утка' \
                     ' форель хорек черепаха ястреб ящерица'.split()}


# функция которая возращает случайную строку из переданного словаря,А также ключ
def getRandomWord(wordDict):
    wordKey = random.choice(list(wordDict.keys()))  # случайным образом выбираем ключ
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)  # случайным образом выбираем слово из списка ключей в словаре


# отображаем игровое поле с введенными буквами и теми которые угаданы или нет
def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Ошибочные буквы:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):  # меняем пропуски отгаданными буквами
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

    for letter in blanks:  # показывает секретное слово с пробелами между букв
        print(letter, end=' ')
    print()


# возвращает букву введенную игроком. Функция проверяет, что игрок ввел только одну букву и ничего больше
def getGuess(alreadyGuessed):
    while True:
        print('Введите букву.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:  # проверяем что введено не более одного символа
            print('Пожалуйста, введите одну букву.')
        elif guess in alreadyGuessed:
            print('Вы уже называли эту букву, назовите другую.')
        elif guess not in 'абвгдеёжзклмнопрстуфхцчшщъьэюяй':
            print('Пожалуйста, введите букву.')
        else:
            return guess


# функция возвращает значение True, если игрок хочет сиграть заново, в противном случае возвращает False
def playAgain():
    print('Хотите сиграть еще? (да или нет)')
    return input().lower().startswith('д')


# далее идет оснвной игровой цикл
print('В И С Е Л И Ц А')

# выбираем уровень сложности
difficulty = ''
while difficulty not in 'ЛСТ':
    print('Выберите уровень сложности: Л - Легкий, С -средний, Т - тяжелый')
    difficulty = input().upper()
if difficulty == 'C':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
if difficulty == 'Т':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]

missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False  # данной переменной присвоится значение True в случае, когда поступит сигнал завершения игры и если игрок захочет сыграть еще

while True:
    print('Секретное слово из набора: '+ secretSet) # говорим категорию загаданного слова
    print('Секретное слово из набора: '+ secretSet) # говорим категорию загаданного слова
    displayBoard(missedLetters, correctLetters, secretWord)
    # позволяет ввести игроку букву
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess
        # проверяет, выиграл ли игрок сравнивая каждую букву загаданного слова с введенными буквами
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Да! Секретное слово - "' + secretWord + '"! Вы угадали!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        # проверяет, превысил ли игрок лимит попыток и проиграл
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
    print('Вы исчерпали все попытки.\nНе угадано букв:'
          + str(len(missedLetters)) + ' и угадано букв:' + str(
        len(correctLetters)) + '. Было загадано слово "' + secretWord + '".')
    gameIsDone = True

    # спрашивает, хочет ли игрок сыграть заново (только если игра завершена)
    if gameIsDone:
        if playAgain():
            missedLetters = ''  # если новая игра то обнуляем это значение
            correctLetters = ''  # если новая игра то обнуляем это значение
            gameIsDone = False
            secretWord,secretSet = getRandomWord(words)  # если новая игра то выбирается новове слово
        else:
            break
