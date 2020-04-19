# 4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

a = ord(input('Введите первую букву: '))
b = ord(input('Введите вторую букву: '))

index_a = a - ord('a') + 1
index_b = b - ord('a') + 1
letters_between_a_and_b = abs(index_b - index_a - 1)
print(f'Индекс буквы {chr(a)} равен: {index_a}.\nИндекс буквы {chr(b)} равен: {index_b}')
print(f'Между буквами {chr(a)} и {chr(b)} находится {letters_between_a_and_b} букв')
