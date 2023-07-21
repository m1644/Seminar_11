


''' Задание №2
Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков архивов
list-архивы также являются свойствами экземпляра
'''

class Archive:
    _number_archives = []
    _string_archives = []

    def __init__(self, number, string):
        self._number = number
        self._string = string
        self._number_archives.append(number)
        self._string_archives.append(string)

    @property
    def number(self):
        return self._number

    @property
    def string(self):
        return self._string

    @classmethod
    def get_number_archives(cls):
        return cls._number_archives

    @classmethod
    def get_string_archives(cls):
        return cls._string_archives


archive1 = Archive(10, "первый")
archive2 = Archive(20, "второй")
archive3 = Archive(30, "третий")

print("Архивы чисел:", Archive.get_number_archives())
print("Архивы строк:", Archive.get_string_archives())

print("Архив 1: число =", archive1.number, "строка =", archive1.string)
print("Архив 2: число =", archive2.number, "строка =", archive2.string)
print("Архив 3: число =", archive3.number, "строка =", archive3.string)
