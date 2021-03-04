#zd_26
    n = int(input("Введите число n: "))

    maxi = max(str(n))
    mini = min(str(n))
    print(f"Максимальная цифра числа {n}: {maxi}\nМинимальная цифра числа {n}: {mini}")

#zd_27
    n = int(input("Введите число n: "))

    maxi = max(str(n))
    mini = min(str(n))
    difference = int(max(str(n))) - int(min(str(n)))
    sum = int(max(str(n))) + int(min(str(n)))

    print(f"Максимальная цифра числа {n}: {maxi}\nМинимальная цифра числа {n}: {mini}")
    print(f"Максимальное число превышает минимальное число на {difference}")
    print(f"Сумма максимальной и минимальной цифр числа: {sum}")

