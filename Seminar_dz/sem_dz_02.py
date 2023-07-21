

'''
Создайте класс Матрица. Добавьте методы для:
○ вывода на печать,
○ сравнения,
○ сложения,
○ *умножения матриц
'''

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        result = ""
        for row in self.data:
            result += " ".join(str(elem) for elem in row) + "\n"
        return result

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False
        if self.rows != other.rows or self.cols != other.cols:
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] != other.data[i][j]:
                    return False
        return True

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("Складывать матрицы можно только вместе.")
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Для сложения матрицы, они должны иметь одинаковые размеры.")
        
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.data[i][j] = self.data[i][j] * other
            return result

        if not isinstance(other, Matrix):
            raise ValueError("Матрицу можно умножать только на другую матрицу или скаляр.")
        
        if self.cols != other.rows:
            raise ValueError("Количество столбцов в первой матрице должно быть равно количеству строк во второй матрице.")
        
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result

# Пример использования класса Матрица:
m1 = Matrix(3, 3)
m1.data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

m2 = Matrix(3, 3)
m2.data = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

print("Matrix 1:")
print(m1)

print("Matrix 2:")
print(m2)

print("Matrix 1 == Matrix 2:", m1 == m2)

m3 = m1 + m2
print("Matrix 1 + Matrix 2:")
print(m3)

m4 = m1 * 2
print("Matrix 1 * 2:")
print(m4)

m5 = m1 * m2
print("Matrix 1 * Matrix 2:")
print(m5)
