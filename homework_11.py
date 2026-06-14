# 1. Звёздочки вместо чисел
# Напишите программу, которая заменяет все цифры в строке на звёздочки *.
# text = "My number is 123-456-789"
# Пример вывода:
# Строка: My number is 123-456-789
# Результат: My number is ***-***-***

# text = "My number is 123-456-789"
#
# for digit in "0123456789":
#     if digit in text:
#         text = text.replace(digit, "*")
#
# print(text)



# 2. Количество символов
# Напишите программу, которая подсчитывает количество вхождений всех
# символов в строке. Нужно вывести только символы, которые встречаются
# более 1 раза (игнорируя регистр), с указанием их количества. Выводите
# повторяющиеся символы только один раз.
# text = "Programming in python"
# Пример вывода:
# Строка: Programming in python
# Символ 'p' встречается 2 раз(а)
# Символ 'r' встречается 2 раз(а)
# Символ 'o' встречается 2 раз(а)
# Символ 'g' встречается 2 раз(а)
# Символ 'm' встречается 2 раз(а)
# Символ 'i' встречается 2 раз(а)
# Символ 'n' встречается 3 раз(а)
# Символ ' ' встречается 2 раз(а)

# text = "Programming in python".lower()
# printed_chars = []
#
# for char in text:
#     if char not in printed_chars:
#         count = text.count(char)
#         if count > 1:
#             print(f"Символ '{char}' встречается {count} раз(а)")
#             printed_chars.append(char)



# 3. Увеличение чисел
# Напишите программу, которая заменяет все числа в строке на их эквивалент, умноженный на 10.
# text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
# Пример вывода:
# I have 50.0 apples and 100.0 oranges, price is 5.0 each. Card number is ....3672.

# text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
#
# word_list = text.split()
#
# for index in range(len(word_list)):
#     word = word_list[index]
#
#     if word.count(".") > 1:
#         continue
#
#     # для универсальности, если бы были числа сразу перед знаками препинания
#     # и для отрицательных чисел
#     clean_word = word.rstrip(",.!?")
#     word_for_check = clean_word[1:] if (clean_word.startswith("-")
#                                         and clean_word.count("-") == 1) else clean_word
#
#     if word_for_check.replace(".", "", 1).isdigit():
#         new_value = str(float(clean_word) * 10)
#         word_list[index] = word.replace(clean_word, new_value)
#
# print(" ".join(word_list))