# Сортировка пузырьком
from random import randint, shuffle

SIZE = 9
#array = [randint(0, 10) for i in range(SIZE)] # массив из рандомных чисел (возможны повторения чисел)

array = [i for i in range(SIZE)]
shuffle(array)
print(array)

k = 1
while k < len(array):
    for i in range(len(array) - k):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
            print(array)
    k += 1

print(array)