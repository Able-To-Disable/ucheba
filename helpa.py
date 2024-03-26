from abc import ABC, abstractmethod


class CipherManager(ABC):

    def __init__(self) -> None:
        self._data: list = []

    @abstractmethod
    def _get_by_separated_symbol(self, text_list, key_list) -> str:
        ...

    @abstractmethod
    def _get_by_group(self, text_list, key_list, number) -> str:
        ...

    @abstractmethod
    def _get_by_word(self, text_list, key_list) -> str:
        ...

    def execute(self, shifr: int, text_list, key_list, number) -> str:
        match shifr:
            case 1:
                return self._get_by_separated_symbol(text_list, key_list)
            case 2:
                return self._get_by_group(text_list, key_list, number)
            case 3:
                return self._get_by_word(text_list, key_list)
            case _:
                print("Not found")


class Decrypter(CipherManager):

    def _get_by_separated_symbol(self, text_list, key_list) -> str:
        while len(text_list) % len(key_list) != 0:
            text_list.append('\0')
        for i in range(0, len(text_list), len(key_list)):
            for j in range(len(key_list)):
                self._data.append(text_list[i + key_list[j]])
        result = ''.join(self._data)
        result = result.replace("\0", "")
        return result

    def _get_by_group(self, text_list, key_list, number) -> str:
        for i in range(
                (len(text_list) // (len(key_list) * number) + 1) * (len(key_list) * number) - len(text_list)):
            text_list.append('\0')
        for i in range(0, len(text_list), len(key_list) * number):
            for j in range(len(key_list)):
                for g in range(number):
                    self._data.append(text_list[i + key_list[j] * number + g])
        result = ''.join(self._data)
        result = result.replace("\0", "")
        return result

    def _get_by_word(self, text_list, key_list) -> str:
        text_list = "".join(text_list).split()
        while len(text_list) % len(key_list) != 0:
            text_list.append('\0')
        for i in range(0, len(text_list), len(key_list)):
            for j in range(len(key_list)):
                self._data.append(text_list[i + key_list[j]])
        result = ' '.join(self._data)
        result = result.replace("\0", "")
        return result


class Encrypter(CipherManager):

    def _get_by_separated_symbol(self, text_list, key_list) -> str:
        while len(text_list) % len(key_list) != 0:
            text_list.append('\0')
        for i in range(len(text_list)):
            self._data.append('\0')
        for i in range(0, len(text_list), len(key_list)):
            for j in range(len(key_list)):
                self._data.insert(key_list[j] + i, text_list[j + i])
        result = ''.join(self._data)
        result = result.replace("\0", "")
        return result

    def _get_by_group(self, text_list, key_list, number) -> str:
        for i in range(
                (len(text_list) // (len(key_list) * number) + 1) * (len(key_list) * number) - len(text_list)):
            text_list.append('\0')
        for i in range(len(text_list)):
            self._data.append('\0')
        for i in range(0, len(text_list), len(key_list) * number):
            for j in range(len(key_list)):
                for g in range(number):
                    self._data.insert(i + key_list[j] * number + g, text_list[i + j + g])
        result = ''.join(self._data)
        result = result.replace("\0", "")
        return result

    def _get_by_word(self, text_list, key_list) -> str:
        text_list = "".join(text_list).split()
        while len(text_list) % len(key_list) != 0:
            text_list.append('\0')
        for i in range(len(text_list)):
            self._data.append('\0')
        for i in range(0, len(text_list), len(key_list)):
            for j in range(len(key_list)):
                self._data.insert(key_list[j] + i, text_list[j + i])
        result = ' '.join(self._data)
        result = result.replace("\0", "")
        return result


def main() -> None:
    number = None
    key_list = []
    text = input('Введите текст:\n')
    text_list = list(text)
    shifr = int(input('Выберите параметр :\n1-Шифрование\n2-Расшифрование\n'))
    type_is = int(input(
        'шифрование или расшифрование :\n1-Отдельный символ\n2-Группа из заданного количества символов \n3-Слово\n'))
    if type_is == 2:
        number = int(input('Количество элементов блока:'))  # Количество элементов блока
    key = int(input('Введите ключ:\n'))

    while key > 0:  # Превращение ключа в список
        key_list.append(key % 10)
        key //= 10
    key_list.reverse()

    match shifr:
        case 1:
            result: str = Decrypter().execute(shifr, text_list, key_list, number)
            print(f"Зашифрованный текст: {result}")
        case 2:
            result: str = Encrypter().execute(shifr, text_list, key_list, number)
            print(f"Расшифрованный текст: {result}")
        case _:
            print("Handler is not found")


if __name__ == "__main__":
    main()
