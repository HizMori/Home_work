#zd_23
    n = int(input("Введите число n: "))
    a = int(input("Введите число a: "))
    z = int(input("Введите число z: "))
    x = int(input("Введите число x: "))
    y = int(input("Введите число y: "))

    print(f"В числе {n} встречаетсься цифра {a} {str(a).count(str(a))} раз")
    print(f"Цифр в числе {n} кратных {z}: {len([i for i in str(n) if int(i) % z == 0])}")
    print(f"Сумма его больших {a}: {len([i for i in str(n) if int(i) > a])}")
    print(f"Цифры {x} и {y} встречаются {str(x).count(str(x)) and str(y).count(str(y))} раз")

#zd_24
    numbers = map(int, input("Введите последовательность чисел: ").split(" "))
    x = int(input("Введите число x: "))

    print(f"Сумма всех чисел последовательности больше числа {x}: {sum([i for i in numbers if i > x])}")
    print(f"Кол-во всех чётных чисел последовательности: {len([i for i in numbers if i % 2 == 0])}")
    # numbers = map(int, input("Введите последовательность чисел: ").split(" "))
    # x = int(input("Введите число x: "))

    # print(f"Сумма всех чисел последовательности больше числа {x}: {sum([i for i in numbers if i > x])}")
    # print(f"Кол-во чётных чисел последовательности: {len([i for i in numbers if i % 2 == 0])}")

    #a = [1, 2, 3, 4, 5]
    #b = []
    #for x in a:
        #if x % 2 == 0:
            #b.append(x)

#zd_26
    n = int(input("Введите число n: "))

    print(f"Максимальная цифра числа {n}: {max(str(n))}\nМинимальная цифра числа {n}: {min(str(n))}")

    maxi = max(str(n))
    mini = min(str(n))
    print(f"Максимальная цифра числа {n}: {m}\nМинимальная цифра числа {n}: {e})

#zd_27

    n = int(input("Введите число n: "))

    print(f"Максимальная цифра числа {n}: {max(str(n))}\nМинимальная цифра числа {n}: {min(str(n))}")
    print(f"Максимальное число превышает минимальное число на {int(max(str(n))) - int(min(str(n)))}")
    print(f"Сумма максимальной и минимальной цифр числа: {int(max(str(n))) + int(min(str(n)))}")

    maxi = max(str(n))
    mini = min(str(n))
    difference = int(max(str(n))) - int(min(str(n)))
    sum = int(max(str(n))) + int(min(str(n)))

