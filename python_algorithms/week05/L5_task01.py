# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль
# (за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import deque

plant_amount = int(input('Введите число предприятий: '))
dic = {}
sum = 0 #для посчета суммы прибыли по всем предприятиям
i = 1
while i <= plant_amount:
    plants = input('Введите название предприятия:')
    income = int(input('Введите его прибыль за 4-ре квартала:'))
    dic[plants] = income
    i += 1
    sum += income

avg = round(sum / plant_amount, 2)
print(f'Средняя прибыль по предприятиям в год = {avg}')

less_avg = deque() # предприятия, чья прибыль ниже среднего
more_avg = deque() # предприятия, чья прибыль выше среднего
for plants in dic:
    if dic[plants] > avg:
        more_avg.append(plants)
    elif dic[plants] < avg:
        less_avg.append(plants)

print(f'Предприятия, чья прибыль ниже среднего: {less_avg}')
print(f'Предприятия, чья прибыль выше среднего: {more_avg}')