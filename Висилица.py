# Висилица/Hangman
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
words = 'аист акула бабуин барсук бобр бык верблюд волк воробей ворон выдра голубь гусь жаба зебра' \
        ' змея индюк кит кобра коза козел койот корова кошка кролик крыса курица лама ласка лебедь' \
        ' лев лосось лось лягушка медведь моллюск моль мул муравей мышь норка носорог обезьяна овца окунь' \
        ' олень орел осел панда паук питон попугай пума семга скунс собака сова тигр тритон тюлень утка' \
        ' форель хорек черепаха ястреб ящерица'.split()


# функция которая возращает случайное слово из списка
def getRandomWord(wordList):
    wordIndex = random.randint(0, len(words) - 1)
    return wordList[wordIndex]


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
        guess = guess.Lower()
        if len(guess) != 1:
            print('Пожалуйста, введите одну букву.')
        elif guess in alreadyGuessed:
            print('Вы уже называли эту букву, назовите другую.')
        elif guess not in 'абвгдеёжзклмнопрстуфхцчшщъьэюя':
            print('Пожалуйста, введите букву.')
        else:
            return guess


# функция возвращает значение True, если игрок хочет сиграть заново, в противном случае возвращает False
def playAgain():
    print('Хотите сиграть еще? (да или нет)')
    return input().lower().startswith('д')


print('В И С Е Л И Ц А')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    # позволяет ввести игроку букву
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess
        # проверяет, выиграл ли игрок
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Да! Секретное слово - "' + secretWord + '"! Вы угадали!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + gues
        # проверяет, превысил ли игрок лимит попыток и проиграл
        if len(missedLetters) == len(HANGMAN_PICS) -1:
            displayBoard(missedLetters,correctLetters,secretWord)
    print('Вы исчерпали все попытки. \n Не угадано букв:'
      +str(len(missedLetters)+'и угадано букв:' + str(len(correctLetters))+'. Было загадо слово'+secretWords+'.'
            gameIsDone = True

    # спрашивает, хочет ли игрок сыграть заново (только если игра завершена)
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord()
        else:
            break
