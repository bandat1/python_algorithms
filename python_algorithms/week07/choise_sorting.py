# Сортировка выборром

from random import randint, shuffle

SIZE = 9
array = [randint(0, 10) for i in range(SIZE)] # массив из рандомных чисел (возможны повторения чисел)

#array = [i for i in range(SIZE)]
#shuffle(array)
print(array)

for j in range(len(array)):
    min_ind = j
    for i in range(j + 1, len(array)):
        if array[i] < array[min_ind]:
            min_ind = i

    array[min_ind], array[j] = array[j], array[min_ind]

print(array)
