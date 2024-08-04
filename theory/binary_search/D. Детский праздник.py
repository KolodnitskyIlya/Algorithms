'''
D. Детский праздник
ограничение по времени на тест 2 секунды
ограничение по памяти на тест 512 мегабайт
Организаторы детского праздника планируют надуть для него 𝑚 воздушных шариков. С этой целью они пригласили 𝑛
добровольных помощников, 𝑖-й среди которых надувает шарик за 𝑡𝑖 минут, однако каждый раз после надувания 𝑧𝑖 шариков
устает и отдыхает 𝑦𝑖 минут. Теперь организаторы праздника хотят узнать, через какое время будут надуты все шарики при
наиболее оптимальной работе помощников, и сколько шариков надует каждый из них. (Если помощник надул шарик, и должен
отдохнуть, но больше шариков ему надувать не придется, то считается, что он закончил работу сразу после окончания
надувания последнего шарика, а не после отдыха).

Входные данные
В первой строке входных данных задаются числа 𝑚 и 𝑛 (0≤𝑚≤15000,1≤𝑛≤1000). Следующие 𝑛 строк содержат по три целых
числа — 𝑡𝑖, 𝑧𝑖 и 𝑦𝑖 соответственно (1≤𝑡𝑖,𝑦𝑖≤100,1≤𝑧𝑖≤1000).

Выходные данные
Выведите в первой строке число 𝑇 — время, за которое будут надуты все шарики. Во второй строке выведите 𝑛 чисел —
количество шариков, надутых каждым из приглашенных помощников. Если распределений шариков несколько, выведите любое из
них.

Пример
входные данные
1 2
2 1 1
1 1 2
выходные данные
1
0 1
'''

'''
1  2  3  ...  zi  0
ti ti ti      ti  yi

(1 блок) zi * ti + yi - чтобы надуть zi шариков

xi / zi - проделаем блоки 
xi = 10, zi = 3

   3         3         3       1 
1 блок    2 блок    3 блок   

xi / zi * блок + (xi % zi) * ti
если xi % zi = 0, то формула будет вот такая xi / zi * блок - yi (чтобы не отдыхать после последнего шара)

x1 + x2 + ... + xn >= m
'''

def getCnt(T:int, t:int, z:int, y:int) -> int:
    cnt = 0
    block = z * t + y
    cntBlocks = T // block
    cnt += cntBlocks * z
    cnt += min((T % block) // t, z)
    return cnt

def ok(T:int, t:[], z:[], y:[]) -> bool:
    res = 0
    for i in range(len(t)):
        res += getCnt(T, t[i], z[i], y[i])
    return res

m, n = map(int, input().split())
t = []
z = []
y = []
for i in range(n):
    x1, x2, x3 = map(int, input().split())
    t.append(x1)
    z.append(x2)
    y.append(x3)

l = 0
r = 10**18
T = 0
while l <= r:
    mid = (l + r) // 2
    if ok(mid, t, z, y) >= m:
        r = mid - 1
        T = mid
    else:
        l = mid + 1
print(T)
for i in range(n):
    cnt = getCnt(T, t[i], z[i], y[i])
    print(min(m, cnt), end=' ')
    m -= cnt
    m = max(m, 0)