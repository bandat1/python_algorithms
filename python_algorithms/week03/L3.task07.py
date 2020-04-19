# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

import random

list1 = [random.randint(-10, 10) for i in range(10)]
print(f'Массив: {list1}')

min_index1, min1 = 0, list1[0] # индекс минимального элемента в массиве и его значение
min_index2, min2 = 0, list1[0] # индекс минимального элемента в массиве и его значение

for i, item in enumerate(list1): # ищем самый минимальный элементы массива
    if item < min1:
        min1 = item
        min_index1 = i
for i, item in enumerate(list1): # ищем минимальный элементы массива
    if i != min_index1 and item < min2:
        min2 = item
        min_index2 = i

print(f'Answer: {min1} and {min2}')