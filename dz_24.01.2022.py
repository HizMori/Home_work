#5
for n in range(1, 70):
    n -= n % 4
    n = bin(n)[2:]
    n += str(n.count('1') % 2)
    n += str(n.count('1') % 2)
    r = int(n, 2)
    if r > 56:
        print(r)
        break

#6
for i in range(70, 1000):
    s = i
    n = 1
    while s*n < 4096:
        s = s // 2
        n = n * 4
    if n == 1024:
        print(i)