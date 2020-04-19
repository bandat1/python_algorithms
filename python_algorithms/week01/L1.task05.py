# 5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

a = int(input("Введете число: "))

letter_ord = a + ord('a') - 1
letter = chr(letter_ord)

print(letter)