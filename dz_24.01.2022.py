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

#14
a = 5**2019 - 5**2019 + 25**600 - 125
print(a)
d = ''
while a > 0:
    d += f'{a % 5}'
    a = a // 5
print(d)
print(d.count('4')-1)

#15

a = 18
b = 81
for i in range(1, 1000):
    if i % a == 0 and i % b == 0:
        print(i)
        break

#16
def f(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return n + 2 * f(n - 1)
    if n % 2 != 0 and n > 1:
        return 1 + 3 * f(n - 2)

print(f(17))

#22
for i in range(1000):
    x = i
    q = 15
    l = 0
    while x >= q:
        l += 1
        x -= q
    m = x
    if m < l:
        m = l
        l = x
    if l == 3 and m == 7:
        print(i)

#23
def f(x, y):
    if x < y:
        return 0
    if x == y:
        return 1
    if x > y:
        return f(x-1, y)+f(x//2, y)

print(f(30, 10)*f(10, 1))

#19

v = lambda f: ((f[0]+2, f[1]), (f[0]*2, f[1]), (f[0], f[1]+2), (f[0], f[1]*2))

a = 2
s = 35
for x in v((a, s)):
    for y in v((x[0], x[1])):
        if sum(x) >= 142:
            print(f'{(a, s)} -> {x} - Победил Петя')
            break
        if sum(y) >= 142:
            print(f'{(a, s)} -> {x} -> {y} - Победил Ваня')
            break