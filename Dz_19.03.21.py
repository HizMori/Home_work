# №1
import math

n = int(input('Введите чилсо: '))
r = math.factorial(n)

print(f'{n}! = {r}')

# №2
n = int(input('Введите число:'))
s = int(input('Введите степень:'))

if s > 0:
    for i in range(s):
        n *= n