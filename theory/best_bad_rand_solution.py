# СТРЕСС ТЕСТЫ
'''
-> best_solution (не уверены) <---------------
                                              |    ans_best
-> bad_solution (уверены на 101%) <-----      |       ||
                                       |      |    ans_bad
-> rand (генерация случайных тестов) ----------
                                  ? ans_best = ans_bad
'''

# найти сумму на подотрезках
arr = [1, -1, 5, 7, 8, -5]

# best_solution O(n) (префиксная сумма) можно допустить какой-нибудь баг
'''
P(i) (сумма отрезков от 0 до i) = arr[0] + arr[1] + ... + arr[i] -------- O(n)

Найти сумму на отрезке эйлера (дают запрос Эйлера)
l, r -> P(r) - P(l-1)   O(1)
'''

# bad_solution O(n^2)
'''
Пишем два встроенных цикла
l, r -> l <= i <= r
        sum += arr[i]
'''

# rand - генерация arr; l, r


from random import randint

def best_solution(arr, quarry):
    # O(m)
    n = len(arr)
    prefix_sum = [0] * n
    prefix_sum[0] = arr[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]

    ans = []

    for i in range(len(quarry)):
        l, r = quarry[i]
        sum_l_r = prefix_sum[r]
        if l - 1 >= 0:
            sum_l_r -= prefix_sum[l - 1]
        ans.append(sum_l_r)

    return ans

def bad_solution(arr, querry):
    # O(m * n)
    ans = []
    for i in range(len(querry)):
        l, r = querry[i]
        sum_l_r = 0
        for j in range(l, r + 1):
            sum_l_r += arr[j]
        ans.append(sum_l_r)

    return ans

def check(arr, querry):
    if best_solution(arr, querry) != bad_solution(arr, querry):
        print('arr = ', arr)
        print('querry =', querry)
        print('best_solution =', best_solution(arr, querry))
        print('bad_solution =', bad_solution(arr, querry))
        raise Exception("Wrong")
    #print('OK')

def main():
    n = 4
    m = 5

    arr = []
    # заполняем массив arr рандомными числами
    for i in range(n):
        arr.append(randint(-5, 5))

    querry = [] # массив хранящий пары эйлера(запросы)
    for i in range(m):
        l = randint(0, n - 1)
        r = randint(l , n - 1)
        # l <= r
        querry.append([l, r])
    check(arr, querry)



if __name__ == "__main__":
    for i in range(100):
        main()
    print('OK')