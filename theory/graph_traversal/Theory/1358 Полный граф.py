'''
(Время: 1 сек. Память: 16 Мб Сложность: 22%)
Неориентированный граф с кратными рёбрами называется полным, если любая пара его различных вершин соединена хотя бы одним ребром.

Для заданного списком рёбер графа проверьте, является ли он полным.

Входные данные
Первая строка входного файла INPUT.TXT содержит натуральные числа N и M – число вершин и рёбер в графе соответственно (N ≤ 100, M ≤ 10 000). Далее, в последующих M строках следует M пар чисел U и V, описывающих рёбра графа (U≠V).

Выходные данные
В выходной файл OUTPUT.TXT выведите «YES», если граф является полным, и «NO» в противном случае.

Пример
INPUT.TXT	OUTPUT.TXT
5 18        YES
1 2
1 3
1 3
1 4
1 4
1 4
1 5
1 5
2 3
2 4
2 4
2 5
3 4
3 4
3 4
3 5
3 5
4 5
'''

# N, M = map(int, input().split())
# graph_list = [[] for _ in range(N)]
#
# for i in range(M):
#     u, v = map(int, input().split())
#     if v not in graph_list[u - 1]:
#         graph_list[u - 1].append(v)
#     if u not in graph_list[v - 1]:
#         graph_list[v - 1].append(u)
#
# ans = "YES"
#
# for i in range(N):
#     if len(graph_list[i]) != N - 1:
#         ans = "NO"
#         break
# print(ans)

N, M = map(int, input().split())
graph_list = [{} for _ in range(N)]

for i in range(M):
    u, v = map(int, input().split())
    graph_list[u - 1][v] = 1
    graph_list[v - 1][u] = 1

ans = "YES"

for i in range(N):
    if len(graph_list[i]) != N - 1:
        ans = "NO"
        break
print(ans)
