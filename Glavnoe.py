print(f'Форматный вывод: \nДля дробей: {123.4566:.2f}; {1264563.454565466:,.2f} \nМодуль числа: {abs(-12)} \nОкругление: {round(2.3)} \nЦело число: {int(13.23)} \nПеревод в двоичную систему исчисления: {14:b} \nПеревод восьмеричную систему исчисления: {14:o} \nПеревод шестнадцатиричную систему исчисления: {14:x}')

print(f'Для строк:')
welcome = "Hello {:s}"
name = "Katya"
print(welcome.format(name))

print('Для целых чисел:')
source = "{:d} символов"
print(source.format(5))

source = "{:,d} символов"
print(source.format(5000))

print(f'Проценты: {12345:.3%}')
number = .12345
print("{:.2%}".format(number))

a, b = map(int, input('Ввод нескольких переменных в сторку: ').split())
print(a, b)

print('import math - подключение математического модуля')

import math
print(f'Число «пи»: {math.pi}')
print(f'Квадратный корень: {math.sqrt(4)}')
print(f'Синус угла, заданного в радианах: {math.sin(45)}')
print(f'Косинус угла, заданного в радианах: {math.cos(45)}')
print(f'Округление «вниз»: {math.floor(15.6)}')
print(f'Округление «вверх»: {math.ceil(15.4)}')
print(f'{math.factorial(4)}')

from random import *

print(f'Целые числа на отрезке [a,b]: {randint(1,5)}')
print(f'Генератор на [0,1): {random()}')
print(f'Генератор на [a, b] (вещественные числа): {uniform(1.5, 10.5)}')

#Счётчик
n = int(input('Счётчик: '))
m = 0
while n > 0:
    n = n // 10
    m += 1
print(m)

#Максимальная и минимальная цифра числа
n = int(input('Введите число n: '))
M = -1

maxi = max(str(n))
mini = min(str(n))
print(f"Максимальная цифра числа {n}: {maxi}\nМинимальная цифра числа {n}: {mini}")

while n > 0:
  d = n % 10
  if d > M:
    M = d
  n = n // 10
print(f"Максимальная цифра в числе: {M}")

#Алгоритм Евклида (НОД)
q = int(input('Первое число: '))
w = int(input('Второе число: '))

while q != w:
    if q > w:
        q -= w
    else:
        w -= q

print(f'НОД({q},{w}) = {q}')

#Поиск простого числа
count = 0
k = 2
j = int(input('Введи число больше 4: '))

while k*k <= j:
    if j % k == 0:
        print('False')
    k += 1
if k*k > j:
    print('True') #Так себе вариант

def prostoe(x):
    s = int(x**0.5)
    for i in range(2, s+1):
        if x % i == 0:
            return False
    return True
print(prostoe(12)) #Лучше этот вариант