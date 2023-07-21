import time


''' Задание №3
Добавьте к задачам 1 и 2 строки документации для классов.
'''

#1
class MyString(str):
    """
    Класс MyString наследует функциональность стандартного класса str.
    Дополнительно хранит имя автора строки и время создания.

    Атрибуты:
        author (str): Имя автора строки.
        creation_time (float): Время создания строки в формате time.time().
    """

    def __new__(cls, value, author):
        """
        Создает новый объект класса MyString.

        Аргументы:
            value (str): Значение строки.
            author (str): Имя автора строки.

        Возвращает:
            MyString: Новый объект класса MyString.
        """
        obj = super(MyString, cls).__new__(cls, value)
        obj.author = author
        obj.creation_time = time.time()
        return obj


author_name = "Пушкин А.С."
my_string = MyString("Зима!.. Крестьянин, торжествуя, \
    \nНа дровнях обновляет путь; \
        \nЕго лошадка, снег почуя, \
            \nПлетется рысью как-нибудь;", author_name)
print("Строка:", my_string)
print("Автор:", my_string.author)
print("Время создания:", my_string.creation_time)
help(MyString)
print('------------------------')


#2
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


archive1 = Archive(10, "первый")
archive2 = Archive(20, "второй")
archive3 = Archive(30, "третий")
print("Архивы чисел:", Archive.get_number_archives())
print("Архивы строк:", Archive.get_string_archives())
print("Архив 1: число =", archive1.number, "строка =", archive1.string)
print("Архив 2: число =", archive2.number, "строка =", archive2.string)
print("Архив 3: число =", archive3.number, "строка =", archive3.string)
help(Archive)
