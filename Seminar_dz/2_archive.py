

''' Задание №2
Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков архивов
list-архивы также являются свойствами экземпляра
'''

# Добавлены строки документации и методы вывода информации на печать.

class Archive:
    """
    Класс Archive хранит пару свойств и сохраняет старые данные в списки архивов.

    Атрибуты:
        _number_archives (list): Список архивов чисел.
        _string_archives (list): Список архивов строк.

    Свойства:
        number (int): Числовое свойство экземпляра класса.
        string (str): Строковое свойство экземпляра класса.
    """

    _number_archives = []
    _string_archives = []

    def __init__(self, number, string):
        """
        Инициализирует новый объект класса Archive.

        Аргументы:
            number (int): Значение числового свойства.
            string (str): Значение строкового свойства.
        """
        self._number = number
        self._string = string
        self._number_archives.append(number)
        self._string_archives.append(string)

    @property
    def number(self):
        """
        Возвращает числовое свойство экземпляра класса.

        Возвращает:
            int: Значение числового свойства.
        """
        return self._number

    @property
    def string(self):
        """
        Возвращает строковое свойство экземпляра класса.

        Возвращает:
            str: Значение строкового свойства.
        """
        return self._string

    @classmethod
    def get_number_archives(cls):
        """
        Возвращает список архивов чисел.

        Возвращает:
            list: Список архивов чисел.
        """
        return cls._number_archives

    @classmethod
    def get_string_archives(cls):
        """
        Возвращает список архивов строк.

        Возвращает:
            list: Список архивов строк.
        """
        return cls._string_archives

    def __repr__(self):
        """
        Возвращает формальное строковое представление объекта.

        Возвращает:
            str: Формальное строковое представление объекта.
        """
        return f"Archive(number={self.number}, string='{self.string}')"

    def __str__(self):
        """
        Возвращает строковое представление объекта для вывода на экран.

        Возвращает:
            str: Строковое представление объекта.
        """
        return f"Число: {self.number}, Строка: '{self.string}'"


archive1 = Archive(10, "первый")
archive2 = Archive(20, "второй")
archive3 = Archive(30, "третий")

print("Архивы чисел:", Archive.get_number_archives())
print("Архивы строк:", Archive.get_string_archives())

print("Архив 1:", archive1)
print("Архив 2:", archive2)
print("Архив 3:", archive3)

# Выводим информацию об архивах
print("------------------------")
# help(Archive)
print("Информация об архивах:")
print(archive1)
print(archive2)
print(archive3)
print(repr(archive1))
print(repr(archive2))
print(repr(archive3))
