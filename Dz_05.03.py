#zd_26
n = int(input("Введите число n: "))
M = -1
#m = -1

maxi = max(str(n))
mini = min(str(n))
print(f"Максимальная цифра числа {n}: {maxi}\nМинимальная цифра числа {n}: {mini}")

While n > 0:
  p = n % 10
  if p > M:
    M = p
  n = n // 10
print(f"Максимальная цифра в числе {n}: {M}")

#While n > 0:
  #p = n % 10
  #if p < m:
    #m = p
  #n = n // 10
#print(f"Минимальная цифра в числе {n}: {m}")


#zd_27
n = int(input("Введите число n: "))
M = -1
m = 10

maxi = max(str(n))
mini = min(str(n))
difference = int(maxi) - int(mini)
sum = int(maxi) + int(mini)

print(f"Максимальная цифра числа {n}: {maxi}\nМинимальная цифра числа {n}: {mini}")
print(f"Максимальное число превышает минимальное число на {difference}")
print(f"Сумма максимальной и минимальной цифр числа: {sum}")

While n > 0:
  p = n % 10
  if p > M:
    M = p
  n = n // 10
print(f"Максимальная цифра в числе {n}: {M}")

#While n > 0:
  #p = n % 10
  #if p < m:
    #m = p
  #n = n // 10
#print(f"Минимальная цифра в числе {n}: {m}")

#if M > m:
  #S = int(M) - int(m)
#print(f"Максимальное число превышает минимальное число на {S}"

#if M > m:
  #s = int(M) + int(m)
#print(f"Сумма максимальной и минимальной цифр числа: {s}")


