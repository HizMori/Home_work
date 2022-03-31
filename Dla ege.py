# №2
'''
Логическая функция F задаётся выражением:
(¬x ∧ y ∧ z) ∨ (¬x ∧ ¬y ∧ z) ∨ (¬x ∧ ¬y ∧ ¬z).
На рисунке приведён фрагмент таблицы истинности функции F, содержащий все наборы аргументов, при которых функция F истинна.
Определите, какому столбцу таблицы истинности функции F соответствует каждая из переменных x, y, z.
'''

print("x y z")
for x in range(2):
    for y in range(2):
        for z in range(2):
            if ((not(x) and y and z) or (not(x) and not(y) and z) or (not(x) and not (y) and not(z))) == 1:
                print(x, y, z)

'''
Логическая функция F задаётся выражением (¬z)∧x ∨ x∧y. Определите, какому столбцу таблицы истинности функции F соответствует каждая из переменных x, y, z.
В ответе напишите буквы x, y, z в том порядке, в котором идут соответствующие им столбцы 
(сначала – буква, соответствующая 1-му столбцу; затем – буква, соответствующая 2-му столбцу; 
затем – буква, соответствующая 3-му столбцу). Буквы в ответе пишите подряд, никаких разделителей между буквами ставить не нужно.
'''

print("x y z")
for x in range(2):
    for z in range(2):
        for y in range(2):
            if ((not(z) and x) or (x and y)) == 1:
                print(x, y, z)

# №4
'''
Для кодирования букв И, Д, Т, О, X решили использовать двоичное представление чисел 0, 1, 2, 3 и 4 соответственно 
(с сохранением одного незначащего нуля в случае одноразрядного представления). 
Закодируйте последовательность букв ТИХОХОД таким способом и результат запишите шестнадцатеричным кодом.
'''

print(int("1000100111001101", base=2))
print(f"{35277:x}")

# №5
# 1
for n in range(1, 103):
    if n % 2 == 0:
        r = str(bin(n)) + "01"
    else:
        r = str(bin(n)) + "10"
    if int(r, 2) > 102:
        print(int(r, 2))
        break

# 2
'''
На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
1. Строится двоичная запись числа N.
2. К этой записи дописываются справа ещё два разряда по следующему правилу:
а) складываются все цифры двоичной записи, и остаток от деления суммы на 2 дописывается в конец числа (справа). 
Например, запись 10000 преобразуется в запись 100001;
б) над этой записью производятся те же действия — справа дописывается остаток от деления суммы цифр на 2.
Полученная таким образом запись (в ней на два разряда больше, чем в записи исходного числа N) 
является двоичной записью искомого числа R.
Укажите такое наименьшее число N, для которого результат работы алгоритма больше 77. 
В ответе это число запишите в десятичной системе счисления.
'''

for n in range(1, 78):
    r = str(bin(n))
    if r.count("1") % 2 == 0:
        r = str(bin(n)) + "00"
    else:
        r = str(bin(n)) + "10"
    if int(r, 2) > 77:
        print(n, int(r, 2))
        break

# 3

for i in range(10000, 100000):
    n = str(i)
    a = int(n[0]) + int(n[2]) + int(n[4])
    b = int(n[1]) + int(n[3])
    if min(a, b) == 7 and max(a, b) == 23:
        print(i)
        break

# 4

for i in range(1, 37):
    n = str(bin(i)[2:])
    if n.count("1") > n.count("0"):
        n += "1"
    else:
        n += "0"
    n = int(n, base=2)
    if n > 36:
        print(n)
        break

# №6
# 1
'''
Сколько существует положительных чисел, подаваемых на вход программе,
при которых программа в результате своей работы выведет на экран одно положительное число?

d = int(input())
n = 20
s = 40
while s + n < d:
  s = s – 10
  n = n - 20
print(n)
'''

for i in range(1, 10000):
    d = i
    n = 20
    s = 40
    while s + n < d:
        s = s - 10
        n = n - 20
    if n > 0:
        print(i)

