import time


''' Задание №1
Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания (time.time)
'''

# Добавлены строки документации и методы вывода информации на печать.

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

    def __str__(self):
        """
        Возвращает строковое представление объекта для вывода на экран.

        Возвращает:
            str: Строковое представление объекта.
        """
        return f"Значение: {super().__str__()}, Автор: {self.author}, Время создания: {self.creation_time}"

    def __repr__(self):
        """
        Возвращает формальное строковое представление объекта.

        Возвращает:
            str: Формальное строковое представление объекта.
        """
        return f"MyString(value={super().__repr__()}, author='{self.author}')"


author_name = "Пушкин А.С."
my_string = MyString("Зима!.. Крестьянин, торжествуя, \
    \nНа дровнях обновляет путь; \
        \nЕго лошадка, снег почуя, \
            \nПлетется рысью как-нибудь;", author_name)
print("Строка:", my_string)
print("Автор:", my_string.author)
print("Время создания:", my_string.creation_time)

# Выводим информацию о строке
print("------------------------")
# help(MyString)
print("Информация о строке:")
print(my_string)
print(repr(my_string))
