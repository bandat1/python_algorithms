# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

list1 = [random.randint(-10, 10) for i in range(10)]
print(f'Массив: {list1}')

max_index, max = 0, list1[0] # индекс максимального элемента в массиве и его значение
min_index, min = 0, list1[0] # индекс минимального элемента в массиве и его значение

for i, item in enumerate(list1): # ищем максимальный и минимальный элементы массива
    if item > max:
        max = item
        max_index = i
    if item < min:
        min = item
        min_index = i
print(f'max = {max}, min = {min}')
sum = 0 # сумма элементов, находящихся между минимальным и максимальным элементами
if max_index > min_index:
    for i in range(min_index + 1, max_index):
        sum += list1[i]
else:
    for i in range(max_index + 1, min_index):
        sum += list1[i]

print(f'Сумма элементов, находящихся между минимальным и максимальным элементами: {sum}')