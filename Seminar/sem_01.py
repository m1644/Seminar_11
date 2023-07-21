import time


''' Задание №1
Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания (time.time)
'''

class MyString(str):
    def __new__(cls, value, author):
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
print("------------------------")
