# 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input('Введите первое число. a = '))
b = int(input('Введите второе число. b = '))
c = int(input('Введите третье число. c = '))

if (a > b and a > c):
    if b > c:
        print(f"Среднее: {b}")
    else:
        print(f"Среднее: {c}")
else:
    if (b > a and b > c):
        if c > a:
            print(f"Среднее: {c}")
        else:
            print(f"Среднее: {a}")
    else:
        if a > b:
            print(f"Среднее: {a}")
        else:
            print(f"Среднее: {b}")