print(f'Форматный вывод:')
print(f'Для дробей: {123.4566:.2f} или {1264563.454565466:,.2f}')
print(f'Модуль числа: {abs(-12)}')
print(f'Округление: {round(2.3)}')
print(f'Цело число: {int(13.23)}')
print(f'Перевод в двоичную систему исчисления: {14:b}')
print(f'Перевод восьмеричную систему исчисления: {14:o}')
print(f'Перевод шестнадцатиричную систему исчисления: {14:x}')
print(f'Создание массива: {[i for i in range(10)]} или {list(range(10))} или {[int(input()) for i in range(2)]} или {list(map(int, input().split()))}')

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
print(f'Факториал числа: {math.factorial(4)}')

from random import *

print(f'Целые числа на отрезке [a,b]: {randint(1,5)}')
print(f'Генератор на [0,1): {random()}')
print(f'Генератор на [a, b] (вещественные числа): {uniform(1.5, 10.5)}')

print("(x and y) - логическое и, ^; (x or y) - логическое или, ∨; not(x) - логическое не, ¬x; "
      "(not(x) or y) - логическое слндование, (x → y); ")

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
print(f'Максимальная цифра числа: {max(str(n))}\nМинимальная цифра числа: {min(str(n))}')

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


def NOD(a, b):
    if a == 0 or b == 0:
        return a+b
    if a > b:
        return NOD(a - b, b)
    else:
        return NOD(a, b - a)

a = int(input('Первое число: '))
b = int(input('Второе число: '))

print(f'НОД({a},{b}) = {NOD(a, b)}')

def NOD(a, b):
  if b == 0: return a
  return NOD(b, a % b)

a = int(input('Первое число: '))
b = int(input('Второе число: '))

print(f'НОД({a},{b}) = {NOD(a, b)}')

#Поиск простого числа

count = 0
k = 2
j = int(input('Введи число больше 2: '))

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

#Перевод в другие системы исчисления

n = 178
k = 128
while k > 0:
    print(n // k, end = "")
    n = n % k
    k = k // 2

def printBin(h):
    k = 128
    while k > 0:
        print(h // k, end = "")
        h = h % k
        k = k // 2
print(printBin(178))

def printBin ( n ):
    if n == 0: return
    printBin(n // 2)
    print(n % 2, end = "")


#Сумма цифр чисел

def sumDigits(e):
    sumi = 0
    while e != 0:
        sumi += e % 10
        e = e // 10
    return sumi
print(sumDigits(123))

def sumDigits(n):
    if n < 10: return n
    d = n % 10
    sumi = d + sumDigits(n // 10)
    return sumi
print(sumDigits(567))

#Проверка на чётность

def even(z):
  if z % 2 == 0:
    return True
  else:
    return False
print(even(12))

#Фибиначи

f1 = 1
f2 = 1
for i in range(3, 10):
    f3 = f1 + f2
    print(f3)
    f1, f2, = f2, f3

#Ханойские башни

def Hanoi ( n, k, m ):
    if n == 0: return
    p = 6 - k - m
    Hanoi(n-1, k, p)
    print(k, "->", m)
    Hanoi(n-1, p, m)
Hanoi(2, 1, 3)

#Перебор элементов в мвссиве

A =[1, 2, 3]
n = 0
for x in A:
    if x < 10:
        n += 1
print(n)

