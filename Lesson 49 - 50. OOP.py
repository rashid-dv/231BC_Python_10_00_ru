# Перегрузка методов
'''

Использование декоратора singledispatchmethod:
from functools import singledispatchmethod
class MyClass:
    @singledispatchmethod
    def my_method(self, a):
        raise NotImplementedError('Метод не реализован для этого типа данных')
    @my_method.register
    def _(self, a: int):
        return a + 1
    @my_method.register
    def _(self, a: str):
        return a.upper()
obj = MyClass()
print(obj.my_method(10)) # Выводит: 11
print(obj.my_method("hello")) # Выводит: "HELLO"

'''

# Наследование.
'''
Наследование - это механизм в ООП, позволяющий создавать новый класс
на основе существующего,  уже существующий класс при этом называется базовым (или родительским)
классом, а новый класс - производным (или дочерним) классом.

При наследовании дочерний класс получает все атрибуты и методы базового класса,
а также может добавлять свои собственные атрибуты и методы,
переопределять или дополнять базовые методы.

Наследование позволяет избежать дублирования кода, если несколько классов имеют общие свойства и методы

class суперкласс :
    методы_суперкласса


class подкласс (суперкласс):
    методы_подкласса




#Множественное наследование и MRO (порядок разрешения методов).
Множественное наследование (Multiple Inheritance) - это возможность создания класса,
 наследующего свойства и методы одновременно от двух или более родительских классов.


 MRO (Method Resolution Order) - это порядок, в котором Python ищет методы в множественном наследовании. 

class A:
    def foo(self):
        print("A.foo()")

class B:
    def foo(self):
        print("B.foo()")

class C:
    def foo(self):
        print("C.foo()")

class D(B, C):
    pass
a = D()
a.foo()
'''

# Полиморфизм.
'''
Полиморфизм - это принцип объектно-ориентированного программирования, который позволяет объектам
 одного класса иметь различное поведение при вызове одного и того же метода,
в зависимости от типа объекта, с которым он работает.

1.Метод одного класса, реализация которого происходит в других классах
class Operation:
    def execute(self, x, y):
        pass

class Addition(Operation):
    def execute(self, x, y):
        return x + y

class Subtraction(Operation):
    def execute(self, x, y):
        return x - y

class Multiplication(Operation):
    def execute(self, x, y):
        return x * y

class Division(Operation):
    def execute(self, x, y):
        if y == 0:
            raise ValueError('Division by zero')
        return x / y

class Calculator:
    def __init__(self, operation):
        self.operation = operation

    def calculate(self, x, y):
        return self.operation.execute(x, y)


addition = Addition()
subtraction = Subtraction()
multiplication = Multiplication()
division = Division()

calc1 = Calculator(addition)
print(calc1.calculate(2, 3))  # 5





2. Перегрузка операторов.Реализация магических методов.
https://habr.com/ru/post/186608/



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            return NotImplemented
p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2

print(p3.x, p3.y)  # Output: 4 6


'''

'''
class Human:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def set_name(self,value):
        self.__name = value

    def get_name(self):
        return self.__name

    def set_age(self,value):
        self.__age = value

    def get_age(self):
        return self.__age

    def info(self):
        pass


class Employee(Human):
    def info(self):
        print(f'{self.get_name()} is under the age = {self.get_age()}')


class Teacher(Human):

    def __init__(self,name, age,character):
        super().__init__(name,age)
        self.character = character
        print('\n\nChild class\'s constructor')

    def info(self):
        print(f'{self.get_name()} is under the age = {self.get_age()}')

    def teach(self, class_name):
        print(f'Teacher {self.get_name()} teaches group {class_name} but he has {self.character}')


class Student(Teacher):
    def study(self):
        self.teach('3B class')

    def info(self):
        print(f'{self.get_name()} is under the age = {self.get_age()} and he is {self.character}')


employee = Employee('Murad', 20)
employee.info()
teacher = Teacher('Ivan', 55,'Unimaginable rude')
teacher.info()
print(teacher.get_name())

student = Student('Vitalik', 29, 'Unimaginable friendly')
print(student.get_name())
student.study()
student.info()'''

'''
class A:
    def foo(self):
        print("A.foo()")

class B:
    def __init__(self):
        print('Constructor B')
    def foo(self):
        print("B.foo()")

class C:
    def __init__(self):
        print('Constructor C')
    def foo(self):
        print("C.foo()")

class D(C,B):
    pass

a = D()
a.foo()'''

'''class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            return NotImplemented
p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3)
print(p3.x, p3.y)  # Output: 4 6'''

from random import randint

class Dice:
    def __init__(self,sides = 4):
        self.side = sides

    def __str__(self):
        return f'Our dice has {self.side}'

    def __len__(self):
        return self.side

    def __add__(self, other):
        return self.side + other.side

    def __sub__(self, other):
        return self.side - other.side

    def __eq__(self, other):
        return self.side == other.side

    def __ne__(self, other):
        return self.side != other.side

    def __lt__(self, other):
        return self.side < other.side

    def __gt__(self, other):
        return self.side > other.side

    def __le__(self, other):
        return self.side <= other.side

    def __ge__(self, other):
        return self.side >= other.side

    def roll(self):
        return randint(1,self.side+1)

d4 = Dice()
print(d4)
d6 = Dice(6)
print(d6)
d20 = Dice(20)
print(d20)

d10 = d4+d6
d16 = d20 - d4

print(d20.roll())
print(d10 == d16)
print(d10 > d16)
print(d10 < d16)
print(d10 <= d16)
print(d10 >= d16)
print(d10 != d16)
print(len(d4))
print(d10)
print(d16)

#Practise
'''

1. Создайте класс Human, который будет содержать информацию о человеке.
 С помощью механизма наследования, реализуйте класс Builder 
 (содержит информацию о строителе), класс Sailor (содержит информацию о моряке),
  класс Pilot (содержит информацию о летчике). 
 Каждый из классов должен содержать необходимые для работы методы



2.Создайте класс Число (или используйте уже ранее созданный вами).
 Класс число хранит внутри одно значение.
  Используя перегрузку операторов реализуйте для него арифметические 
  операции для работы с числом (операции +, -, *, /)



'''
