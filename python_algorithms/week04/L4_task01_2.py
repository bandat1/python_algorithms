# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.

import cProfile
import random

def func1(n):
    array = [random.randint(-n, n) for i in range(n)]
    i = 0
    index = -1

    while i < n:
        if array[i] < 0 and index == -1:
            index = i
        elif array[i] < 0 and array[i] > array[index]:
            index = i

        i += 1
    print(array)
    return array[index]

#print(func1(10))

# "L4_task01_1.func1(15)"
# 1000 loops, best of 5: 262 usec per loop

# "L4_task01_1.func1(30)"
# 1000 loops, best of 5: 393 usec per loop

# # "L4_task01_1.func1(45)"
# 1000 loops, best of 5: 471 usec per loop

# "L4_task01_1.func1(150)"
# 1000 loops, best of 5: 1.16 msec per loop
# Видно, что время выполнения данного алгоритма примерно равно тому, что было в первом файле. Алгоритмы равнозначны.

# cProfile.run('func1(15)')
# 15    0.000    0.000    0.000    0.000 random.py:200(randrange)

#cProfile.run('func1(30)')
# 30    0.000    0.000    0.000    0.000 random.py:200(randrange)

# cProfile.run('func1(45)')
# 45    0.000    0.000    0.000    0.000 random.py:200(randrange)
# Аналогично предыдущему алгоритму.