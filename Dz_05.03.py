#zd_24
numbers = list(map(int, input("Введите последовательность чисел: ").split()))
x = int(input("Введите число x: "))

for i in numbers
    if i > x:
        print(f"Сумма всех чисел последовательности больше числа {x}: {sum}")
sum = sum([i for i in numbers if i > x])
quantity = len([i for i in numbers if i % 2 == 0])

print(f"Сумма всех чисел последовательности больше числа {x}: {sum}")
print(f"Кол-во всех чётных чисел последовательности: {quantity}")

#zd_26
n = int(input("Введите число n: "))

maxi = max(str(n))
mini = min(str(n))
print(f"Максимальная цифра числа {n}: {m}\nМинимальная цифра числа {n}: {e}")

#zd_27

n = int(input("Введите число n: "))

maxi = max(str(n))
mini = min(str(n))
difference = int(max(str(n))) - int(min(str(n)))
sum = int(max(str(n))) + int(min(str(n)))

print(f"Максимальная цифра числа {n}: {maxi}\nМинимальная цифра числа {n}: {mini}")
print(f"Максимальное число превышает минимальное число на {difference}")
print(f"Сумма максимальной и минимальной цифр числа: {sum}")

