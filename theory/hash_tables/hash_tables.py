'''
Python - те самые dict(словарь)

есть какая-то строка

s1
s2
s3
...
sn

хотим очень быстро узнать, есть ли строка t в нашем наборе строк:
1) По тупому каждую строку сравниваем с t - O(n * max(len si))
2) Словари!!!!!!!!!!!
O(1) - вставка ключа
O(1) - поиск ключа
'''
my_dict = {}

s = ['abc', 'wq', 'xyz', 'qwe']

for st in s:
    my_dict[st] = True

print(my_dict)

t = 'abc'
if t in my_dict:
    print('Yes')
else:
    print('No')

print('--------------------------------')

my_dict = {}
s = ['abc', 'abc', 'qw', 'qw', 'qw', 'y']

for st in s:
    if st in my_dict:
        my_dict[st] += 1
    else:
        my_dict[st] = 1

print(my_dict)

print('--------------------------------')

a = (1, 2, 3)
my_dict[a] = True
print(my_dict)