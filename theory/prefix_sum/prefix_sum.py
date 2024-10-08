'''
arr = [. . . . . . . .]
подотрезок l,r (0 <= l <= r < n)
Найти сумму чисел в массиве arr на подотрезке l, r:

1) Можно пройтись циклом с позиции l до r и найти эту сумму - O(n)
Но если у нас будет не один подотрезок, а m штук:
(l1, r1) = arr[l1] + ... + arr[r1]
(l2, r2) = arr[l2] + ... + arr[r2]
...
(lm, rm) = arr[lm] + ... + arr[rm]
Сложность уже будет - O(n * m) - ой как плохо будет на контесте, сервер в Яндексе не вывезет => БАН

2) Префиксная сумма
P[i] = arr[0] + arr[1] + ... + arr[i] (O(n))
P[0] = arr[0]
P[1] = arr[0] + arr[1] = P[0] + arr[1]
P[i] = P[i-1] + arr[i]
Мы можем заранее, когда получаем масcив arr, запомнить префиксную сумму (P[i])
Дальше нам дают m отрезков: например (l1, r1) = P[r1] - P[l1-1] = arr[l1] + ... + arr[r1] (ответ на 1 запрос - O(1))
Сложность будет - O(n) - быстрейшее решение
Префиксную сумму можно использовать при неизменяемом arr, если же массив изменяется то про префиксную сумму лучше забыть
'''