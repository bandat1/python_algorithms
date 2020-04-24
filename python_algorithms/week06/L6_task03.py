# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random, sys
from showsize import show_size

print(sys.version, sys.platform)
SIZE = 7
array = [random.randint(-100, 100) for i in range(SIZE)]
print(array)

max_index, max = 0, array[0]
min_index, min = 0, array[0]
for i, item in enumerate(array):
    if item > max:
        max_index, max = i, item
    if item < min:
        min_index, min = i, item

array[max_index] = min
array[min_index] = max

print(f'Min = {min} в ячейке {min_index}'
      f'\nMax = {max} в ячейке {max_index}')
print(array)

show_size(max_index)
show_size(max)
show_size(min_index)
show_size(min)
show_size(array)

"""
3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] win32
Для массива array:
 type= <class 'list'>, size= 60, object= [74, -76, 76, -10, -78, -59, 36]
	 type= <class 'int'>, size= 14, object= 74
	 type= <class 'int'>, size= 14, object= -76
	 type= <class 'int'>, size= 14, object= 76
	 type= <class 'int'>, size= 14, object= -10
	 type= <class 'int'>, size= 14, object= -78
	 type= <class 'int'>, size= 14, object= -59
	 type= <class 'int'>, size= 14, object= 36

Для объявленных переменных:
 type= <class 'int'>, size= 14, object= 4
 type= <class 'int'>, size= 14, object= 76
 type= <class 'int'>, size= 14, object= 2
 type= <class 'int'>, size= 14, object= -78
 
Общий вывод: размер массива во всех трех программах одинаковый, поэтому играет только количество переменных, объявленных в коде помимо массива.
Первое решение оказалось самым экономичным по памяти.
p.s. наличие числа 0 в массиве тоже играет роль, т.к. оно занимает 12 байт. 
"""
