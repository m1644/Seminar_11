

''' Задание №6
Доработайте прошлую задачу.
Добавьте сравнение прямоугольников по площади
Должны работать все шесть операций сравнения
'''

# Добавлены строки документации и методы вывода информации на печать.

class Rectangle:
    def __init__(self, length, width=None):
        """
        Конструктор класса прямоугольник.

        :param length: Длина прямоугольника.
        :param width: Ширина прямоугольника (если не указана, будет считаться квадратом).
        """
        self.length = length
        self.width = length if width is None or width == "" else width

    def get_perimeter(self):
        """
        Вычисляет периметр прямоугольника.

        :return: Значение периметра.
        """
        return 2 * (self.length + self.width)

    def get_area(self):
        """
        Вычисляет площадь прямоугольника.

        :return: Значение площади.
        """
        return self.length * self.width

    def __add__(self, other):
        """
        Переопределение операции сложения для прямоугольников.

        :param other: Другой прямоугольник для сложения.
        :return: Новый прямоугольник суммы.
        :raises ValueError: Если сложение выполняется с объектом другого типа.
        """
        if not isinstance(other, Rectangle):
            raise ValueError("Можно сложить только два прямоугольника")
        new_length = self.length + other.length
        new_width = self.width + other.width
        return Rectangle(new_length, new_width)

    def __sub__(self, other):
        """
        Переопределение операции вычитания для прямоугольников.

        :param other: Другой прямоугольник для вычитания.
        :return: Новый прямоугольник разности.
        :raises ValueError: Если вычитание выполняется с объектом другого типа.
        """
        if not isinstance(other, Rectangle):
            raise ValueError("Можно вычесть только другой прямоугольник")
        new_length = self.length - other.length
        new_width = self.width - other.width

        # Ограничиваем значения длины и ширины нулем, чтобы избежать отрицательных значений
        new_length = max(new_length, 0)
        new_width = max(new_width, 0)

        return Rectangle(new_length, new_width)

    def __eq__(self, other):
        """
        Переопределение операции равенства для прямоугольников.

        :param other: Другой прямоугольник для сравнения.
        :return: Результат сравнения.
        """
        if not isinstance(other, Rectangle):
            return False
        return self.get_area() == other.get_area()

    def __ne__(self, other):
        """
        Переопределение операции неравенства для прямоугольников.

        :param other: Другой прямоугольник для сравнения.
        :return: Результат сравнения.
        """
        return not self.__eq__(other)

    def __lt__(self, other):
        """
        Переопределение операции "меньше" для прямоугольников.

        :param other: Другой прямоугольник для сравнения.
        :return: Результат сравнения.
        :raises ValueError: Если сравнение выполняется с объектом другого типа.
        """
        if not isinstance(other, Rectangle):
            raise ValueError("Можно сравнивать только с другим прямоугольником")
        return self.get_area() < other.get_area()

    def __le__(self, other):
        """
        Переопределение операции "меньше или равно" для прямоугольников.

        :param other: Другой прямоугольник для сравнения.
        :return: Результат сравнения.
        :raises ValueError: Если сравнение выполняется с объектом другого типа.
        """
        if not isinstance(other, Rectangle):
            raise ValueError("Можно сравнивать только с другим прямоугольником")
        return self.get_area() <= other.get_area()

    def __gt__(self, other):
        """
        Переопределение операции "больше" для прямоугольников.

        :param other: Другой прямоугольник для сравнения.
        :return: Результат сравнения.
        :raises ValueError: Если сравнение выполняется с объектом другого типа.
        """
        if not isinstance(other, Rectangle):
            raise ValueError("Можно сравнивать только с другим прямоугольником")
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        """
        Переопределение операции "больше или равно" для прямоугольников.

        :param other: Другой прямоугольник для сравнения.
        :return: Результат сравнения.
        :raises ValueError: Если сравнение выполняется с объектом другого типа.
        """
        if not isinstance(other, Rectangle):
            raise ValueError("Можно сравнивать только с другим прямоугольником")
        return self.get_area() >= other.get_area()

    def __str__(self):
        """
        Возвращает строковое представление прямоугольника.

        :return: Строковое представление.
        """
        return f"Прямоугольник: длина={self.length}, ширина={self.width}, периметр={self.get_perimeter()}, площадь={self.get_area()}"


# Вводим длину и ширину первого прямоугольника
length_1 = float(input("Введите длину первого прямоугольника: "))
width_1 = input("Введите ширину первого прямоугольника (если оставить пустым, будет считаться квадрат): ")
if width_1:
    width_1 = float(width_1)

# Вводим длину и ширину второго прямоугольника
length_2 = float(input("Введите длину второго прямоугольника: "))
width_2 = input("Введите ширину второго прямоугольника (если оставить пустым, будет считаться квадрат): ")
if width_2:
    width_2 = float(width_2)

# Создаем экземпляры класса
rectangle_instance_1 = Rectangle(length_1, width_1)
rectangle_instance_2 = Rectangle(length_2, width_2)

# Вычисляем периметры
perimeter_1 = rectangle_instance_1.get_perimeter()
perimeter_2 = rectangle_instance_2.get_perimeter()

# Выполняем операции сложения и вычитания
sum_rectangle = rectangle_instance_1 + rectangle_instance_2
sub_rectangle = rectangle_instance_1 - rectangle_instance_2

# Выводим результаты
print(f"Периметр первого прямоугольника: {perimeter_1}")
print(f"Периметр второго прямоугольника: {perimeter_2}")

sum_perimeter = sum_rectangle.get_perimeter()
sum_area = sum_rectangle.get_area()
print(f"Сумма периметров прямоугольников: {sum_perimeter}")
print(f"Площадь суммы прямоугольников: {sum_area}")

sub_perimeter = sub_rectangle.get_perimeter()
sub_area = sub_rectangle.get_area()
print(f"Разность периметров прямоугольников (не меньше нуля): {sub_perimeter}")
print(f"Площадь разности прямоугольников (не меньше нуля): {sub_area}")

# Сравниваем прямоугольники по площади
if rectangle_instance_1 == rectangle_instance_2:
    print("Прямоугольники равны по площади")
elif rectangle_instance_1 != rectangle_instance_2:
    print("Прямоугольники не равны по площади")

if rectangle_instance_1 < rectangle_instance_2:
    print("Первый прямоугольник меньше второго по площади")
elif rectangle_instance_1 <= rectangle_instance_2:
    print("Первый прямоугольник меньше или равен второму по площади")

if rectangle_instance_1 > rectangle_instance_2:
    print("Первый прямоугольник больше второго по площади")
elif rectangle_instance_1 >= rectangle_instance_2:
    print("Первый прямоугольник больше или равен второму по площади")

# Выводим информацию о прямоугольниках
print("------------------------")
# help(Rectangle)
print("Информация о прямоугольниках:")
print(rectangle_instance_1)
print(rectangle_instance_2)
