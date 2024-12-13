#print("Hallo world")

#name = 'Alex'
#print('Привет, меня зовут', name)
#print(f'Привет, меня зовут {name}')
#print('Привет,', 'меня', 'зовут', name)
#text = 'Привет, меня зовут'
#print(text, name)


#name = input()
#surname = input()
#print(f'Привет, меня зовут {name.title()} {surname.title()}')

#a = int(input())
#b = int(input())
#rezult = a + b
#print(rezult)

#a, b = int(input()), int(input())
#c = a + b
#print(c)

# # Перебор всех возможных значений для n, k и m
# for n in range(1, 13):  # n может быть от 1 до 12
#     for k in range(0, 13 - n):  # k может быть от 0 до 12 - n
#         m = 12 - n - k  # Вычисляем m из второго уравнения
#         if 28 * n + 30 * k + 31 * m == 365:
#             print(f"n = {n}, k = {k}, m = {m}")
#             break  # Найдено решение, выходим из цикла
# Имеется
# 100
# 100 рублей. Сколько быков, коров и телят можно купить на все эти деньги, если плата за быка –
# 10
# 10 рублей, за корову –
# 5
# 5 рублей, за теленка –
# 0.5
# 0.5 рубля и надо купить
# 100
# 100 голов скота?
# for b in range(0, 101):  # Количество быков от 0 до 100
#     for c in range(0, 101 - b):  # Количество коров от 0 до (100 - b)
#         t = 100 - b - c  # Вычисляем количество телят
#         # Проверяем, удовлетворяет ли система уравнений
#         if 10 * b + 5 * c + 0.5 * t == 100:
#             print(f"Быков: {b}, Коров: {c}, Телят: {t}")
from itertools import combinations_with_replacement
import time
#
# def fifth_power(x):
#     return x ** 5
#
# # Создаем словарь для хранения пятой степени чисел
# fifth_powers = {i: fifth_power(i) for i in range(1, 151)}
#
# # Создаем обратный словарь для быстрого поиска
# inverse_fifth_powers = {v: k for k, v in fifth_powers.items()}

# Поиск решения
# start_time = time.time()
#
# for a in range(1, 151):
#     a5 = fifth_powers[a]
#     for b in range(a, 151):
#         b5 = fifth_powers[b]
#         for c in range(b, 151):
#             c5 = fifth_powers[c]
#             for d in range(c, 151):
#                 d5 = fifth_powers[d]
#                 sum_of_powers = a5 + b5 + c5 + d5
#                 if sum_of_powers in inverse_fifth_powers:
#                     e = inverse_fifth_powers[sum_of_powers]
#                     if e >= d:  # Убедиться, что e не меньше d
#                         print(f"a = {a}, b = {b}, c = {c}, d = {d}, e = {e}")
#                         print(f"Sum = {a + b + c + d + e}")
#                         end_time = time.time()
#                         print(f"Time taken: {end_time - start_time} seconds")
#                         exit()
# day = input()
# if day == 'sunday' or day == 'saturday':
#     print('today is weekend')
# elif day == 'wensday':
#     print('Today i have an appointment')
# else:
#     print('Usual day')

# n = int(input())
# text = input()
# for i in range(n):
#     print(text)

# message = input()
# count = 0
# for i in message:
#     if i == 'a' or i == 'u' or i == 'e' or i == 'i' or i == 'o':
#         count += 1
# print(count)

# n = int(input())
# count = 0
# while n > 0:
#     count = n + n
# print(count)
#
# def sum_of_divisors(n):
#     total = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             total += i
#     return total
#
# # Ввод данных
# a, b = map(int, input().split())
#
# max_sum = 0
# result_number = a
#
# for num in range(a, b + 1):
#     current_sum = sum_of_divisors(num)
#     if (current_sum > max_sum) or (current_sum == max_sum and num > result_number):
#         max_sum = current_sum
#         result_number = num
#
# # Вывод результата
# print(result_number)


# sums_of_cubes = {}
#
# # Максимальное значение для проверки (достаточно большое для нахождения первых 5 чисел)
# max_value = 100
#
# # Перебор всех пар чисел
# for a in range(1, max_value):
#     for b in range(a, max_value):
#         cube_sum = a ** 3 + b ** 3
#
#         if cube_sum in sums_of_cubes:
#             sums_of_cubes[cube_sum].append((a, b))
#         else:
#             sums_of_cubes[cube_sum] = [(a, b)]
#
# # Список для хранения интересных чисел
# interesting_numbers = []
#
# # Поиск чисел, которые могут быть представлены как сумма двух кубов двумя разными способами
# for cube_sum, pairs in sums_of_cubes.items():
#     if len(pairs) > 1:  # Должно быть как минимум 2 разные пары
#         interesting_numbers.append(cube_sum)
#
# # Сортируем и берем первые 5 интересных чисел
# interesting_numbers = sorted(set(interesting_numbers))
# first_five_interesting_numbers = interesting_numbers[:5]
#
# # Выводим результаты
# print("Первые 5 интересных чисел:")
# for number in first_five_interesting_numbers:
#     print(number)
