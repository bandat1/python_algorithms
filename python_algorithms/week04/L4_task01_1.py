# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.

import cProfile
import random

def func1(n):
    list1 = [random.randint(-n, n) for i in range(n)]
    list2 = [i for i in list1 if i < 0]

    num =list2[0]
    for i in list2:
        if i > num:
            num = i
    print(list1)
    return num

# print(func1(10))

# "L4_task01_1.func1(15)"
# 1000 loops, best of 5: 254 usec per loop

# "L4_task01_1.func1(30)"
# 1000 loops, best of 5: 358 usec per loop

# # "L4_task01_1.func1(45)"
# 1000 loops, best of 5: 436 usec per loop

# "L4_task01_1.func1(150)"
# 1000 loops, best of 5: 1.06 msec per loop
# Видно, что сложность алгоритма меньше, чем линейная, ближе к логарифмической.

# cProfile.run('func1(15)')
# 15    0.000    0.000    0.000    0.000 random.py:200(randrange)

#cProfile.run('func1(30)')
# 30    0.000    0.000    0.000    0.000 random.py:200(randrange)

# cProfile.run('func1(45)')
# 45    0.000    0.000    0.000    0.000 random.py:200(randrange)
# Видно, что затрачивается в основном ресурс на вызов функций из библиотеки random