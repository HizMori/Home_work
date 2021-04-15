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
#/////
from random import  randint

print('Введите границы диапазона:')
a, b = map(int, input().split())
A = [randint(a, b) for i in range(10)]
print(*A)

#////
from random import  randint

print('Введите границы диапазона:')
a, b = sorted(int(i) for i in input().split())
A = [randint(a, b) for i in range(10)]

print(*A)

#////
from random import  randint

print('Введите границы диапазона:')
a, b = sorted(int(i) for i in input().split())
A = []

for i in range(10):
    A.append(randint(a, b) if i < 5
             else pow(A[i - 5], 2))
print(*A)

#///
print('Массив:')
A = [int(i) for i in input().split()]
print(f'Среднее арифметическое {sum(A)/len(A)}')

#///
from random import  randint

print('Массив:')
A = [randint(0, 101) for i in range(10)]
for a in A:
  print (a, end = " ")

for i in A:
    if i < 50:
        a = sum(A) / len(A)
        A.remove(i)
    else:
        b = sum(A) / len(A)
print(f'\nСр. арифм. элементов < 50: {a}\nСр. арифм. элементов >=50: {b}')