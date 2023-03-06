#	Что такое функция?
'''
Функция - область в которую помещается определенный код , который в дальнейшем будем вызываться,
 для избежения возможного повторения кода.
'''

#	Цели и задачи функции.
'''
Функции нужны чтобы можно было повысить читабельность вашего кода,
не переполняя его не нужными повторениями. 
'''
#	Встроенные функции.
'''
max() - находит максимальное число,
min() - находит минимальное число
len() - длина строк и коллекций
reversed() 
sorted()
int() 
float()
str()
bool()
print()
input()

sum()
eval() - переводит выржание в строке, в целочисленную операцию
pow() - возводит в степень
ord() - определял номер символа по таблице АСКИ
oct() - восьмиричное представление
bin() - двоичное представление 
hex() - шестнадцатеричное представление
abs() - модуль числа
fabs() - модуль только целочисленных данных

map() - выполняет какое-либо действие с итерируемыемыми данными 
filter() - ____
zip() - ____
reduce() - ____
'''

#	Математические функции и случайные числа.
'''
import math
import random
'''

#Синтаксис объявления функций.
'''
def имя_функүии(параметры):
    инструция/тело функции
 '''
#Аргументы и возвращаемые значения
# аргументы - то что указывается при создании функции
# параметры -то, что передается в качестве аргунтов для функции
'''
Виды функций:
1)ничего не принимает ничего не возвращает
2) при входе принимает но ничего не возвращает
3) ничего не принимает но возвращает
4)принимает и возвращает
'''
#1)ничего не принимает ничего не возвращает
'''def foo():
    print('Hello world')
foo()'''

#2)при входе принимает но ничего не возвращает
'''def print_numbers_in_sequences(number, number2,number3):
    summ= number+number2+number3
    print(summ)

print_numbers_in_sequences(150130,1715,12)
print_numbers_in_sequences(150130,1900,14)'''

#3)ничего не принимает но возвращает
'''def foo():
    return 'Pelmeni'
a = foo()
print(a)
def foo():
    return 2+2
a = foo()
print(a)

def foo():
    return 12,7,3,4,5
a = foo()
print(a)

def foo():
    return 12,7,3,4,5
a = foo()
print(list(a))

def foo():
    return условные и итерируемые конструкции
a = foo()
print(a)'''

#4)принимает и возвращает
'''
def foo(number1,number2):
    summ=0
    for i in range(10):
        summ+=number1+number2
    return summ
print(foo(int(input()),int(input())))
'''
#___________________________________________________________________
#Practise
'''
1.Напишите функцию, которая принимает два числа в качестве параметра и отображает все четные числа между ними.
2.Напишите функцию, которая отображает горизонтальную или вертикальную линию из некоторого символа.
 Функция принимает в качестве параметра: длину линии, направление, символ. 
 ( сделать так, чтобы если пользователь вводил направление с большой буквы, программа работала верно)
3. Напишите функцию, которая возвращает максимальное из четырёх чисел. 
 Числа передаются в качестве параметров.  
4. Напишите функцию, которая возвращает сумму чисел в указанном диапазоне. Границы диапазона передаются в качестве параметров.
'''
#1
'''def sequences_odd_num(number_1,number_2):
    for i in range(number_1,number_2+1):
        if i%2!=0:
            print(i)

sequences_odd_num(1,10)
'''
#2
'''
def symbol_destination(length,destination,symbol):
    if destination == 'horizontal':
        print(symbol*length)
    elif destination == 'vertical':
        for i in range(0,length+1):
            print(symbol)

length = int(input('Write length: '))
destination = input('Choose destiantion:\'horizontal\' or \'vertical\':\n ')
symbol = input('Write symnol: ')
symbol_destination(length,destination,symbol)
'''
#___________________________________________________________________


# Организация функций
'''
def main():
    say_hello()
    say_goodbye()

def say_hello():
    print("Hello")

def say_goodbye():
    print("Good Bye")

# Вызов функции main
main()
'''

#	Распаковка и упаковка аргументов.
'''
Распаковка 
Мы можем использовать * для распаковки списка, чтобы все его элементы можно было передавать как разные параметры.
def fun(a, b, c, d):
    print(a, b, c, d)
my_list = [1, 2, 3, 4]
# Unpacking list into four arguments
fun(*my_list)

Упаковка 
Когда мы не знаем, сколько аргументов нужно передать функции
def mySum(*args):
    return sum(args)
print(mySum(1, 2, 3, 4, 5))
print(mySum(10, 20))


'''

