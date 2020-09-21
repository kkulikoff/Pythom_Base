# Task 1
# Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__()
# для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.

class Matrix:
    def __init__(self, array):
        self.array = array

    def __str__(self):
        return '\n'.join(str(s) for s in self.array)

    def __add__(self, other):
        return Matrix([[j[0] + j[1] for j in zip(i[0], i[1])] for i in zip(self.array, other.array)])


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_3 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8]])
matrix_4 = Matrix([[6, 5], [4, 3], [2, 1]])
matrix_5 = Matrix([[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]])
matrix_6 = Matrix([[2, 2, 2], [2, 1, 2], [2, 2, 2]])

m1 = matrix_1 + matrix_1
m2 = matrix_2 + matrix_2
m3 = matrix_3 + matrix_3
m4 = matrix_4 + matrix_4
m1_4 = matrix_1 + matrix_4
m_ziccurat = matrix_5 + matrix_6

print('matrix_1 + matrix_1:', m2, sep='\n')
print('')
print('matrix_2 + matrix_2:', m2, sep='\n')
print('')
print('matrix_3 + matrix_3:', m3, sep='\n')
print('')
print('matrix_4 + matrix_4:', m4, sep='\n')
print('')
print('matrix1 + matrix4:', m1_4, sep='\n')
print('')
print('W O W:', m_ziccurat, sep='\n')
