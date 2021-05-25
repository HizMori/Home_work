#7
A = [int(x) for x in input().split()]

A.sort()
A.remove(0)

#или

n = len(A)

for i in range(n - 1):
    mini = i
    for j in range(i + 1, n):
        if A[j] < A[mini]:
            mini = j
    if i != mini:
        A[i], A[mini] = A[mini], A[i]

A.remove(0)

print(*A)

#9
a = list(map(int, input().split()))
n = a[0]
a.pop(0)

for i in range(n):
    if a[-i] >= 0:
        n += 0
    else:
        a.pop(-i)
        n -= 1

a.sort()
a.insert(0, n)
print(*a)

#10
def sumDigits(n):
    if n < 10: return n
    d = n % 10
    sumi = d + sumDigits(n // 10)
    return sumi
print(sumDigits(int(input())))