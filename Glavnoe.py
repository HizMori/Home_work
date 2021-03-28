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

import random

print(f'Целые числа на отрезке [a,b]: {random.randint(1,5)}')
print(f'Генератор на [0,1): {random.random()}')
print(f'Генератор на [a, b] (вещественные числа): {random.uniform(1.5, 10.5)}')
