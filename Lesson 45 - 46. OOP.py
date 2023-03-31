# Понятие ООП.
'''
Конкретным воплощением класса является объект.

Классы-Класс предназначен для описания некоторого типа объектов
Класс может определять переменные и константы для хранения состояния
 объекта и функции для определения поведения объекта.
 Переменные которые хранятся в классе мы будем называть полями,а функции внутри классa методами

#Особенности реализации ООП в Python, «утиная типизация».

Утиная типизация – это концепция, характерная для языков программирования с
 динамической типизацией(А это значит, что переменная не привязана жестко с определенному типу)
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

get,set

self – общепринятое имя для ссылки на объект,
 в контексте которого вызывается метод.
 Этот параметр обязателен и отличает метод класса от обычной функции.

Перегрузка методов.
Если два или более метода имеют одинаковые имена,
но разное количество параметров или разные типы параметров, или и то, и другое,
то это называется перегрузкой методов.

# Function to take multiple arguments
def add(datatype, *args):
	if datatype == 'int':
		answer = 0
	if datatype == 'str':
		answer = ''
	for x in args:
		answer = answer + x

	print(answer)

# Integer
add('int', 5, 6)
# String
add('str', 'Hi ', 'Geeks')


Python является динамически типизированным языком и следовательно,
перегрузка методов здесь невозможна, тем не менее,
есть простой способ реализовать такое поведение в Python.

Magic-методы, конструкторы.
Конструктор - это функция которая вызывается, как только создается экземпляр класса
В Python имена методов, которые имеют ведущее и последующее двойное подчеркивание - называют магическими методами
Эти методы известны как dunder методы("Double Under (Underscores)")

def __len__(obj):
    return len(obj)

len(list)

https://habr.com/ru/post/186608/

'''
# example
'''import random


class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def __repr__(self):
        return f"Dice with {self.sides} sides"

    def __str__(self):
        return f"Dice with {self.sides} sides"

    def __add__(self, other):
        return Dice(self.sides + other.sides)

    def __sub__(self, other):
        return Dice(self.sides - other.sides)

    def __eq__(self, other):
        return self.sides == other.sides

    def __ne__(self, other):
        return self.sides != other.sides

    def __lt__(self, other):
        return self.roll() < other.roll()

    def __le__(self, other):
        return self.roll() <= other.roll()

    def __gt__(self, other):
        return self.roll() > other.roll()

    def __ge__(self, other):
        return self.roll() >= other.roll()

    def roll(self):
        return random.randint(1, self.sides)

# Создание объектов Dice с разным количеством граней
d6 = Dice()
d10 = Dice(10)

# Бросок костей
print(f"D6 roll: {d6.roll()}")
print(f"D10 roll: {d10.roll()}")

# Сложение костей
d16 = d6 + Dice(10)
print(f"D6 + D10 = {d16}")

# Сравнение результатов бросков
print(f"D10 > D6: {d10 > d6}")
print(f"D10 == D6: {d10 == d6}")
print(f"D6 < D10: {d6 < d10}")

'''
'''


Статические методы и методы класса.
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

Переменные и функции, объявленные внутри класса с использованием префикса _ (одно нижнее подчеркивание),
 являются защищенными (protected) и доступны только внутри класса и его наследников. 
 Однако, защищенные члены могут быть доступны извне, если к ним обратиться напрямую.

 Переменные и функции, объявленные внутри класса с использованием префикса __ (двойное нижнее подчеркивание),
  являются приватными (private) и не доступны извне класса.

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
Множественное наследование и MRO (порядок разрешения методов).

'''
# Полиморфизм.
'''

Перегрузка операторов.
Реализация магических методов.

'''