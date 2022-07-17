Ввод данных, команда input
Все предыдущие программы выводили на экран текст, известный в момент написания программного кода. Однако программы могут работать с данными, которые станут известны только во время выполнения программы. Другими словами, программы могут считывать данные, а затем их использовать.

Для считывания данных в языке Python используется команда input().

Рассмотрим следующую программу:

print('Как тебя зовут?')
name = input()
print('Привет,', name)
Сначала программа распечатает текст на экран «Как тебя зовут?». Далее программа будет ждать от пользователя ввода данных. Ввод данных реализуется с помощью команды input().

Команда input() всегда пишется с круглыми скобками. Она работает так: когда программа доходит до места, где есть input(), она ждет, пока пользователь введёт текст с клавиатуры (ввод завершается нажатием клавиши Enter). Введенная строка подставляется на место input().

То есть, если вы ввели строку «Parrot», программа дальше будет работать так, как будто на месте input() было написано «Parrot».

Таким образом, input() получает от пользователя какие-то данные и вместо вызова подставляет строковое значение, в нашем случае записывает его в качестве значения переменной name.

Что такое переменные и что значит сохранить в переменной значение, подробнее поговорим чуть позже, а пока запоминаем:

Команда print() выводит на экран данные.

Команда input() считывает введенные с клавиатуры данные.

Примечания
Примечание. Очень часто перед считыванием данных мы печатаем некоторый текст, чтобы пользователь, который вводит эти данные понимал, что именно от него требуется. Например, в программе

print('Как тебя зовут?')
name = input()
print('Привет,', name)
мы сначала выведем текст «Как тебя зовут?», а уже потом считаем данные.

Поскольку это достаточно распространённый сценарий, то в языке Python можно выводить текст, передавая его в качестве параметра в команду input(). Предыдущий код можно переписать так:

name = input('Как тебя зовут?')
print('Привет,', name)