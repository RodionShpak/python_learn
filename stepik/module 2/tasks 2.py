
# // ###########################################################################################################################################################

# // // ==========================================Task-1
# Работа каких операторов дает верный ответ при любом значении переменной i?

# // //  --------------------===================== Сonditions =====================--------------------
# if i / 2:
#     print(i, 'чётное')
# else:
#     print(i, 'нечётное')
# if i // 2:
#     print(i, 'чётное')
# else:
#     print(i, 'нечётное')
# if i % 2 == 0:
#     print(i, 'чётное')
# else:
#     print(i, 'нечётное')
# if i // 2 == 0:
#     print(i, 'чётное')
# else:
#     print(i, 'нечётное')
# if i % 2 != 0:
#     print(i, 'нечётное')
# else:
#     print(i, 'чётное')
# if i // 2 != 0:
#     print(i, 'нечётное')
# else:
#     print(i, 'чётное')
# // //  --------------------===================== Tests =====================--------------------

# // //  --------------------===================== Result =====================--------------------
# 3, 5



# // ###########################################################################################################################################################

# // // ==========================================Task-2
# Пароль

# // //  --------------------===================== Сonditions =====================--------------------
# При регистрации на сайтах требуется вводить пароль дважды. 
# Это сделано для безопасности, поскольку такой подход уменьшает возможность неверного ввода пароля.

# Напишите программу, которая сравнивает пароль и его подтверждение. 
# Если они совпадают, то программа выводит: «Пароль принят», иначе: «Пароль не принят».

# Формат входных данных
# На вход программе подаются две строки.

# Формат выходных данных
# Программа должна вывести одну строку в соответствии с условием задачи.
# // //  --------------------===================== Tests =====================--------------------
# Тестовые данные 🟢
# Sample Input 1:
# qwerty
# qwerty

# Sample Output 1:
# Пароль принят

# Sample Input 2:
# qwerty
# Qwerty

# Sample Output 2:
# Пароль не принят

# Sample Input 3:
# PythonROCKS
# PythonROCKS

# Sample Output 3:
# Пароль принят
# // //  --------------------===================== Result =====================--------------------
# answer = input()
# answer2 = input()
# if answer == answer2:
#     print('Пароль принят')
# else:
#     print('Пароль не принят')



# // ###########################################################################################################################################################

# // // ==========================================Task-3
# Четное или нечетное?

# // //  --------------------===================== Сonditions =====================--------------------
# Напишите программу, которая определяет, является число четным или нечетным.
# Формат входных данных
# На вход программе подаётся одно целое число.
# Формат выходных данных
# Программа должна вывести «Четное», если число четное, и «Нечетное» — если число нечетное.

# // //  --------------------===================== Tests =====================--------------------
# Тестовые данные 🟢
# Sample Input 1:
# 10

# Sample Output 1:
# Четное

# Sample Input 2:
# 17

# Sample Output 2:
# Нечетное

# Sample Input 3:
# 0

# Sample Output 3:
# Четное

# // //  --------------------===================== Result =====================--------------------
# x = int(input())
# if x % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')



# // ###########################################################################################################################################################

# // // ==========================================Task-4
# Соотношение

# // //  --------------------===================== Сonditions =====================--------------------
# Напишите программу, которая проверяет, что для заданного четырехзначного числа выполняется следующее соотношение:
#  сумма первой и последней цифр равна разности второй и третьей цифр.
# Формат входных данных
# На вход программе подаётся одно целое положительное четырёхзначное число.
# Формат выходных данных
# Программа должна вывести «ДА», если соотношение выполняется, и «НЕТ» — если не выполняется.

# // //  --------------------===================== Tests =====================--------------------
# Тестовые данные 🟢
# Sample Input 1:
# 1614

# Sample Output 1:
# ДА

# Sample Input 2:
# 1234

# Sample Output 2:
# НЕТ

# Sample Input 3:
# 7911

# Sample Output 3:
# ДА

# // //  --------------------===================== Result =====================--------------------
# x = int (input ()) 
# a = x//1000%10 
# b = x//100%10 
# c = x//10%10 
# d = x%10 
# e = a + d 
# f = b - c 
# if e == f: 
#     print ("ДА") 
# else: 
#     print ("НЕТ")



# // ###########################################################################################################################################################

# // // ==========================================Task-5

# // //  --------------------===================== Сonditions =====================--------------------
# Напишите программу, которая определяет, разрешен пользователю доступ к интернет-ресурсу или нет.

# Формат входных данных
# На вход программе подаётся целое число — возраст пользователя.

# Формат выходных данных
# Программа должна вывести текст «Доступ разрешен» если возраст не менее 18, и «Доступ запрещен» в противном случае.

