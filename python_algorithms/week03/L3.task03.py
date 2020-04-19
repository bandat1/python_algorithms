# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import  random

list1 = [random.randint(-100, 100) for i in range(7)]
print(list1)

max_index, max = 0, list1[0]
min_index, min = 0, list1[0]
for i, item in enumerate(list1):
    if item > max:
        max_index, max = i, item
    if item < min:
        min_index, min = i, item

list1[max_index] = min
list1[min_index] = max

print(list1)
