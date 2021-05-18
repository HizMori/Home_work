#7
A = [int(x) for x in input("Введите числа: ").split()]

A.sort()
A.pop(0)

#или

n = len(A)

for i in range(n - 1):
    mini = i
    for j in range(i + 1, n):
        if A[j] < A[mini]:
            mini = j
    if i != mini:
        A[i], A[mini] = A[mini], A[i]

A.pop(0)

print(A)