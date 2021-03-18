# №1.1
import math

n = int(input('Введите чилсо: '))
r = math.factorial(n)

print(f'{n}! = {r}')

# №1.2
n = int(input('Введите чилсо: '))
r = 1

while n > 0:
    r *= n
    n -= 1

print(f'Факториал = {r}')

# №2
n = int(input('Введите число, возводимое в степень: '))
s = int(input('Введите степень: '))

n = pow(n, s)
print(n)