# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 13
# Задание необходимо решать через рекурсию

# Решение: 
# n = int(input("Введите число "))
# def fib(n):
#     if n in (0, 1):
#         return n
#     return fib(n - 1) + fib(n - 2)
# print(fib(n))

# Задача: 
# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# Решение 1:
# import random
# n = int(input("Введите число "))
# arr = [random.randint(1, 5) for x in range(n)]
# print(arr)
# maxx = max(arr)
# minn = min(arr)
# for i in range(n):
#     if arr[i] == maxx:
#         arr[i] = minn
# print(arr)


# Решение 2:
# import random
# n = int(input("Введите число "))
# arr = [random.randint(1, 5) for x in range(n)]
# print(arr)
# maxx = max(arr)
# minn = min(arr)
# for i,k in enumerate(arr):
#     if k == maxx:
#         arr[i] = minn
# print(arr)



# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)
# Input: 5
# Output: yes

# Решение (оптимизированное):
# import math
# n = int(input("Введите число на проверку "))
# def prime(n):
#     d = 2
#     while d < math.sqrt(n) + 1:
#         if n % d != 0:
#             d += 1
#         else:
#             return False
#     return True
# print(prime(n))

# Решение (простое):
# def check(num):
#     for i in range (2, num):
#         if num % i == 0:
#             return 'No'
#     return 'Yes'

# num = int(input("Введите число на проверку "))
# print(check(num))

# Задача №37
# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание.
# В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

# import random
# def rev(n):
# if n == 0:
# return " ! "
# x = random.randrange(n)
# print(x, end=" ")
# return rev(n - 1) + " " + str(x)
# print(rev(5))

# Д/З

# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

# def fun(a,b):
#     umnog = 1
#     for i in range(1, b+1):
#         if b <= 1:
#             return 1
#         umnog *= a
#     return umnog
    
# a = int(input("Введите число А: "))
# b = int(input("Введите число B: "))
# print(fun(a,b))

#Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций 
#допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4 

# def sum(a,b):
#     summa = a
#     for i in range(0, b):
#         if b == 0:
#             return 0
#         summa = summa + 1
#     return summa

# a = int(input("Введите число А: "))
# b = int(input("Введите число B: "))
# print(sum(a,b))
