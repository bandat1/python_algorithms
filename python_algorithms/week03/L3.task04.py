# 4. Определить, какое число в массиве встречается чаще всего.

import  random

list1 = [0, 10, 10, 1, 8, 2, 8]
print(list1)

list2 = [] # массив, длина которого равна длине list1. здесь будут храниться значения повторей для каждого числа из list1
for i in list1:
    m = 0
    for j in list1:
        if i == j:
            m += 1
    list2.append(m)

#print(list2)

search_num_index, search_num = 0, 0
for i, item in enumerate(list2): # ищем максимальное значение в массиве list2
    if item > search_num:
        search_num = item
        search_num_index= i

print(f'Чаще всего встречается число {list1[search_num_index]}')


