
SYMBOLS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя0123456789 !@#$%^&*()_+-№,?.:;'
MAX_KEY_SIZE = len(SYMBOLS)

def getMode():
    while True:
        print('Вы хотите зашифровать, расшифровать или взломать текст?')
        mode = input().lower()
        if mode in ('зашифровать', 'з', 'расшифровать', 'р', 'взломать', 'в'):
            return mode
    else:
        print('Введите "зашифровать" или "з" для зашифровки или "расшифровать" или "р" для расшифровки или "в" или "взломать"')

def getMessage(): # получаем от пользователя сообщение и возвращаем его
    print('Введите текст')
    return input()

def getKey(): # пользователь вводит ключ шифрования который будет использоваться для шифрования/расшифрования
    key = 0
    while True:
        print('Введите ключ шифрования (1-%s)' %(MAX_KEY_SIZE))
        key = int(input())
        if (key >=1 and key <=MAX_KEY_SIZE):
            return key

def getTransLatedMessage(mode, message, key): # функция выполняет шифрование/расшифрование
    if mode [0] == 'р':
        key = -key
    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex ==-1: # символ не найден в SYMBOLS
            # просто добавь этот символ без изменений
            translated += symbol
        else:
            #зашифровать или расшифровать
            symbolIndex += key

            if symbolIndex >= len(SYMBOLS):
                symbolIndex -= len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)

            translated += SYMBOLS[symbolIndex]
    return  translated

mode = getMode()
message = getMessage()
if mode[0] != 'в':
    key = getKey()
print('Преобразованный текст: ')
if mode[0] != 'в':
    print(getTransLatedMessage(mode, message, key))
else:
    for key in range (1, MAX_KEY_SIZE + 1):
        print(key, getTransLatedMessage('расшифровать', message, key))