#2
'''
Определите, при каком наименьшем введённом значении переменной s программа выведет число 256
'''

s1 = 1
while True:  # внешний цикл, бесконечный
    s = s1
    # --- код из условия задания ---
    n = 1
    while s <= 45:
        s = s + 4
        n = n * 2
    # --- конец кода из условия задания ---
    if n == 256:
        print(s1)
        break
    s1 += 1

#3
'''
Определите, при каком наибольшем введённом значении переменной s программа выведет число 96
'''

s1 = 50
while True:  # внешний цикл, бесконечный
    s = s1
    # --- код из условия задания ---
    n = 3
    while s <= 51:
        s = s + 7
        n = n * 2
    # --- конец кода из условия задания ---
    if n == 96:
        print(s1)
        break
    s1 -= 1

# №8
# 1
'''
Вася составляет 4-буквенные слова, в которых есть только буквы Л, Е, Т, О, причём буква Е используется в каждом слове хотя 
бы 1 раз. Каждая из других допустимых букв может встречаться в слове любое количество раз или не встречаться совсем.
Сколько существует таких слов, которые может написать Вася?
'''

n = 0
str = 'ЛЕТО'
for s1 in str:
  for s2 in str:
    for s3 in str:
      for s4 in str:
          if (s1+s2+s3+s4).count('Е') >= 1:
            n += 1
print(n)

# 2
'''
Олег составляет таблицу кодовых слов для передачи сообщений, каждому сообщению соответствует своё кодовое слово. 
В качестве кодовых слов Олег использует 5-буквенные слова, в которых есть только буквы A, Б, В, и Г, 
причём буква Г появляется не более одного раза и только на последнем месте. Каждая из других допустимых букв может 
встречаться в кодовом слове любое количество раз или не встречаться совсем.
Сколько различных кодовых слов может использовать Олег?
'''

n = 0
str = 'АБВГ'
for s1 in str:
  for s2 in str:
    for s3 in str:
      for s4 in str:
        for s5 in str:
          if s5 == "Г" and s4 != "Г" and s3 != "Г" and s2 != "Г" and s1 != "Г"\
                  or s5 != "Г" and s4 != "Г" and s3 != "Г" and s2 != "Г" and s1 != "Г":
            n += 1
print(n)

# №12
#1
'''
Исполнитель Редактор получает на вход строку цифр и преобразовывает её. Редактор может выполнять две команды, 
в обеих командах v и w обозначают цепочки цифр.
А) заменить (v, w)
Эта команда заменяет в строке первое слева вхождение цепочки v на цепочку w.
Б) нашлось (v)
Эта команда проверяет, встречается ли цепочка v в строке исполнителя Редактор. Если она встречается, 
то команда возвращает логическое значение «истина», в противном случае возвращает значение «ложь». 
Строка при этом не изменяется.
Какая строка получится в результате применения приведённой ниже программы к строке, состоящей из 90 идущих подряд 
цифр 3 и в конце одной цифры 1? В ответе запишите полученную строку.
НАЧАЛО
ПОКА нашлось (331) ИЛИ нашлось (166)
  ЕСЛИ нашлось (331)
    ТО заменить (331, 16)
    ИНАЧЕ заменить (166, 31)
  КОНЕЦ ЕСЛИ
КОНЕЦ ПОКА
КОНЕЦ
'''

s = 90*'3'+'1'
while "331" in s or "166" in s:
  if "331" in s:
    s = s.replace("331", "16", 1)
  else:
    s = s.replace("166", "31", 1)
print(s)

#2
'''
Исполнитель Редактор получает на вход строку цифр и преобразовывает её. 
Редактор может выполнять две команды, в обеих командах v и w обозначают цепочки цифр.
А) заменить (v, w)
Эта команда заменяет в строке первое слева вхождение цепочки v на цепочку w.
Б) нашлось (v)
Дана программа для исполнителя Редактор:
ПОКА нашлось (555) ИЛИ нашлось (333)
  ЕСЛИ нашлось (333)
    ТО заменить (333, 5)
    ИНАЧЕ заменить (555, 3)
  КОНЕЦ ЕСЛИ 
КОНЕЦ ПОКА 
Дана строка, состоящая из 500 цифр 5. Сколько пятёрок было удалено за время обработки строки по этой программе?
'''

