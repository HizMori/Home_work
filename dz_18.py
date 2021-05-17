A = list(map(int, input("Введите число: ")))
n = len(A)

B = sorted(A)

for i in range(0, n - 1):
    for j in range(0, n - 1):
        if A[j+1] > A[j]:
            A[j + 1], A[j] = A[j], A[j + 1]

print(*A, sep='')
print(*B, sep='')