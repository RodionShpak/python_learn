
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
# age = int(input())
# if age <= 13:
#     print('детство')
# if 14 <= age <= 24:
#     print('молодость')
# if 25 <= age <= 59:
#     print('зрелость')
# if 60 <= age:
#     print('старость')



# // ###########################################################################################################################################################

# // // ==========================================Task-10
# Только + 🌶️

# // //  --------------------===================== Сonditions =====================--------------------
# Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.

# Формат входных данных
# На вход программе подаются три целых числа.

# Формат выходных данных
# Программа должна вывести одно число – сумму положительных чисел.

# Примечание. Если положительных чисел нет, то следует вывести 00.

# // //  --------------------===================== Tests =====================--------------------
# Тестовые данные 🟢
# Sample Input 1:
# 4
# -22
# 1

# Sample Output 1:
# 5

# Sample Input 2:
# 33
# 55
# 63

# Sample Output 2:
# 151

# Sample Input 3:
# -1
# 37
# 62

# Sample Output 3:
# 99

# // //  --------------------===================== Result =====================--------------------
# a, b, c = int(input()), int(input()),int(input()) # ввод чисел
# if a < 0:
#     a = 0
# if b < 0:
#     b = 0
# if c < 0:
#     c = 0
# print (a + b + c)



# // ###########################################################################################################################################################

# // // ==========================================Task-11

# // //  --------------------===================== Сonditions =====================--------------------
# Допустим, что даны переменные a = 2, b = 4, c = 6. 
# Заполните таблицу, выбрав True или False, чтобы показать, является результатом такой комбинации истина или ложь.
# // //  --------------------===================== Tests =====================--------------------

# // //  --------------------===================== Result =====================--------------------

# Логическое выражение	True	False
# a == 2 or b > 2        V

# 6 <= c and a > 3                V	

# 1 != b and c != 3      V	

# a >= -1 or a <= b      V	

# not (a > 2)            V	

# not (c <= 10)                    V



# // ###########################################################################################################################################################

# // // ==========================================Task-12
# 
# // //  --------------------===================== Сonditions =====================--------------------
# Что будет выведено на экран в результате выполнения следующей программы?

# num1 = 34
# num2 = 81
# if num1 // 9 == 0 or num2 % 9 == 0:
#     print('число', num1, 'выиграло')
# else:
#     print('число', num2, 'выиграло')
# // //  --------------------===================== Tests =====================--------------------

# // //  --------------------===================== Result =====================--------------------
# число num1 выиграло

# число 81 выиграло

# число num2 выиграло

# число 34 выиграло                V



# // ###########################################################################################################################################################

# // // ==========================================Task-13

# // //  --------------------===================== Сonditions =====================--------------------
# Какое значение будет выведено на экран после выполнения следующей программы, если с клавиатуры введено число 7?

# a = int(input())
# if a >= 2 and a <= 17:
#     b = 3
#     p = a * a + b * b
# else:
#     b = 5
# p = (a + b) * (a + b)
# print(p)
# // //  --------------------===================== Tests =====================--------------------

# // //  --------------------===================== Result =====================--------------------
# 100



# // ###########################################################################################################################################################

# // // ==========================================Task-14
# Решение задач

# // //  --------------------===================== Сonditions =====================--------------------
# Задача 1. Напишите программу, которая определяет, является ли заданное натуральное число трёхзначным.

# Решение. Программа, решающая поставленную задачу, может иметь следующий вид:

# num = int(input())
# if 100 <= num <= 999:     # num >= 100 and num <= 999
#     print('Число является трёхзначным')
# else:
#     print('Число не является трёхзначным')

# Задача 2. Напишите программу, которая проверяет, что все три цифры натурального трёхзначного числа различны.

# Решение. Программа, решающая поставленную задачу, может иметь следующий вид:

# num = int(input())
# d3 = num % 10
# d2 = num % 100 // 10
# d1 = num // 100
# if d3 != d2 and d3 != d1 and d2 != d1:
#     print('Цифры различны')
# else:
#     print('Цифры не различны')
# Задача 3. Напишите программу, которая по координатам точки, не лежащей на осях координат, 
# определяет номер координатной четверти, в которой она находится.

# Решение. Программа, решающая поставленную задачу, может иметь следующий вид:

# x = int(input())
# y = int(input())

# if x > 0 and y > 0:
#     print('1 четверть')
# if x < 0 and y > 0:
#     print('2 четверть')
# if x < 0 and y < 0:
#     print('3 четверть')
# if x > 0 and y < 0:
#     print('4 четверть')

# // //  --------------------===================== Tests =====================--------------------
# Примечание. Обратите внимание: никакие два из четырёх условий не могут быть истинными одновременно.
# // //  --------------------===================== Result =====================--------------------

# // // Before


# // // After



# // ###########################################################################################################################################################

# // // ==========================================Task-15
# Принадлежность 1

# // //  --------------------===================== Сonditions =====================--------------------
# Напишите программу, которая принимает целое число xx и определяет, принадлежит ли данное число указанному промежутку. 

# Формат входных данных
# На вход программе подаётся целое число xx.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

# Примечание. Если точка выколотая, то граница не включается, если точка закрашенная, то граница включается.
# // //  --------------------===================== Tests =====================--------------------
# Тестовые данные 🟢
# Sample Input 1:
# 2

# Sample Output 1:
# Принадлежит

