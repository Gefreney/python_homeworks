# 1. Прогрессия увеличения
# Напишите программу, которая создаёт новый кортеж, состоящий
# из элементов изначального в том же порядке. Добавить в него только
# элементы, которые больше всех предыдущих значений в исходном кортеже.
# Данные:
# numbers = (3, 7, 2, 8, 5, 10, 1)
# Пример вывода:
# Кортеж по возрастанию: (3, 7, 8, 10)

# numbers = (3, 7, 2, 8, 5, 10, 1)
# tmp_list = [numbers[0]]
# max_number = numbers[0]
#
# for index in range(1, len(numbers)):
#     number = numbers[index]
#
#     if number > max_number:
#         tmp_list.append(number)
#         max_number = number
#
# result = tuple(tmp_list)
# print(result)



# 2. Повторяющиеся элементы
# Напишите программу, которая находит индексы элементов кортежа,
# встречающихся более одного раза. Вывести сами элементы и их индексы.
# Данные:
# numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
# Пример вывода:
# Индексы элемента 2: 1 4 9
# Индексы элемента 3: 2 6
# Индексы элемента 4: 3 8

# numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
#
# # вариант 1
# suitable_numbers = []
# number_indices = []
#
# for index, number in enumerate(numbers):
#     if number not in suitable_numbers:
#         if numbers.count(number) > 1:
#             suitable_numbers.append(number)
#             number_indices.append([])
#         else:
#             continue
#
#     number_indices[suitable_numbers.index(number)].append(index)
#
# for number in suitable_numbers:
#     print(f"Индексы элемента {number}: ", *number_indices[suitable_numbers.index(number)])
#
# # вариант 2
# processed_numbers = []
#
# for index, number in enumerate(numbers):
#     if not number in processed_numbers and number in numbers[index + 1:]:
#         indices = []
#         for idx, num in enumerate(numbers):
#             if num == number:
#                 indices.append(idx)
#
#         print(f"Индексы элемента {number}: ", *indices)
#         processed_numbers.append(number)