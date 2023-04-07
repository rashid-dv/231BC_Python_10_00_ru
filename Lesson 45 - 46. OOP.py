# Понятие ООП.
'''
Конкретным воплощением класса является объект.

Классы-Класс предназначен для описания некоторого типа объектов
Класс может определять переменные и константы для хранения состояния
 объекта и функции для определения поведения объекта.
 Переменные которые хранятся в классе мы будем называть полями,а функции внутри классa методами

Syntaxix:
class name_of_the_class:
    #methods
    #attributes

object = name_of_the_class()


#Особенности реализации ООП в Python, «утиная типизация».

Утиная типизация – это концепция, характерная для языков программирования с
 динамической типизацией(А это значит, что переменная не привязана жестко k определенному типу)
 согласно которой конкретный тип или класс объекта не важен, а важны лишь свойства и методы,
 которыми этот объект обладает

class Meter:
    def __len__(self):
        return 1000
print(len([1, 2, 3]))
print(len("Duck typing..."))
print(len(Meter()))

Экземпляр класса.
Экземпляр класса - переменная представитель класса, которая присваивает ее класс и работающая от его имени.
(Если класс является планом, то экземпляр – это объект, который построен по этому плану.)

Классы и объекты.
Syntaxix:
class название_класса:
    атрибуты_класса
    методы_класса


Атрибуты или поля (свойства), методы класса.
Атрибут/Поле/Свойство - Это переменная, существующая внутри объекта этого класса
и содержащая в себе значение, отражающее некоторое свойство этого объекта.

методы (функции-члены) класса – это функции, описывающие, что умеют делать объекты класса.


self – общепринятое имя для ссылки на объект,
 в контексте которого вызывается метод.
 Этот параметр обязателен и отличает метод класса от обычной функции.

Конструктор - это специальный метод классов, который выступает в качестве
метода который вызывается автоматически, как только создается объект класса.
Обычно используется для инциализации разного рода полей.
def __init__(self):

Деструктор - это специальный метод классов, который выступает в качестве
метода который вызывается автоматически, как только завершается работа класса.
Обычно используется для удалению данных(освобождении памяти)
def __del__(self):

Перегрузка методов.
Если два или более метода имеют одинаковые имена,
но разное количество параметров или разные типы параметров, или и то, и другое,
то это называется перегрузкой методов.

Python является динамически типизированным языком и следовательно,
перегрузка методов здесь невозможна, тем не менее,
есть простой способ реализовать такое поведение в Python.
1. Использование аргументов со значениями по умолчанию: 
class MyClass:
    def my_method(self, a, b=None):
        if b:
            print(a, b)
        else:
            print(a)

obj = MyClass()
obj.my_method(1) 
obj.my_method(1, 2)
2.Использование декоратора singledispatch:

from functools import singledispatch

class MyClass:
    @singledispatch
    def my_method(self, a):
        raise NotImplementedError('Метод не реализован для этого типа данных')

    @my_method.register(int)
    def _(self, a: int):
        return a + 1

    @my_method.register(str)
    def _(self, a: str):
        return a.upper()

obj = MyClass()
print(obj.my_method(10)) # Выводит: 11
print(obj.my_method("hello")) # Выводит: "HELLO"

По умолчанию, если переданный объект не является зарегистрированным типом, 
будет выброшено исключение NotImplementedError.
Однако, можно зарегистрировать функцию-обработчик по умолчанию,
используя декоратор @<имя_функции>.register(object)
'''


'''
Magic-методы
В Python имена методов, которые имеют ведущее и последующее двойное подчеркивание - называют магическими методами
Эти методы известны как dunder методы("Double Under (Underscores)")

def __len__(obj):
    return len(obj)

len(list)

https://habr.com/ru/post/186608/

'''



'''
class Student:

    def __init__(self,name,age,hobby):
        self.name = name
        self.age = age
        self.progress = 0
        self.hobby = hobby



    def study(self,subject,study):

        if study:
            self.progress += 1
            print(f'You study {subject} and your progress = {self.progress} out of 10')
        else:
            self.progress-=1
            print(f'Your study progress decreased by 1. Overall progress = {self.progress} out of 10')

hobby = input()
student = Student("Rashad", 24, hobby )
'''


