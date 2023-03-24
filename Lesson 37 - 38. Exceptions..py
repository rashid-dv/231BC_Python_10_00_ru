# Исключения (Exception)
'''
Исключения - это ошибки, обнаруженные при исполнении программы.(или реакция программы на исключительные ситуации в ходе ее выполнения.)
2 типа ошибок:
1. Синтаксические - ошибки указывающие на нарушения синтаксиса языка
2. Ошибки выполнения - ошибки появляющиеся уже в запущенной программе в процессе ее выполнения
другими словами подобные ошибки - исключения.
string1='Rafael'
string2='21'
print(int(string1))
print(int(string2))

'''

# Типы исключений
'''
2 типа исключений
1. Явные - через команду raise
2. Скрытые - те что спрятаны в функциях,классах, методах(те что трудно заметить)
'''

# Конструкция try except finally.
'''
Чтобы избежать резкого прерывания программы 
и обрабатывать исключения есть конструкция try..except.

try: - сюда помещается основной код, в котором потенциально может возникнуть исключение
    инструкции
except [Тип_исключения]: - Если в коде генерируется исключение, то работа кода в блоке try прерывается, и выполнение переходит сюда. Тип исключения не обязательно указывать
    инструкции
else:
    если не было исключений
ПРИМЕР:
try:
    number = int(input())
    print(f"Entered number:{number}")
except:
    print("What you entered is not a number")

Блок finally
Данный блок работает как последнее слово исключения,само же исключение может и не сработать, данный блок в любом случае отработает,если он будет присутствовать 
В основном используется для освобождения данных или закрытия файлов
try:
    number = int(input())
    print(f"Entered number:{number}")
except:
    print("What you entered is not a number")
finally:
    print("Блок try завершил выполнение")
'''

# Базовые типы исключений.
'''
all exceptions in documentation https://docs.python.org/3/library/exceptions.html
•	BaseException - базовый тип для всех встроенных исключений
•	Exception - базовый тип, который обычно применяется для создания своих типов исключений
•	ArithmeticError -  базовый тип для исключений, связанных с арифметическими операциями (OverflowError, ZeroDivisionError, FloatingPointError).
•	BufferError - тип исключения, которое возникает при невозможности выполнить операцию с буффером
•	LookupError -  базовый тип для исключений, которое возникают при обращении в коллекциях по некорректному ключу или индексу (например, IndexError, KeyError)
выше были перечислены одни из основных классов от которых наследуются исключения
•	IndexError - исключение возникает, если индекс при обращении к элементу коллекции находится вне допустимого диапазона
•	KeyError - возникает, если в словаре отсутствует ключ, по которому происходит обращение к элементу словаря.
•	OverflowError - возникает, если результат арифметической операции не может быть представлен текущим числовым типом (обычно типом float).
•   RecursionError: возникает, если превышена допустимая глубина рекурсии.
•   ValueError - возникает, если операция или функция получают объект корректного типа с некорректным значением.
•   TypeError: возникает, если операция или функция применяется к значению недопустимого типа.

и т.д.


try:
    number1 = int(input("Введите первое число: "))
    number2 = int(input("Введите второе число: "))
    print("Результат деления:", number1/number2)
except ValueError:
    print("Преобразование прошло неудачно")
except ZeroDivisionError:
    print("Попытка деления числа на ноль")
except BaseException:
    print("Общее исключение под которое попадают все исключительные ситуации,которое не представляет тип ValueError или ZeroDivisionError")

'''
# Получение информации об исключении через оператор as
'''
С помощью оператора as передается вся информация об исключении в переменную, которую затем используется в блоке except

try:
    number = int(input("Введите число: "))
    print("Введенное число:", number)
except ValueError as e:
    print("Сведения об исключении", e)
print("Завершение программы")

'''

# Генерация исключений.
'''
Оператор raise нужен,чтобы вручную сгенерировать то или иное исключение

try:
    number1 = int(input())
    number2 = int(input())
    if number2 == 0:
        raise Exception("NEVER DEVIDE BY 0")
    print("result:", number1/number2)
except ValueError:
    print("Check data again")
except Exception as e:
    print(e)

'''


