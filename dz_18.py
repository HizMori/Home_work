A = list(map(int, input("Введите число: ")))
n = len(A)

B = sorted(A)
A = sorted(A, reverse = True)

print(*A, sep='')
print(*B, sep='')