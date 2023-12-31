# Task 1
# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# # (т.е. не меньше заданного минимума и не больше заданного максимума).
# # На вход подается список с элементамиlist_1 и границы диапазона в виде чисел min_number, max_number.
# # Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# # Вывод: [1, 9, 13, 14, 19]
#
# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# list_2 = []
# max = 10
# min = 0
# for i in range(len(list_1)):
#     if list_1[i] >= min and list_1[i] <= max:
#         list_2.append(i)
# print(*list_2, sep='\n')

# или   -------------------------------

# for i in range(len(list_1)):
#   if min <= list_1[i] <= max:
#     print(i)


# Task 2
# Заполните массив элементами арифметической прогрессии. Её первый элемент a1 , разность d и количество
# элементов n будет задано автоматически. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# На входе:

# a1 = 7
# d = 2
# n = 5
# res = []
# for i in range(n):
#     i = a1 + i * d
#     res.append(i)
#     i += 1
# print(*res, sep='\n')