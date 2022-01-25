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

#12
a = '1' * 70
while '1111' in a or '2222' in a:
    if '1111' in a:
        a = a.replace('1111', '22', 1)
    if '2222' in a:
        a = a.replace('2222', '11', 1)
print(a)