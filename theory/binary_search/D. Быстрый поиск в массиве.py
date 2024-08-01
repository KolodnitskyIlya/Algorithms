'''
D. Быстрый поиск в массиве
ограничение по времени на тест 2 секунды
ограничение по памяти на тест 512 мегабайт
Дан массив 𝑎 из 𝑛 целых чисел 𝑎1,𝑎2,…,𝑎𝑛.

Нужно уметь отвечать на запросы вида «Сколько чисел имеют значения от 𝑙 до 𝑟»?

Входные данные
В первой строке находится целое число 𝑛 (1≤𝑛≤10^5) — длина массива.

Во второй строке находятся 𝑛 целых чисел 𝑎1,𝑎2,…,𝑎𝑛 (−10^9≤𝑎𝑖≤10^9).

В третьей строке находится целое число 𝑘 (1≤𝑘≤10^5) — число запросов.

В следующих 𝑘 строках находятся пары чисел 𝑙 𝑟 (−10^9≤𝑙≤𝑟≤10^9).

Выходные данные
Выведите 𝑘 чисел — ответы на запросы.

Пример
входные данные
5
10 1 10 3 4
4
1 10
2 9
3 4
2 2
выходные данные
5 2 2 0
'''

n = int(input())
list_number = list(map(int, input().split()))
list_number.sort()
requests = int(input())

def low(list_number, mid, start):
    return list_number[mid] >= start

def up(list_number, mid, end):
    return list_number[mid] <= end

for i in range(requests):
    start, end = map(int, input().split())

    l = 0
    r = n - 1
    L = 0
    while l <= r:
        mid = (l + r) // 2
        if low(list_number, mid, start):
            r = mid - 1
            L = mid
        else:
            l = mid + 1

    l = 0
    r = n - 1
    R = n - 1
    while l <= r:
        mid = (l + r) // 2
        if up(list_number, mid, end):
            l = mid + 1
            R = mid
        else:
            r = mid - 1

    if start > list_number[n - 1] or end < list_number[0]:
        print(0, end=' ')
    else:
        print(R - L + 1, end=' ')

