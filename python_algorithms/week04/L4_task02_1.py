# «Решето Эратосфена».

import cProfile

def prime_num1(n):
    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i * 2

            while j < n:
                sieve[j] = 0
                j += i

    result = [i for i in sieve if i != 0]
    return result

# print(prime_num1(40))

# "L4_task02_1.prime_num1(10)"
# 1000 loops, best of 5: 8.72 usec per loop

#"L4_task02_1.prime_num1(20)"
# 1000 loops, best of 5: 12.5 usec per loop

# "L4_task02_1.prime_num1(30)"
# 1000 loops, best of 5: 20.5 usec per loop

# "L4_task02_1.prime_num1(40)"
# 1000 loops, best of 5: 24.7 usec per loop

# "L4_task02_1.prime_num1(100)"
# 1000 loops, best of 5: 66.9 usec per loop

# "L4_task02_1.prime_num1(1000)"
# 1000 loops, best of 5: 813 usec per loop
# Видно, что время вычисления зависит пропорционально от входного числа. Сложность алгоритма близка к линейной.


# cProfile.run('prime_num1(10)')
# 6 function calls in 0.000 seconds

#cProfile.run('prime_num1(1000)')
# 6 function calls in 0.000 seconds
# Число вызовов каждой строки равно 1, не зависит от входных данных