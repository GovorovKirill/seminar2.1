# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

print('введите число')

n = int(input())

degree = 2

while degree <= n:
    print(degree)
    degree *= 2

