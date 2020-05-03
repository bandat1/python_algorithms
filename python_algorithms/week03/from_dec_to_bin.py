# Convertation from binary to dec type of number

def binary(num):
    s = ''
    while num > 0:
        s = f'{num % 2}' + s
        num //= 2
    return s

print(binary(5))