s = 500*'5'
k = 0
while "555" in s or "333" in s:
  if "333" in s:
    s = s.replace("333", "5", 1)
  else:
    s = s.replace("555", "3", 1)
    k += 3
print(k)

# 3
'''
На вход приведённой ниже программе поступает строка, начинающаяся с символа «>», а затем содержащая 10 цифр 1, 20 цифр 2 и 30 цифр 3, расположенных в произвольном порядке.
Определите сумму числовых значений цифр строки, получившейся в результате выполнения программы.
Так, например, если результат работы программы представлял бы собой строку, состоящую из 50 цифр 4, то верным ответом было бы число 200.
НАЧАЛО
ПОКА нашлось (>1) ИЛИ нашлось (>2) ИЛИ нашлось (>3)
 ЕСЛИ нашлось (>1)
   ТО заменить (>1, 22>)
 КОНЕЦ ЕСЛИ
 ЕСЛИ нашлось (>2)
   ТО заменить (>2, 2>)
 КОНЕЦ ЕСЛИ
 ЕСЛИ нашлось (>3)
   ТО заменить (>3, 1>)
 КОНЕЦ ЕСЛИ
КОНЕЦ ПОКА
КОНЕЦ 
'''

a = '>' + '1'*10 + '2'*20 + '3'*30
while '>1' in a or '>2' in a or '>3' in a:
    if '>1' in a:
        a = a.replace('>1', '22>', 1)
    if '>2' in a:
        a = a.replace('>2', '2>', 1)
    if '>3' in a:
        a = a.replace('>3', '1>', 1)
a1 = a[:-1]
b = 0
for i in range(len(a1)):
    b += int(a[i])
print(b)

# №14
# 1
'''
Значение арифметического выражения
43∙7**103 – 21∙7**57 + 98
записали в системе счисления с основанием 7.
Найдите сумму цифр получившегося числа и запишите её в ответе в десятичной системе счисления.
'''

x = 43*7**103 - 21*7**57 + 98
s = 0
# в получившемся числе рассматриваем каждую цифру в 7-й системе сч.
while x:
    s += x % 7 # добавляем цифру к сумматору
    x //= 7 # убираем разряд числа в 7-й системе сч.
print(s)

# 2
'''
Значение арифметического выражения: 2**1024 + 4**64 - 64
записали в системе счисления с основанием 2.
Сколько цифр "1" содержится в этой записи?
'''

x = 2**1024 + 4**64 - 64
k = 0
# в получившемся числе рассматриваем каждую цифру в 2-й системе сч.
while x > 0:
    if x % 2 == 1: # если цифра = 1, то считаем ее
        k += 1
    x //= 2 # убираем разряд числа в 2-й системе сч.
print(k)

# 3
'''
Решите уравнение: 35_6 + x = 35_7
Ответ запишите в десятичной системе счисления.
'''

x = int('35', 7) - int('35', 6) # переводим в 10 сс и решаем
print(x)

# 4
'''
Решите уравнение:
204N+1 = 204N + 2616
В ответе укажите значение переменной N.
'''

for n in range(5, 20):
    if int('204', n+1) - int('204', n) == int('26', 16):
        print(n)

# №15
# 1
'''
Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m».
Для какого наименьшего натурального числа А формула
ДЕЛ(x, A) → (¬ДЕЛ(x, 28) ∨ ДЕЛ(x, 42))
тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной х)?
'''

for A in range(1, 50):
    OK = 1
    for x in range(1, 1000):
        OK *= (x % A == 0) <= ((x % 28 != 0) or (x % 42== 0))
    if OK:
        print(A)

# 2
'''
Укажите наименьшее значение А, при котором выражение
(y + 3x < A) ∨ (x > 20) ∨ (y > 40)
истинно для любых целых положительных значений x и y.
'''

