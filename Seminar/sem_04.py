

''' Задание №4
Доработаем класс Архив из задачи 2.
Добавьте методы представления экземпляра для программиста и для пользователя.
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

    def __repr__(self):
        return f"Archive(number={self.number}, string='{self.string}')"

    def __str__(self):
        return f"Архив: Число = {self.number}, Строка = '{self.string}'"


archive1 = Archive(10, "первый")
archive2 = Archive(20, "второй")
archive3 = Archive(30, "третий")

print("Архивы чисел:", Archive.get_number_archives())
print("Архивы строк:", Archive.get_string_archives())

print("Архив 1:", archive1)
print("Архив 2:", archive2)
print("Архив 3:", archive3)

print("----Представление для программиста:")
print(repr(archive1))
print(repr(archive2))
print(repr(archive3))

print("----Представление для пользователя:")
print(str(archive1))
print(str(archive2))
print(str(archive3))
