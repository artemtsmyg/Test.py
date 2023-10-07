# Напишите программу, которая проверяет, является ли число числом Армстронга.
# Число Армстронга — натуральное число, которое в данной системе счисления равно сумме своих цифр, возведённых в степень, равную количеству его цифр.
# Пример: 3**3 + 7**3 + 1**3 = 371


def is_armstrong_number(number):
    # Преобразуем число в строку, чтобы посчитать количество цифр
    num_str = str(number)

    # Получаем количество цифр в числе
    num_digits = len(num_str)

    # Вычисляем сумму цифр, возведенных в степень num_digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)

    # Проверяем, является ли число числом Армстронга
    return armstrong_sum == number


# Пример использования:
number = int(input("Введите число: "))
if is_armstrong_number(number):
    print(f"{number} - это число Армстронга.")
else:
    print(f"{number} - это не число Армстронга.")


    # Напишите программу, которая проверит, что число является совершенным.
    # Совершенное число - натуральное число, равное сумме всех своих собственных делителей.
    # Например, число 6 равно сумме своих собственных делителей 1 + 2 + 3.
    # Примеры совершенных чисел: 6, 28, 496, 8128

def is_perfect_number(number):
    # Инициализируем сумму делителей
    divisors_sum = 0

    # Итерируемся по всем целым числам от 1 до (number - 1)
    for i in range(1, number):
        # Если i является делителем number, добавляем его к сумме
        if number % i == 0:
            divisors_sum += i

    # Проверяем, является ли число совершенным
    return divisors_sum == number


# Пример использования:
number = int(input("Введите число: "))
if is_perfect_number(number):
    print(f"{number} - это совершенное число.")
else:
    print(f"{number} - это не совершенное число.")


# Напишите программу, которая переведет десятичное число в двоичное.

def decimal_to_binary(decimal_number):
    # Инициализируем пустую строку для хранения двоичного представления
    binary_result = ""

    # Пока десятичное число больше 0
    while decimal_number > 0:
        # Получаем остаток от деления на 2 (0 или 1)
        remainder = decimal_number % 2

        # Преобразуем остаток в строку и добавляем его в начало результата
        binary_result = str(remainder) + binary_result

        # Делаем целочисленное деление на 2
        decimal_number = decimal_number // 2

    return binary_result


# Пример использования:
decimal_number = int(input("Введите десятичное число: "))
binary_result = decimal_to_binary(decimal_number)
print(f"Двоичное представление: {binary_result}")



# Напишите программу, которая найдет количество вхождений подстроки в строку.
# Подстроки могут перекрываться


def count_overlapping_substrings(main_string, substring):
    count = 0
    start = 0
    while start < len(main_string):
        start = main_string.find(substring, start)
        if start == -1:
            break
        count += 1
        start += 1
    return count

main_string = input("Введите основную строку: ")
substring = input("Введите подстроку: ")

result = count_overlapping_substrings(main_string, substring)
print(f"Количество вхождений подстроки в строку: {result}")

#