# Sample Input 2:
# -790

# Sample Output 2:
# Не принадлежит

# Sample Input 3:
# -1

# Sample Output 3:
# Не принадлежит

# // //  --------------------===================== Result =====================--------------------

# x = int(input())
# if -1 < x < 17:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')



# // ###########################################################################################################################################################

# // // ==========================================Task-16
# Принадлежность 2

# // //  --------------------===================== Сonditions =====================--------------------
# Напишите программу, которая принимает целое число xx и определяет, принадлежит ли данное число указанным промежуткам.

# Формат входных данных
# На вход программе подаётся целое число xx.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

# Примечание. Если точка выколотая, то граница не включается, если точка закрашенная, то граница включается. 

# // //  --------------------===================== Tests =====================--------------------
# Тестовые данные 🟢
# Sample Input 1:
# -44

# Sample Output 1:
# Принадлежит

# Sample Input 2:
# -3

# Sample Output 2:
# Принадлежит

# Sample Input 3:
# 5

# Sample Output 3:
# Не принадлежит

# // //  --------------------===================== Result =====================--------------------

# x = int(input())
# if -3 >= x or x >= 7:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')



# // ###########################################################################################################################################################

# // // ==========================================Task-17
# Принадлежность 3

# // //  --------------------===================== Сonditions =====================--------------------
# Напишите программу, которая принимает целое число xx и определяет, принадлежит ли данное число указанным промежуткам.

# Формат входных данных
# На вход программе подаётся целое число xx.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

# // //  --------------------===================== Tests =====================--------------------
# Примечание. Если точка выколотая, то граница не включается, если точка закрашенная, то граница включается. 

# Тестовые данные 🟢
# Sample Input 1:
# -332

# Sample Output 1:
# Не принадлежит

# Sample Input 2:
# -30

# Sample Output 2:
# Не принадлежит

# Sample Input 3:
# -21

# Sample Output 3:
# Принадлежит

# // //  --------------------===================== Result =====================--------------------

# x = int(input())
# if -30 < x <= -2 or 7 < x <= 25:
#      print('Принадлежит')
# else:
#      print('Не принадлежит')



# // ###########################################################################################################################################################

# // // ==========================================Task-18
# Красивое число 🌶️

# // //  --------------------===================== Сonditions =====================--------------------
# Назовем число красивым, если оно является четырехзначным и делится нацело на 77 или на 1717. 
# Напишите программу, определяющую, является ли введённое число красивым. 
# Программа должна вывести «YES», если число является красивым, или «NO» в противном случае.

# Формат входных данных
# На вход программе подаётся натуральное число.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

# // //  --------------------===================== Tests =====================--------------------
# Тестовые данные 🟢
# Sample Input 1:
# 1043

# Sample Output 1:
# YES

# Sample Input 2:
# 1045

# Sample Output 2:
# NO

# Sample Input 3:
# 2751

# Sample Output 3:
# YES
# // //  --------------------===================== Result =====================--------------------

# num = int(input())
# if (1000 <= num <= 9999) and ((num % 7 == 0) or (num % 17 == 0)):     
#     print('YES')
# else:
#     print('NO')



# // ###########################################################################################################################################################

# // // ==========================================Task-19
# Неравенство треугольника

# // //  --------------------===================== Сonditions =====================--------------------
# Напишите программу, которая принимает три положительных числа и определяет, существует ли невырожденный треугольник с такими сторонами.

# Формат входных данных
# На вход программе подаётся три положительных целых числа.

# Формат выходных данных
# Программа должна вывести «YES» или «NO» в соответствии с условием задачи.

# Примечание. Треугольник существует, если выполняется неравенство треугольника.

# // //  --------------------===================== Tests =====================--------------------
# Тестовые данные 🟢
# Sample Input 1:
# 5
# 2
# 3

# Sample Output 1:
# NO

# Sample Input 2:
# 3
# 4
# 6
# Sample Output 2:
# YES

# Sample Input 3:
# 8
# 2
# 4

# Sample Output 3:
# NO

# // //  --------------------===================== Result =====================--------------------
# a = int(input())
# b = int(input())
# c = int(input())
# if (a < b + c) and (b < c + a) and (c < a + b):   
#      print('YES')
# else:
#      print('NO')



# // ###########################################################################################################################################################

# // // ==========================================Task-20
# Високосный год

# // //  --------------------===================== Сonditions =====================--------------------
# Напишите программу, которая определяет, является ли год с данным номером високосным. 
# Если год является високосным, то выведите «YES», иначе выведите «NO».

# Год является високосным, если его номер кратен 4, но не кратен 100, или если он кратен 400.

# Формат входных данных
# На вход программе подаётся натуральное число.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

# // //  --------------------===================== Tests =====================--------------------
# Тестовые данные 🟢
# Sample Input 1:
# 2020

# Sample Output 1:
# YES

# Sample Input 2:
# 2012

# Sample Output 2:
# YES

# Sample Input 3:
# 2009

# Sample Output 3:
# NO

# // //  --------------------===================== Result =====================--------------------

# year = int(input())
# if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
#     print('YES')
# else:
#     print('NO')

























# // ###########################################################################################################################################################

# // // ==========================================Task-21

# // //  --------------------===================== Сonditions =====================--------------------

# // //  --------------------===================== Tests =====================--------------------

# // //  --------------------===================== Result =====================--------------------

# // // Before


# // // After