# Calculation of greater common divisor of two numbers

def gcd_1(m, n):
    while m != n:
        if m > n:
            m -= n
        elif n > m:
            n -= m
    return m
print(gcd_1(54, 24000))

def gcd_2(m, n):
    if n == 0:
        return m
    else:
        return gcd_2(n, m % n)

print(gcd_2(24, 914))

def gcd_3(m, n):
    while n != 0:
        m, n = n, m % n
    return m

print(gcd_3(24, 914))