'''
(Время: 1 сек. Память: 16 Мб Сложность: 20%)
По матрице смежности графа необходимо определить: является ли он ориентированным графом без петель? Напомним, что граф с симметричной матрицей смежности является неориентированным.

Входные данные
Первая строка входного файла INPUT.TXT содержит натуральное число N (N ≤ 100) – число вершин графа. Далее следуют N строк по N цифр, каждая из которых равна 0 или 1, задающих матрицу смежности.

Выходные данные
В выходной файл OUTPUT.TXT выведите «YES», если граф отвечает требованиям в условии, в противном случае выведите «NO».

Примеры
INPUT.TXT
4
0 1 1 0
1 0 1 0
0 1 0 1
1 0 0 0

OUTPUT.TXT
YES

INPUT.TXT
5
0 0 1 0 0
0 0 1 0 1
1 1 0 0 0
0 0 0 0 0
0 1 0 0 0

OUTPUT.TXT
NO
'''

N = int(input())
graph_list = [[] * N for _ in range(N)]
graph_list_prov = [[0] * N for _ in range(N)]

petlya = False

for i in range(N):
    u_v = list(map(int, input().split()))
    graph_list[i] = u_v
    if u_v[i] == 1:
        petlya = True
        break
    for j in range(i, N):
        if u_v[j]:
            graph_list_prov[i][j] = 1
            graph_list_prov[j][i] = 1

if graph_list_prov != graph_list and not petlya:
    print('YES')
else:
    print('NO')











