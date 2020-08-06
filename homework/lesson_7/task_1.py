""" Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:

    def __init__(self, matrix):
        self.__matrix = matrix

    def __str__(self):
        for i in self.__matrix:
            line = ''
            for element in i:
                line += str(element) + ' '
            print(line)

    def __add__(self, other):
        matrix_2 = other.get_matrix()
        if len(self.__matrix) != len(matrix_2):
            return ValueError('Матрицы должны быть одинакового размера!')
        for idx in range(0, len(self.__matrix)):
            if len(self.__matrix[idx]) != len(matrix_2[idx]):
                return ValueError('Матрицы должны быть одинакового размера!')

        new_matrix = []
        for i in range(0, len(self.__matrix)):
            inner_list = []
            for j in range(0, len(self.__matrix[i])):
                inner_list.append(self.__matrix[i][j] + matrix_2[i][j])
            new_matrix.append(inner_list)

        return Matrix(new_matrix)

    def get_matrix(self):
        return self.__matrix


matrix = [
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
]

mat = Matrix(matrix)

matrix_2 = [
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
]

mat_2 = Matrix(matrix_2)
result = mat.__add__(mat_2)
result.__str__()