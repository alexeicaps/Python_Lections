# Task 20
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;


# word = input("Input word: ").upper()
# data = {"A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т": 1,
#         "D, G, Д, К, Л, М, П, У": 2,
#         'B, C, M, P, Б, Г, Ё, Ь, Я': 3
#         'F, H, V, W, Y, Й, Ы': 4
#         'K, Ж, З, Х, Ц, Ч': 5
#         'J, X, }
# result = 0
# for char in word:
#     for key in data:    # data.keys()    "A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т" (first key, after one itteration)
#         if char in data:
#             result += data[key]
# print(result)



# print(*[chr(i) for i in range(ord('a'), ord('z') + 1)]) вывод английского алфавита

# print('hel' in 'hello')


# Task 31
# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21









# Task 33
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# n = int(input("Input count marks: "))
# marks = [int(i) for i in input("Input marks: ").split()[:n]]
# print(*[min(marks) if i == max(marks) else i for i in marks])


# Task 35
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

# def is_prime(n):
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
#
# print('yes' if is_prime(int(input("Input number: "))) else 'no')


# Task 37
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

# def rec(n):
#     if n == 0:
#         return ''
#     x = int(input("Введите число: "))
#     return rec(n - 1) + f' {x}'
#
#
# n = int(input("Введите кол-во чисел: "))
# print(rec(n))
# # rec(2) -> x = 3 -> rec(1) + ' 3' = " 4" + " 3"
# #                      |
# #                    rec(0) + ' 4' = '' + " 4"
# #                      |
# #


# Task 26
# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

A = int(input())