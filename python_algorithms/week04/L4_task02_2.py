# Перебор делителей

import cProfile

def prime_num2(n):
    lst = []   # список для хранения простых чисел
    for i in range(2, n+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst

# print(prime_num2(40))

# "L4_task02_2.prime_num2(10)"
# 1000 loops, best of 5: 8.43 usec per loop

# "L4_task02_2.prime_num2(20)"
# 1000 loops, best of 5: 21.8 usec per loop

# "L4_task02_2.prime_num2(30)"
# 1000 loops, best of 5: 35.3 usec per loop

# "L4_task02_2.prime_num2(40)"
# 1000 loops, best of 5: 50.7 usec per loop

# "L4_task02_2.prime_num2(100)"
# 1000 loops, best of 5: 200 usec per loop

# "L4_task02_2.prime_num2(1000)"
# 1000 loops, best of 5: 12.3 msec per loop
# Видно, что данный алгоритм сложнее, с использованием решета Аратосфена, также выполняется дольше по времени. Сложность алгоритма похожа на экспоненциальную.


# cProfile.run('prime_num2(10)')
# 8 function calls in 0.000 seconds

# cProfile.run('prime_num2(100)')
# 29 function calls in 0.000 seconds
# Здесь видно, что много раз вызывается функция append, видимо, из-за нее так сильно увеличивает время выполнения функции