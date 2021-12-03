#p-03
# 1

def f(n):
    global s
    s += 2*n
    if n > 1:
        s += n-5
        f(n-1)
        f(n-2)

for i in range(10000):
    s = 0
    f(i)
    if s > 500000:
        print(i, s)
        break

# 2

def f(n):
    global s
    s += 2*n
    if n > 1:
        s += n-5
        return s+f(n-1)+f(n-2)
    return s

n = 0

while True:
    s = 0
    n += 1
    f(n)
    if s > 500000:
        print(n, s)
        break

#Ответ: 24 531864

#p-02

s = []

def f(n):
    s.append('*')
    if n >= 1:
        s.append('*')
        f(n-1)
        f(n-2)
        f(n-3)

f(22)
print(len(s)) #Ответ: 1957585

#p-01

def f(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return n + 2 + f(n-1)
    else:
        return 2 * f(n-2)

print(f(24)) #Ответ: 2074