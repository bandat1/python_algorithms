# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random, sys
from showsize import show_size

print(sys.version, sys.platform)
SIZE = 7
array = [random.randint(-100, 100) for i in range(SIZE)]
print(array)

min_num = min(array)
max_num = max(array)

idx_min = array.index(min_num)
idx_max = array.index(max_num)

print(f'Min = {array[idx_min]} в ячейке {idx_min}'
      f'\nMax = {array[idx_max]} в ячейке {idx_max}')
array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
print(array)

show_size(min_num)
show_size(idx_min)
show_size(max_num)
show_size(idx_max)
show_size(array)

"""
3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] win32
Для массива array:
 type= <class 'list'>, size= 60, object= [53, -81, 74, -95, -76, -52, -49]
	 type= <class 'int'>, size= 14, object= 53
	 type= <class 'int'>, size= 14, object= -81
	 type= <class 'int'>, size= 14, object= 74
	 type= <class 'int'>, size= 14, object= -95
	 type= <class 'int'>, size= 14, object= -76
	 type= <class 'int'>, size= 14, object= -52
	 type= <class 'int'>, size= 14, object= -49

Для объявленных переменных:	 
 type= <class 'int'>, size= 14, object= -95
 type= <class 'int'>, size= 14, object= 2
 type= <class 'int'>, size= 14, object= 74
 type= <class 'int'>, size= 14, object= 3

"""
