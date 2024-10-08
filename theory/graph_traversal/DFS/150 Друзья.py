'''
(Время: 1 сек. Память: 16 Мб Сложность: 41%)
В клубе N человек. Многие из них - друзья. Так же известно, что друзья друзей так же являются друзьями. Требуется выяснить, сколько всего друзей у конкретного человека в клубе.

Входные данные
В первой строке входного файла INPUT.TXT заданы два числа: N и S (1 ≤ N ≤ 100; 1 ≤ S ≤ N), где N - количество человек в клубе, а S – номер конкретного человека. В следующих N строках записано по N чисел - матрица смежности, состоящая из единиц и нулей. Причем единица, стоящая в i-й строке и j-м столбце гарантирует, что люди с номерами i и j – друзья, а 0 – выражает неопределенность.

Выходные данные
В выходной файл OUTPUT.TXT выведите количество гарантированных друзей у человека с номером S, помня о транзитивности дружбы.

Пример
INPUT.TXT	OUTPUT.TXT
3 1         2
0 1 0
1 0 1
0 1 0
'''

n, s = map(int, input().split())
a = []
for i in range(n):
    b = list(map(int, input().split()))
    a += [b]
ans = 0
used = [False] * n
def dfs(v, used):
    used[v] = True
    global ans
    ans += 1
    for to in range(n):
        if a[v][to] == 1 and used[to] == False:
            dfs(to, used)
dfs(s - 1, used)
print(ans - 1)