#	Аргументы по умолчанию, аргументы-ключи.
'''
def print_person(name, age = 18):
    print(f"Name: {name}  Age: {age}")
print_person("Rafael")


#Именнованные параметры
def print_person(name, age):
    print(f"Name: {name}  Age: {age}")
print_person(age = 21, name = "Rafael")

# * -  Все параметры, которые располагаются справа от символа *, получают значения только по имени:
def print_person(name, *,  age, company):
    print(f"Name: {name}  Age: {age}  Company: {company}")
print_person("Bob", age = 41, company ="Microsoft") 


'''

#	Область видимости, правило LEGB.
'''
ОБЛАСТЬ ВИДИМОСТИ
LEGB
Интерпретатор начинает поиски имени изнутри, последовательно переходя от локальной 
области видимости к объемлющей, затем к глобальной и в завершении к встроенной.

Local -> Enclosed -> Global -> Built-in

Local - inside fun-s. Удаляется, когда функция или блок кода завершают свое выполнение.

Global - free space

Enclosed - подобная область видимости относится к переменным которые созданы в функция, которые были созданы внутри других
функций lambda(частный пример)

Built-in - все встроенные по типу pi, punctuation, and etc.

'''

#	Локальные и глобальные переменные в функциях.
'''
global название переменной

n = 15
print(n)#15
def change_value():
    global n
    n+=15
    print(n)
change_value()

nonlocal 
Имена, перечисленные в инструкции nonlocal, в отличие от тех, что перечислены в инструкции global,
должны ссылаться на ранее существовавшие переменные в охватывающей области.

def football():
    x = 'Ronaldo'
    def argentina():
        nonlocal x
        x = 'Messi'

    return x
print(football())


'''

#	Функции как объекты первого класса.
'''
Это означает, что функции можно передавать и использовать в качестве аргументов, 
как и любой другой объект(string, int, float, list и т.Д.).

Особенности функций как объектов первого класса:

Функции можно присваивать переменным.
Функцию можно вернуть из функции.
У функций те же свойства и методы, что и у объектов(OOП).
Функцию можно передать в качестве аргумента при вызове другой функции.

def my_object(text):
    return text.upper()  

print(my_object("Вызов my_object"))    
upper = my_object  
print(upper("Вызов upper")) 
'''

#	Рекурсия.
''' 
#Рекурсивная функция - та функция, что вызывает саму же себя.
#Без рекурсии:
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result
#С ней:
def factorial(n):
    if n == 1:
        return 1
    else: return n * factorial(n - 1)

'''

'''
Задание 5
Напишите функцию, которая отображает пустой или
заполненный квадрат из некоторого символа. Функция
принимает в качестве параметров: длину стороны квадрата, символ и переменную логического типа:
■ если она равна True, квадрат заполненный;
■ если False, квадрат пустой.
True
******
******
******
False
******
*    *
*    *
******
'''
'''length = int(input("insert length:"))
symbol = input("isnert simvol")
choice = input("insert your choice\n"
               "True/False:")
def square(length,symbol,choice):
    if choice=='True':
        for i in range(length):
            print(symbol*length)
    elif choice=='False':
        for i in range(length):
            for j in range(length):
                if i ==0 or j ==0 or i==length-1 or j==length-1:
                    print(symbol,end='')
                else:
                    print(" ",end='')
            print()
square(length,symbol,choice)'''

'''
line = 'Cheburek'
print(type(max(line)))
list_el = [1.3,1.5, 90.1 , 10.5]
print(max(list_el))
list_el_2 = [False, True]
print(max(list_el_2))
'''

'''
x = 2
print(type(eval('x+6')))
'''

'''def foo():
    pass

def foo2():
    pass
def foo3():
    pass

def foo4():
    pass
def foo5():
    pass
def Foo():
    pass

def main():
    foo()
    foo2()
    foo4()
    foo3()
    foo5()

main()'''


'''def fun(a, b, c, d):
    print(a, b, c, d)

my_list = [111, 10.5, False, 'Hello']
# Unpacking list into four arguments
fun(*my_list)
'''
def summ_elements(*args):
    list_el = [args]
    return list_el

print(summ_elements(1, 2, 3, 4, 5,10,15))

