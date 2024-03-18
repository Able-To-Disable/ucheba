# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


text = input('Введите текст:\n')
text_list = list(text)
shifr = int(input('Выберите параметр :\n1-Шифрование\n2-Расшифрование\n'))
result_list = []
types = int(input('тип шифрования или расшифрования :' ' \n1-Отдельный символ''\n2-Группа символов \n3-Слово\n'))
number = int(input('Количество элементов блока:'))  # Количество элементов блока
key = int(input('Введите ключ:\n'))
key_list = []
while key > 0:  # Превращение ключа в список
    key_list.append(key % 10)
    key //= 10
    key_list.reverse()
if shifr == 1:  # если нужно зашифровать
    if types == 1:
        while len(text_list) % len(key_list) != 0:  # добавление нулевых элементов в исходный список
            text_list.append('\0')
        for i in range(0, len(text_list), len(key_list)):
            for j in range(len(key_list)):
                result_list.append(text_list[i + key_list[j]])
        result = ''.join(result_list)
        result = result.replace("\0", "")
        print('Зашифрованный текст: \n')
        print(result)

    if types == 2:
        for i in range((len(text_list) // (len(key_list) * number) + 1) * (len(key_list) * number) - len(text_list)):
            text_list.append('\0')
        for i in range(0, len(text_list), len(key_list) * number):
            for j in range(len(key_list)):
                for g in range(number):
                    result_list.append(text_list[i + key_list[j] * number + g])
        result = ''.join(result_list)
        result = result.replace("\0", "")
        print('Зашифрованный текст: \n')
        print(result)
    if types == 3:
        text_list = text.split()
        while len(text_list) % len(key_list) != 0:
            text_list.append('\0')
        for i in range(0, len(text_list), len(key_list)):
            for j in range(len(key_list)):
                result_list.append(text_list[i + key_list[j]])
        result = ' '.join(result_list)
        result = result.replace("\0", "")
        print('Зашифрованный текст: \n')
        print(result)
if shifr == 2:
    if types == 1:
        while len(text_list) % len(key_list) != 0:
            text_list.append('\0')
        for i in range(len(text_list)):
            result_list.append('\0')
        for i in range(0, len(text_list), len(key_list)):
            for j in range(len(key_list)):
                result_list.insert(key_list[j] + i, text_list[j + i])
        result = ''.join(result_list)
        result = result.replace("\0", "")
        print('Расшифрованный текст: \n')
        print(result)

    if types == 2:
        for i in range((len(text_list) // (len(key_list) * number) + 1) * (len(key_list) * number) - len(text_list)):
            text_list.append('\0')
        for i in range(len(text_list)):
            result_list.append('\0')
        for i in range(0, len(text_list), len(key_list) * number):
            for j in range(len(key_list)):
                for g in range(number):
                    result_list.insert(i + key_list[j] * number + g, text_list[i + j + g])
        result = ''.join(result_list)
        result = result.replace("\0", "")
        print('Расшифрованный текст: \n')
        print(result)
    if types == 3:
        text_list = text.split()
        while len(text_list) % len(key_list) != 0:
            text_list.append('\0')
        for i in range(len(text_list)):
            result_list.append('\0')
        for i in range(0, len(text_list), len(key_list)):
            for j in range(len(key_list)):
                result_list.insert(key_list[j] + i, text_list[j + i])
        result = ' '.join(result_list)
        result = result.replace("\0", "")
        print('Расшифрованный текст: \n')
        print(result)
