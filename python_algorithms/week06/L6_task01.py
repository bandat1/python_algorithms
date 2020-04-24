# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random, sys
from showsize import show_size

print(sys.version, sys.platform)
SIZE = 7
array = [random.randint(-100, 100) for i in range(SIZE)]
print(array)

idx_min = 0
idx_max = 0

for i in range(SIZE):
    if array[i] < array[idx_min]:
        idx_min = i
    elif array[i] > array[idx_max]:
        idx_max = i

print(f'Min = {array[idx_min]} в ячейке {idx_min}'
      f'\nMax = {array[idx_max]} в ячейке {idx_max}')
array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
print(array)

show_size(idx_min)
show_size(idx_max)
show_size(array)

"""
3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] win32
Для массива array:
 type= <class 'list'>, size= 60, object= [-19, -9, 18, 38, -92, -56, -89]
	 type= <class 'int'>, size= 14, object= -19
	 type= <class 'int'>, size= 14, object= -9
	 type= <class 'int'>, size= 14, object= 18
	 type= <class 'int'>, size= 14, object= 38
	 type= <class 'int'>, size= 14, object= -92
	 type= <class 'int'>, size= 14, object= -56
	 type= <class 'int'>, size= 14, object= -89

Для объявленных переменных:	 
 type= <class 'int'>, size= 14, object= 3
 type= <class 'int'>, size= 14, object= 4

"""

