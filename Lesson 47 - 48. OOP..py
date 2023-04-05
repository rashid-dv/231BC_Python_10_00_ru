#Статические методы и методы класса.
'''

Статический метод - это метод класса, который связан с классом, а не с его экземплярами.
Он не требует создания экземпляра класса для вызова и может быть вызван напрямую из класса.

В отличие от обычных методов класса, статический метод не получает первым аргументом ссылку
на экземпляр класса self. Вместо этого, он может принимать параметры так же, как и обычная функция.

Статические методы обычно используются для группирования функциональности,
которая связана с классом, но не зависит от состояния его экземпляров.

 Такие методы предваряются аннотацией @staticmethod и относятся в целом к классу

 class MyClass:
    @staticmethod
    def my_static_method(x, y):
        return x + y

print(MyClass.my_static_method(1, 2)) # выведет 3


'''

# Инкапсуляция.
'''
Инкапсуляция в Python - это механизм, который позволяет скрыть реализацию данных внутри класса от внешнего мира.

Общедоступный, внутренний и приватный метод.
В Python есть три типа видимости: public, protected и private.

Переменные и функции, объявленные внутри класса и доступные извне, являются публичными (public).
class MyClass:
    def public_method(self):
        print("This is a public method")

    def __init__(self, x):
        self.public_attribute = x

my_object = MyClass(10)
my_object.public_method()    # This is a public method
print(my_object.public_attribute)    # 10

Переменные и функции, объявленные внутри класса с использованием префикса _ (одно нижнее подчеркивание),
 являются защищенными (protected) и доступны только внутри класса и его наследников. 
 Однако, защищенные члены могут быть доступны извне, если к ним обратиться напрямую.
 class MyClass:
    def __init__(self, x):
        self._protected_attribute = x

    def _protected_method(self):
        print("This is a protected method")

class MyChildClass(MyClass):
    def child_method(self):
        self._protected_method()

child_object = MyChildClass(10)
child_object.child_method()    # This is a protected method
print(child_object._protected_attribute)    # 10

 Переменные и функции, объявленные внутри класса с использованием префикса __ (двойное нижнее подчеркивание),
  являются приватными (private) и не доступны извне класса.
class MyClass:
    def __init__(self, x):
        self.__private_attribute = x

    def __private_method(self):
        print("This is a private method")

class MyChildClass(MyClass):
    def child_method(self):
        self.__private_method()

child_object = MyChildClass(10)
child_object.child_method()    # AttributeError: 'MyChildClass' object has no attribute '__private_method'
print(child_object.__private_attribute)    # AttributeError: 'MyChildClass' object has no attribute '__private_attribute'

#Get, Set

Декоратор @property используется для создания геттера,который позволяет получать значение атрибута,
Декоратор @<attr>.setter используется для создания сеттера, который позволяет устанавливать значение атрибута.

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

person = Person("Alice", 30)
print(person.name)    # Alice
person.name = "Bob"
print(person.name)    # Bob

print(person.age)    # 30
person.age = 35
print(person.age)    # 35


'''
# Exercises:
'''
Реализуйте класс BankAccount, который будет иметь закрытый атрибут balance.
 Реализуйте методы deposit и withdraw, которые будут изменять баланс счета, 
 но не давайте возможность напрямую изменять его значение извне класса.

Создайте класс Employee, который будет иметь закрытый атрибут salary.
 Реализуйте метод get_salary, который будет возвращать значение атрибута salary.
  Но не давайте возможность изменять его значение извне класса.

Реализуйте класс Student, который будет иметь закрытый атрибут grades.
 Реализуйте методы add_grade и get_grades, которые будут изменять и 
 возвращать значения атрибута grades соответственно, но не давайте возможность 
 напрямую изменять его значение извне класса.

Реализуйте класс Car, который будет иметь закрытые атрибуты brand, model и year. 
Реализуйте метод get_car_info, который будет возвращать информацию о машине в виде 
строки, но не давайте возможность изменять значения атрибутов извне класса.

Создайте класс Game, который будет иметь закрытый атрибут score. 
Реализуйте методы update_score и get_score, которые будут изменять и возвращать
значение атрибута score соответственно, но не давайте возможность напрямую изменять 
его значение извне класса.
'''

# Наследование.
'''
Наследование - это механизм в ООП, позволяющий создавать новый класс на основе существующего, 
уже существующий класс при этом называется базовым (или родительским)
классом, а новый класс - производным (или дочерним) классом.

При наследовании дочерний класс получает все атрибуты и методы базового класса,
а также может добавлять свои собственные атрибуты и методы,
переопределять или дополнять базовые методы.

Наследование позволяет избежать дублирования кода, если несколько классов имеют общие свойства и методы


class подкласс (суперкласс):
    методы_подкласса

class Person:
    pass


class Employee(Person):
    pass

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

Перегрузка операторов.
Реализация магических методов.

'''


class Person:
    def __init__(self,name):
        self.name = name

    def print_info(self):
        print(f'your persons name is : {self.name}')
    @staticmethod
    def salary(x,raise_salary):
        if raise_salary==True:
            x+=100000
            return x
        else:
            x-=100000
            return x

Human = Person('Gosha')
print(Human.print_info())
print(Human.salary(5000,True))
print(Person.salary(105000,False))