for A in range(-100,200):
    OK = 1
    for x in range(1,100):
        for y in range(1,100):
            OK *= (y+3*x<A) or (x > 20) or (y > 40)
    if OK:
        print(A)

# №16
# 1
'''
Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:
F(0) = 1, F(1) = 1
F(n) = 2 * F(n–1) + F(n-2), при n > 1
Чему равно значение функции F(6)? В ответе запишите только целое число.
'''

def f(n):
    if n == 0:
        return 1
    if n == 1:
        return  1
    if n > 1:
        return 2*f(n-1)+f(n-2)
print(f(6))

# 2
'''
Алгоритм вычисления значений функций F(n) и G(n), где n – натуральное число, задан следующими соотношениями:
F(1) = 1; G(1) = 1;
F(n) = F(n–1) + 3·G(n–1), при n >=2 
G(n) = F(n–1) - 2·G(n–1), при n >=2
Чему равна сумма цифр значения F(18)?
'''

def F(n):
    if n == 1:
        return 1
    elif (n >= 2):
        return F(n - 1) + 3 * G(n - 1)
def G(n):
    if n == 1:
        return 1
    elif (n >= 2):
        return F(n - 1) - 2 * G(n - 1)
res = F(18)
s = 0
while res > 0:
    s += res % 10
    res = res // 10
print(s)

# №17
# 1
'''
Рассматривается множество целых чисел, принадлежащих числовому отрезку [5883; 15906], которые делятся
на 9 или 23 и не делятся на 13, 18, 19, 22.
Найдите количество таких чисел и максимальное из них.
В ответе запишите два целых числа без пробелов и других дополнительных символов:
сначала количество, затем максимальное число.
'''

A = [i for i in range(5883, 15906)
     if i % 9 == 0 or i % 23 == 0 and i % 13 != 0 and i % 18 != 0 and i % 19 != 0 and i % 22 != 0]
print(len(A), max(A)) #лучше так

# или

k = 0
m = -1
for i in range(5883, 15907):
    if (i % 9 == 0 or i % 23 == 0) and i % 13 != 0 and i % 18 != 0 and i % 19 != 0 and i % 22 != 0:
        k += 1
        m = max(m, i)
print(k, m)

# 2
'''
Определите количество принадлежащих отрезку [2 · 10^10; 4 · 10^10] натуральных чисел, которые делятся на
7 и на 100 000 и при этом не делятся на 13, 29, 43 и 101, а также наименьшее из таких чисел. 
В ответе запишите два целых числа без пробелов и других дополнительных символов: 
сначала количество, затем наименьшее число.
'''

A = [i for i in range(2*10**5, 4*10**5+1)
     if i % 7 == 0 and i % 13 != 0 and i % 29 != 0 and i % 43 != 0 and i % 101 != 0]
print(f"{len(A), min(A)}00000") #лучше так

k = 0
m = 1000000
for i in range(2*10**5, 4*10**5+1):
    if i % 7 == 0:
            if i % 13 != 0 and i % 29 != 0 and i % 43 != 0 and i % 101 != 0:
                k += 1
                m = min(m, i)
print(k, m) #незабыть 5 нулей на конце

# 3
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

k = 0
m = -1
for i in range(9999, 100000):
    if i % sumDigits(i) == 0:
        k += 1
        m = max(m, i)
print(k, m)

#или

A = [i for i in range(9999, 100000) if i % sumDigits(i) == 0]
print(len(A), max(A))

# 4
'''
Рассматривается множество целых чисел, принадлежащих числовому отрезку [256; 2566], 
которые делятся на 7 и не делятся на 21, 23, 31.
Найдите сумму таких чисел и максимальное из них.
В ответе запишите два целых числа: сначала сумму, затем максимальное число.
'''

A = [i for i in range(256, 2567) if i % 7 == 0 and i % 21 != 0 and i % 23 != 0 and i % 31 != 0]
print(sum(A), max(A))

