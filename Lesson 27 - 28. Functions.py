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
'''def summ_elements(*args):
    list_el = [args]
    return list_el

print(summ_elements(1, 2, 3, 4, 5,10,15))

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