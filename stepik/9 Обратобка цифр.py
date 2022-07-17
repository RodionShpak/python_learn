# Обработка цифр числа
# При помощи операции нахождения остатка и целочисленного деления можно достаточно несложно вычислить любую цифру числа.

# Рассмотрим программу получения цифр двузначного числа:

# num = 17
# a = num % 10
# b = num // 10
# print(a)
# print(b)
# Результатом выполнения программы будут два числа:

# 7
# 1
# То есть сначала мы вывели последнюю цифру числа, а затем первую цифру.

# Запомни: последняя цифра числа определяется всегда как остаток от деления числа на 10 (% 10). 
# Чтобы отщепить последнюю цифру от числа, необходимо разделить его нацело на 10 (// 10).

# Рассмотрим программу получения цифр трёхзначного числа:

# num = 754
# a = num % 10
# b = (num % 100) // 10
# c = num // 100
# print(a)
# print(b)
# print(c)
# Результатом выполнения программы будут три числа:

# 4
# 5
# 7
# То есть сначала мы вывели последнюю цифру числа, затем среднюю цифру, а затем первую цифру.

# Алгоритм получения цифр nn-значного числа
# Несложно понять, по какому алгоритму можно найти каждую цифру nn-значного числа num:

# Последняя цифра: (num % 101) // 100;
# Предпоследняя цифра: (num % 102) // 101;
# Предпредпоследняя цифра: (num % 103) // 102;
# .....
# Вторая цифра: (num % 10n-1) // 10n-2;
# Первая цифра: (num % 10n) // 10n-1.
# Решение задач
# Задача 1. Напишите программу, определяющую число десятков и единиц в двузначном числе.

# Решение. Число единиц – это последняя цифра числа, число десятков – первая цифра. 
# Чтобы получить последнюю цифру любого числа, нужно найти остаток от деления числа на 10. 
# Чтобы найти первую цифру двузначного числа, нужно поделить число нацело на 10. 
# Программа, решающая поставленную задачу, может иметь следующий вид:

# num = int(input())
# last_digit = num % 10
# first_digit = num // 10
# print('Число десятков =', first_digit)
# print('Число единиц =', last_digit)
# Задача 2. Напишите программу, в которой рассчитывается сумма цифр двузначного числа.

# Решение. Программа, решающая поставленную задачу, может иметь следующий вид:

# num = int(input())
# last_digit = num % 10
# first_digit = num // 10
# print('Сумма цифр =', last_digit + first_digit)
# Задача 3. Напишите программу, которая печатает число, образованное при перестановке цифр двузначного числа.

# Решение. Программа, решающая поставленную задачу, может иметь следующий вид:

# num = int(input())
# last_digit = num % 10
# first_digit = num // 10
# print('Искомое число =', last_digit * 10 + first_digit)
# Задача 4. Напишите программу, в которую вводится трёхзначное число и которая выводит на экран его цифры (через запятую).

# Решение. Программа, решающая поставленную задачу, может иметь следующий вид:

# num = int(input())
# digit3 = num % 10
# digit2 = (num // 10) % 10
# digit1 = num // 100
# print(digit1, digit2, digit3, sep=',')