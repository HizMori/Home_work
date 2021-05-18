A = list(map(int, input("Введите число: ")))

B = sorted(A)
A = sorted(A, reverse = True)

print(*A, sep='')
print(*B, sep='')