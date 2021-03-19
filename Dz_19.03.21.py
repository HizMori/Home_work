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

# №3
n = input('Введите число: ')
s = input('Введите цифру, которую хотите убрать: ')

n = n.replace(s, '')

print(n)

'''
n = int(input('Введите число: '))
s = int(input('Введите цифру, которую хотите убрать: '))

m = []
while n > 0:
  m.append(n % 10)
  n = n // 10
else:
    m.remove(s)
    m = (''.join(map(str, m)))

print(m)
'''
