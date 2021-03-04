def zd_26(n: int) -> None:
    n = int(input("Введите число n: "))
    print(f"Максимальная цифра числа {n}: {max(str(n))}\nМинимальная цифра числа {n}: {min(str(n))}")
def zd_27(n: int) -> None:
    n = int(input("Введите число n: "))
    print(f"Максимальная цифра числа {n}: {max(str(n))}\nМинимальная цифра числа {n}: {min(str(n))}")
    print(f"Максимальное число превышает минимальное число на {int(max(str(n))) - int(min(str(n)))}")
    print(f"Сумма максимальной и минимальной цифр числа: {int(max(str(n))) + int(min(str(n)))}")
def zd_23(n: int, a: int, z: int, x: int, y: int) -> None:
    n = int(input("Введите число n: "))
    a = int(input("Введите число a: "))
    z = int(input("Введите число z: "))
    x = int(input("Введите число x: "))
    y = int(input("Введите число y: "))
    print(f"В числе {n} встречаетсься цифра {a} {str(a).count(str(a))} раз")
    print(f"Цифр в числе {n} кратных {z}: {len([i for i in str(n) if int(i) % z == 0])}")
    print(f"Сумма его больших {a}: {len([i for i in str(n) if int(i) > a])}")
    print(f"Цифры {x} и {y} встречаются {str(x).count(str(x)) and str(y).count(str(y))} раз")