# Сортировка вставками

from random import randint, shuffle

SIZE = 9
array = [randint(0, 10) for i in range(SIZE)] # массив из рандомных чисел (возможны повторения чисел)

#array = [i for i in range(SIZE)]
#shuffle(array)
print(array)

for i in range(1, len(array)):
    spam = array[i]
    j = i

    while array[j - 1] > spam and j > 0:
        array[j] = array[j - 1]
        j -= 1

    array[j] = spam

print(array)