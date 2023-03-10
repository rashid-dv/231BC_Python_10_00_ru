#Функциональное программирование.
#Что такое функциональное программирование?
'''Функциональное программирование представляет собой методику написания программного
обеспечения, в центре внимания которой находятся функции.
Функции могут присваиваться переменным, они могут передаваться в другие функции и порождать новые функции.'''


'''
1. Bсе, что можно делать с «данными», можно делать и с функциями 
2.Использование рекурсии в качестве основной структуры контроля потока управления.
3. «Чистые функции» функциональные языки избегают побочных эффектов. Это исключает присваивания
4.ФП не одобряет или совершенно запрещает инструкции, используя вместо этого вычисление выражений (т.е. функций с аргументами).
5. ФП акцентируется на том, что должно быть вычислено, а не как.

Чистая Функция — Функция которая является детерминированной и не обладает никакими побочными эффектами.
# детерминирована
def sum(a,b): детерминирована
  return a+b

# не  детерминирована
count = 0
a,b = int(input()),int(input())
if a>b:
    count+=1
else:
    count=0
def sum(a,b):
    global count
    if count==1:
        return a+b
    else:
        return a-b
print(sum(a,b))
'''

#Анонимные функции lambda.
'''
1. (lambda перечисляются аргументы через запятую : что то с ними делается)(передаем аргументы)
2. lambda параметры: выражение
'''

#Функции высших порядков.
'''
 Эти функции используют в качестве (некоторых) своих параметров другие функции - вот почему мы называем их функциями высшего порядка.
'''

#Функции map(), reduce(), filter(), zip().

#map() - позволяет обрабатывать одну или несколько последовательностей с использованием заданной функции.
#reduce()- когда требуется обработать список значений таким образом, чтобы свести процесс к единственному результату,
#filter()- определяет нужно ли исключить конкретный элемент из последовательности или нет(если да  то фильтрует последовательность, если нет ничего не делает)
#zip()- oбъединяет отдельные элементы из каждой последовательности в итерируемую последовательность

#Замыкание -  (closure) представляет функцию, которая запоминает свое лексическое окружение даже в том случае, когда она выполняется вне своей области видимости.
'''
def info(value):
    name = value
    def print_info():
        print()
'''

#bez lambda
'''def summ(a,b):
    if a>0 and b>0:
        return a+b
    else:
        return a-b
print(summ(12,9))
'''

'''#s lambdoy
a = (lambda a,b: a+b if a>0 and b>0 else a-b)(12,10)
print(a)
'''

'''
list_el = [1,2,3,4,5,6,7]
print(list(map(lambda element:element*2, list_el)))
'''


'''
def my_map(function,list_el):
    new_list=[]
    for iterable in list_el:#1
        new_list.append(function(iterable))#1
    return new_list


list_el = [1,2,3,4,5,6,7,8,9,10]
print(my_map(lambda element: element*2,list_el))'''
'''
   filter(function or None, iterable) --> filter object
    
    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    
    фильтр (функция или нет, итерируемый) --> объект фильтра
    
     Возвращает итератор, выдающий те элементы итерации, для которых функция (элемент)
     правда. Если функция имеет значение None, верните элементы, которые верны.
'''
'''list_el = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda element: element%2==0,list_el)))
'''
'''from functools import reduce
print(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
'''

'''#print(list(zip('abcdefg', range(3),[99,22,44])))
list_el = [1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda element: element*2,list_el)))
'''
#Practise:
'''
написать свои функции:
zip
filter
reduce
'''
'''
def info(value):
    name = value
    def print_info():
        print(f'your name{name}')
    print_info()
info('Rafael')'''

def my_reduce(function,list_el,initial=1):#summ=0
    for iterable in list_el:
        initial= function(initial,iterable)
    return initial

list_el = [1,2,3,4,5,6,7,8,9,10]
print(my_reduce(lambda x,y: x*y,list_el))