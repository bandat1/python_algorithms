# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.

import cProfile
import random

def func1(n):
    array = [random.randint(-n, n) for i in range(n)]
    num = float('-inf')
    index = -1
    for i, item in enumerate(array):
        if 0 > item > num:
            num = item
            index = i

    print(array)
    return num

#print(func1(10))

# "L4_task01_1.func1(15)"
# 1000 loops, best of 5: 227 usec per loop

# "L4_task01_1.func1(30)"
# 1000 loops, best of 5: 378 usec per loop

# # "L4_task01_1.func1(45)"
# 1000 loops, best of 5: 469 usec per loop

# "L4_task01_1.func1(150)"
# 1000 loops, best of 5: 1.11 msec per loop
# Видно, что время выполнения данного алгоритма примерно равно тому, что было в первых двух. Все три алгоритма оказались, примерно, равнозначными.
# Вывод: учитывая количество строк кода и силы затрачиваемые на разработку, самый первый алгоритм является оптимальным.

# cProfile.run('func1(15)')
# 15    0.000    0.000    0.000    0.000 random.py:200(randrange)

#cProfile.run('func1(30)')
# 30    0.000    0.000    0.000    0.000 random.py:200(randrange)

# cProfile.run('func1(45)')
# 45    0.000    0.000    0.000    0.000 random.py:200(randrange)
# Аналогично предыдущим алгоритмам