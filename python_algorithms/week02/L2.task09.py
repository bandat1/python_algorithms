# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

num = int(input('Введите натуральное число (ноль - выйти): '))
max_sum, max_num = 0, 0
while num != 0:
    temp_num = num
    temp_sum = 0
    while num > 0:
        temp_sum += num % 10
        num //= 10
    if temp_sum > max_sum:
        max_num = temp_num
        max_sum = temp_sum
    num = int(input('Введите натуральное число (ноль - выйти): '))
print(f'Число {max_num} имеет максимальную сумму цифр, равную {max_num}')