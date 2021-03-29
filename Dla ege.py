# №17

'''
Рассматривается множество целых чисел, принадлежащих числовому отрезку [5883; 15906], которые делятся
на 9 или 23 и не делятся на 13, 18, 19, 22.
Найдите количество таких чисел и максимальное из них.
В ответе запишите два целых числа без пробелов и других дополнительных символов:
сначала количество, затем максимальное число.
'''

n = 5883
k = 0
m = -1
while n != 15906:
    if n % 9 == 0 or n % 23 == 0:
        if n % 13 != 0 and n % 18 != 0 and n % 19 != 0 and n % 22 != 0:
            k += 1
            m = max(m, n)
    n += 1
print(k, m)

'''
Определите количество принадлежащих отрезку [2 · 10^10; 4 · 10^10] натуральных чисел, которые делятся на
7 и на 100 000 и при этом не делятся на 13, 29, 43 и 101, а также наименьшее из таких чисел. 
В ответе запишите два целых числа без пробелов и других дополнительных символов: 
сначала количество, затем наименьшее число.
'''

n = 2*10**5
k = 0
m = 1000000
while n != 4*10**5:
    if n % 7 == 0:
            if n % 13 != 0 and n % 29 != 0 and n % 43 != 0 and n % 101 != 0:
                k += 1
                m = min(m, n)
    n += 1
print(k, m) #незабыть 5 нулей на конце

'''
Рассматривается множество целых чисел, принадлежащих числовому отрезку [9999; 99999], которые кратны сумме своих цифр. 
Найдите количество таких чисел и максимальное из них. В ответе запишите два целых числа: 
сначала количество, затем – максимальное число.
'''

def sumDigits(e):
    sumi = 0
    while e != 0:
        sumi += e % 10
        e = e // 10
    return sumi


n = 9999
k = 0
m = -1
while n != 99999:
    if n % sumDigits(n) == 0:
        k += 1
        m = max(m, n)
    n += 1
print(k, m)

#или

k = 0
m = 0
for i in range(9999, 99999 + 1):
    if i % sumDigits(i) == 0:
        k = k + 1
        m = i
print(k, m)

'''
Рассматривается множество целых чисел, принадлежащих числовому отрезку [256; 2566], 
которые делятся на 7 и не делятся на 21, 23, 31.
Найдите сумму таких чисел и максимальное из них.
В ответе запишите два целых числа: сначала сумму, затем максимальное число.
'''

k = 0
m = -1
for i in range(256, 2567):
    if i % 7 == 0:
        if i % 21 != 0 and i % 23 != 0 and i % 31 != 0:
            k += i
            m = max(m, i)
print(k, m)

'''
Назовём натуральное число подходящим, если ровно два из его делителей входят в список (11, 13, 17, 19). 
Определите количество подходящих чисел, принадлежащих отрезку [11000; 22000], 
а также наименьшее из таких чисел. В ответе запишите два целых числа: 
сначала количество, затем, без разделительных знаков, наименьшее число.
'''

k = 0
m = 34000
s1 = {11, 13, 17, 19}

for i in range(11000, 22001):
    s2 = set() #создаём пустое множество
    for u in range(1, i + 1):
        if i % u == 0:
            s2.add(u)
    if len(s1.intersection(s2)) == 2: #если в s2 есть ровно 2 делителя входящие в s1, то... (intersection - сравнение двух множеств)
        k += 1
        m = min(m, i)
print(k, m)