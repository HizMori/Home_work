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
