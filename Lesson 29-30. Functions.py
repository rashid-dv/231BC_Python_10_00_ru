
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
# position arg-s
'''
def print_person(name, age):
    print(f"Name: {name}  Age: {age}")
print_person("Rafael", 21)
'''
#default arg-s
'''
def print_person(name, age = 19):

    print(f"Name: {name}  Age: {age}")

print_person("Rafael")
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

def my_object():
    return text.textupper()  

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

#Practise
'''
1. Реализовать рекурсивную функцию возведения элементов в степень. Функция принимает два параметра х и у.
Функция должна вернуть реузльтат в виде возведения числа х в степень у
2.Реализовать рекурсивную функцию для нахождения последовательности Фибоначчи. Функция принимает один параметр, она должна вернуть результат конечной суммы.
Последовательность Фиббоначи -элементы числовой последовательности 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,… 
в которой первые два числа равны 0 и 1, а каждое последующее число равно сумме двух предыдущих чисел.
Подсказка:
Если число равно 0, то возвращаем 0
Если число равно 1, то возвращаем 1
В ином случае возвращаем рекурсию в виде сумме двух предыдущих чисел.


3.Напишите функцию, которая отображает пустой или
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

'''
def power(x,y):
    if y == 0:
        return 1
    elif y ==1:
        return x
    else:
        return x*power(x,y-1-)#5*power(5,4)=3125->5*power(5,3)= 625->5*power(5,2)=125->5*power(5,1) = 25
print(power(5,5))'''

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



#packing
'''def mySum(*args,summ=0):

    for i in args:
        summ+=i
        print(summ)
    return summ

print(mySum(1, 2, 3, 4, 5.5,12.9,123,1,23,123,1,424,142))
'''
#unpacking
'''
def fun(a, b, c, d):
    print(a, b, c, d)
my_list = [1, 2, 3, 4]
# Unpacking list into four arguments
fun(*my_list)
'''

'''def summ(*args):
    slojeniye=0
    for i in args:
        slojeniye += i
        print(slojeniye)
    return slojeniye


print(summ(1,5,8,11,212))'''


'''n = 120
print(n)#120
def change_value():
    global n
    n+=15
    print(n)#135
change_value()

print(n)#'''

'''def football():
    x = 'Ronaldo'
    print(x)
    def argentina():
        nonlocal x
        x = 'Messi'
        print(x)
    argentina()
    return x

print(football())'''

'''
def my_object(text):
    return text

print(my_object("Вызов my_object"))
upper = my_object
print(upper("Вызов upper"))

text = input()
print(my_object(text.lower()))'''


#7!= 7*6*5*4*3*2*1 -
#Factorial - это представление числа как результат умножения
# чисел начиная с 1 заканчивая самим этим числом включительно
'''def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(7))'''
'''
def factorial_recursion(n): #5
    if n==0 or n==1 or n == 2:
        return n
    else:
        return n*factorial_recursion(n-1)

print(factorial_recursion(7))'''
'''

def factorial_recursion(5):
    if n==0 or n==1 or n == 2:
        return 5
    else:
        return 5*factorial_recursion(5-1) # 5 *4 =20
                            |
                            ->   
                                def factorial_recursion(4):
                                    if n==0 or n==1 or n == 2:
                                        return 4
                                    else:
                                        return 4*factorial_recursion(4-1)# 4*3 = 12
                                                        |
                                                        ->
                                                            def factorial_recursion(3):
                                                                if n==0 or n==1 or n == 2:
                                                                    return 3
                                                                else:
                                                                    return 3*factorial_recursion(3-1)#3*2 = 6
                                                                                    |
                                                                                    ->
                                                                                    def factorial_recursion(2):
                                                                                        if n==0 or n==1 or n == 2:
                                                                                            return 2 # 2
                                                                                        else:
                                                                                            return 2*factorial_recursion(2-1)

        
        

        

'''