'''try:
    number_1 = int(input('Enter the first number'))
    number_2 = int(input('Enter the second number'))
    result = number_1/number_2
    print(f'{number_1}/{number_2} = {result}')
except:
    print('DONT DEVIDE BY ZERO IT IS MATH!!!!!!!')
else:
    print('Something else')

finally:
    print('Final word')'''

'''
try:
    element=int(input('Write digit number:'))
    print(element)
except :
    print('You cant write string element')

finally:
    del element
    
'''

# Примеры использования.
'''
1. Написать функцию которая обработает исключение при делении двух чисел.
2. Обработайте исключение при работе с математическими операциями(например корни отрицательных чисел)
3. Обработайте исключенийе при работе со списками( выход за пределы индексации списка)
4. Обработайте исключение при работе с типами данных(например ввод не тех типов данных или работа с несовместимыми типами)
5. Обработайте исключение при работе со строками(допустим выход за пределы индексации или не корректный ввод)
6. Обработайте исключение при работе с конвертацией типов данных.
'''
'''
def devision():

    try:
        num_1 = int(input('Enter the first number: '))
        num_2 = int(input('Enter the second number: '))
        print(f'{num_1}/{num_2} = {num_1/num_2}')
    except ZeroDivisionError:
        print('You cant divide by zero')
    except ValueError:
        print('You cant use string to divide numbers')
    finally:
        print('Function outworked! You did it!')

devision()
'''
'''from math import sqrt
def sqrt_(num):
    try:
        result = sqrt(num)
        print(f'Koren ot chisla {num} = {result}')
    except ValueError:
        print('Nelza brat koren u otricatelnoqo chisla')

num = int(input())
sqrt_(num)
'''
'''
def foo(x,y):
    try:
        print(x+y)
    except TypeError:
        print('Cant summ int and str')

x=10
y='s'
foo(x,y)'''

'''
try:
    number1 = int(input("Введите первое число: "))
    number2 = int(input("Введите второе число: "))
    print("Результат деления:", number1/number2)
except ValueError:
    print("Преобразование прошло неудачно")
except ZeroDivisionError:
    print("Попытка деления числа на ноль")
except BaseException:
    print("Общее исключение под которое попадают все исключительные ситуации,которое не представляет тип ValueError или ZeroDivisionError")'''

'''try:
    number = int(input("Введите число: "))
    print("Введенное число:", number)
except ValueError as e:
    print("Value Error",e)
except TypeError as e:
    print("Value Error",e)

'''

'''try:
    number1 = int(input())
    number2 = int(input())
    if number2 == 0:
        raise Exception("NEVER DEVIDE BY 0")
    print("result:", number1/number2)
except ValueError:
    print("Check data again")
except Exception as e:
    print(e)
    '''
'''
def devide_element():
    try:
        x = int(input())
        y = int(input())
        if type(x)!=int or type(y)!=int:
            raise ValueError('Wrong type of the element')
        print(f'{x}/{y} ={x/y}')
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)
    else:
        print('Nothing worked')
    finally:
        print('______________________')

devide_element()'''


# Practise:
'''
1. Создайте функцию, которая принимает список и выводит
на экран все элементы списка, пока не встретит элемент
с нулевым значением. Если в списке нет элемента со значением 0,
функция должна выводить сообщение об ошибке.

2. Напишите программу, которая запрашивает у пользователя свой возраст. 
Если пользователь ввел отрицательное число или ноль, программа должна 
выдавать ошибку и повторно запрашивать возраст.

3. Напишите программу, которая принимает на вход список чисел и выводит на экран их сумму.
 Если в списке есть некорректные данные, например, не числа, программа должна выдавать ошибку.

4. Напишите программу, которая запрашивает у пользователя строку и пытается преобразовать
 ее в число. Если это невозможно, выведите сообщение об ошибке.

5. Напишите программу, которая запрашивает у пользователя число и выводит его квадратный корень.
 Если квадратный корень отрицательный , программа должна выдать ошибку.
'''