#или

k = 0
m = -1
for i in range(256, 2567):
    if i % 7 == 0:
        if i % 21 != 0 and i % 23 != 0 and i % 31 != 0:
            k += i
            m = max(m, i)
print(k, m)

# 5
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
    for u in range(1, i+1):
        if i % u == 0:
            s2.add(u)
    if len(s1.intersection(s2)) == 2: #если в s2 есть ровно 2 делителя входящие в s1, то... (intersection - сравнение двух множеств)
        k += 1
        m = min(m, i)
print(k, m)

# 6
'''
Рассматривается множество целых чисел, принадлежащих числовому отрезку [3712; 8432], которые удовлетворяют следующим условиям:
− запись в двоичной и четверичной системах счисления заканчивается одинаковой цифрой;
− кратны 13, 14 или 15.
Найдите количество таких чисел и минимальное из них.
'''

k = 0
m = 10000
for i in range(3712, 8432):
    if (i % 13 == 0 or i % 14 == 0 or i % 15 == 0) and i % 2 == i % 4:
        k += 1
        m = min(m, i)
print(k, m)

# или

L = [x for x in range(3712, 8432+1) if (x % 13 == 0 or x % 14 == 0 or x % 15 == 0) and (x % 2 == x % 4)]
print(len(L), min(L))

# №19
'''
Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежат две кучи камней. 
Игроки ходят по очереди, первый ход делает Петя. 
За один ход игрок может добавить в одну из куч (по своему выбору) один камень или увеличить количество камней в куче в два раза. 
Игра завершается в тот момент, когда суммарное количество камней в кучах становится не менее 77. 
Победителем считается игрок, сделавший последний ход, т.е. первым получивший такую позицию, при которой в кучах будет 77 или больше камней. 
В начальный момент в первой куче было семь камней, во второй куче – S камней; 1 ≤ S ≤ 69.
'''
'''
Известно, что Ваня выиграл своим первым ходом после неудачного первого хода Пети. 
Укажите минимальное значение S, когда такая ситуация возможна.
'''

def F(a,b,h):
    if a+b>=77 and h==2: return True
    if a+b>=77 and h<2: return False
    if h>2: return False
    h=h+1
    if h%2==0: return F(a+1,b,h) or F(a*2,b,h) or F(a,b+1,h) or F(a,b*2,h)     #если ходит Ваня
    if h%2!=0: return F(a+1,b,h) or F(a*2,b,h) or F(a,b+1,h) or F(a,b*2,h)#у Пети неудачный ход учитываем и поэтому пишем or
for s in range (1,69+1):
    if F(7,s,0): print (s)

# №20
'''
Найдите два таких значения S, при которых у Пети есть выигрышная стратегия, причём одновременно выполняются два условия:
− Петя не может выиграть за один ход;
− Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.
'''

def F(a,b,h):
    if a+b>=77 and h==3: return True
    if a+b>=77 and h<3: return False
    if h>3: return False
    h=h+1
    if h%2!=0: return F(a+1,b,h) or F(a*2,b,h) or F(a,b+1,h) or F(a,b*2,h)     #если ходит Петя
    if h%2==0: return F(a+1,b,h) and F(a*2,b,h) and F(a,b+1,h) and F(a,b*2,h) #если ходит Ваня и не должен выиграть
for s in range (1,69+1):
    if F(7,s,0): print (s)

# №21
'''
Найдите минимальное значение S, при котором одновременно выполняются два условия:
– у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Пети;
– у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.
'''

def F(a,b,h):
    if a+b>=77 and (h==2 or h==4): return True
    if a+b>=77 and (h==1 or h==3): return False
    if h>4: return False
    h=h+1
    if h%2==0: return F(a+1,b,h) or F(a*2,b,h) or F(a,b+1,h) or F(a,b*2,h)
    if h%2!=0: return  F(a+1,b,h) and F(a*2,b,h) and F(a,b+1,h) and F(a,b*2,h)
for s in range (1,69+1):
    if F(7,s,0): print (s)