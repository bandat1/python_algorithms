# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

matrix = [[random.randint(1, 10) for _ in range(5)] for _ in range(5)]
for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()

list1 = []
k = 0
for j in range(5):
    min = matrix[k][j]
    for i in range(5):
        if matrix[i][j] < min:
            min = matrix[i][j]
    list1.append(min)
    k += 1

max = list1[0]
for i in range(5):
    if list1[i] > max:
        max = list1[i]

print(f'Max number = {max}')