# // //  --------------------===================== Tests =====================--------------------
# Тестовые данные 🟢
# Sample Input 1:
# 16

# Sample Output 1:
# Доступ запрещен

# Sample Input 2:
# 18

# Sample Output 2:
# Доступ разрешен

# Sample Input 3:
# 19

# Sample Output 3:
# Доступ разрешен

# // //  --------------------===================== Result =====================--------------------
# age = int(input())
# if age >= 18:
#     print('Доступ разрешен')
# else:
#     print('Доступ запрещен')



# // ###########################################################################################################################################################

# // // ==========================================Task-6
# Арифметическая прогрессия

# // //  --------------------===================== Сonditions =====================--------------------
# Напишите программу, которая определяет, являются ли три заданных числа (в указанном порядке) 
# последовательными членами арифметической прогрессии.
# Формат входных данных
# На вход программе подаются три числа, каждое на отдельной строке.
# Формат выходных данных
# Программа должна вывести «YES» или «NO» (без кавычек) в соответствии с условием задачи. 

# // //  --------------------===================== Tests =====================--------------------
# Тестовые данные 🟢
# Sample Input 1:
# 1
# 2
# 3

# Sample Output 1:
# YES

# Sample Input 2:
# 1
# 2
# 4

# Sample Output 2:
# NO

# Sample Input 3:
# 2
# 4
# 8

# Sample Output 3:
# NO
# // //  --------------------===================== Result =====================--------------------

# a = int(input())
# b = int(input())
# c = int(input())
# if (b - a) + b == c:
#     print('YES')
# else:
#     print('NO')
#a - первое число, b - второе число, c - третье число,  ( b - a) - шаг , 
# чтобы понять является ли данная последовательность  арифметической прогрессией, 
# должно выполнятся условие: ( b - a) + b = c



# // ###########################################################################################################################################################

# // // ==========================================Task-7
# Наименьшее из двух чисел

# // //  --------------------===================== Сonditions =====================--------------------
# Напишите программу, которая определяет наименьшее из двух чисел.
# Формат входных данных
# На вход программе подаётся два различных целых числа.
# Формат выходных данных
# Программа должна вывести наименьшее из двух чисел.

# // //  --------------------===================== Tests =====================--------------------
# Тестовые данные 🟢
# Sample Input 1:
# 8
# 11

# Sample Output 1:
# 8

# Sample Input 2:
# 20
# 5

# Sample Output 2:
# 5

# // //  --------------------===================== Result =====================--------------------
# a = int(input())
# b = int(input())
# if a >= b:
#     print(b)
# else:
#     print(a)



# // ###########################################################################################################################################################

# // // ==========================================Task-8
# Наименьшее из четырёх чисел 🌶️

# // //  --------------------===================== Сonditions =====================--------------------
# Напишите программу, которая определяет наименьшее из четырёх чисел.
# Формат входных данных
# На вход программе подаётся четыре целых числа.
# Формат выходных данных
# Программа должна вывести наименьшее из четырёх чисел.

# // //  --------------------===================== Tests =====================--------------------
# Тестовые данные 🟢
# Sample Input 1:
# 1
# 2
# 3
# 4

# Sample Output 1:
# 1

# Sample Input 2:
# 10
# 9
# 11
# 12

# Sample Output 2:
# 9

# Sample Input 3:
# 100
# 200
# 5
# 300

# Sample Output 3:
# 5

# // //  --------------------===================== Result =====================--------------------
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# x = a
# if x > b:
#     x = b
# if x > c:
#     x = c
# if x > d:
#     x = d
# print(x)



# // ###########################################################################################################################################################

# // // ==========================================Task-9
# Возрастная группа

# // //  --------------------===================== Сonditions =====================--------------------
# Напишите программу, которая по введённому возрасту пользователя сообщает, к какой возрастной группе он относится:
# до 13 включительно – детство;
# от 14 до 24 – молодость;
# от 25 до 59 – зрелость;
# от 60 – старость.
# Формат входных данных
# На вход программе подаётся одно целое число – возраст пользователя.
# Формат выходных данных
# Программа должна вывести название возрастной группы.

# // //  --------------------===================== Tests =====================--------------------
# Тестовые данные 🟢

# Sample Input 1:
# 4

# Sample Output 1:
# детство

# Sample Input 2:
# 91

# Sample Output 2:
# старость

# Sample Input 3:
# 40

# Sample Output 3:
# зрелость

# // //  --------------------===================== Result =====================--------------------




























# // ###########################################################################################################################################################

# // // ==========================================Task-10

# // //  --------------------===================== Сonditions =====================--------------------

# // //  --------------------===================== Tests =====================--------------------

# // //  --------------------===================== Result =====================--------------------

# // // Before


# // // After