#List methods
'''
#https://pythontutor.com/visualize.html#mode=display

append(item): добавляет элемент item в конец списка

insert(index, item): добавляет элемент item в список по индексу index

extend(items): добавляет набор элементов items в конец списка

remove(item): удаляет элемент item. Удаляется только первое вхождение элемента. Если элемент не найден, генерирует исключение ValueError

clear(): удаление всех элементов из списка

index(item): возвращает индекс элемента item. Если элемент не найден, генерирует исключение ValueError

pop(index): удаляет и возвращает элемент по индексу index. Если индекс не передан, то просто удаляет последний элемент.

count(item): возвращает количество вхождений элемента item в список

sort(reverse = False,key): сортирует элементы.
Optional. reverse=True отсортирует в обратном порядке. По умолчанию reverse=False(по возростаниө)
Optional. key - функцию сортировки.

people = ["Tom", "Bob", "Alice", "Sam", "Bill"]
people.sort()
people = ["Tom", "Alina", "bob", "alice", "Sam", "Bill" ]
people.sort(key=str.lower)

reverse(): расставляет все элементы в списке в обратном порядке

del list[0]
del list[0:]
del list[:3]
min(list)
max(list)

copy(): копирует список
'''
#Practise:
'''
1.Есть список целых чисел, заполненный случайными числами.
На основании данных этого массива нужно:
1.1. Создать список целых чисел , содержащий только четные
числа из первого списка;
1.2 Создать список целых чисел, содержащий только нечетные
числа из первого списка;
1.3 Создать список целых, содержащий только отрицательные числа из первого списка;
1.4 Создать список целых, содержащий только положительные числа из первого списка.

2 В списке целых, заполненном случайными числами,
определить минимальный и максимальный элементы,
посчитать количество отрицательных элементов, посчитать количество положительных элементов, посчитать
количество нулей. Результаты вывести на экран.

#3
Напишите программу на Python для удаления дубликатов из списка.
#4
Напишите программу на Python, чтобы проверить, пустой список или нет
#5
Напишите программу на Python, чтобы найти список слов, длина которых превышает n, из заданного списка слов
#6
Напишите функцию Python, которая принимает два списка и возвращает True, если у них есть хотя бы один общий член.
#7
Напишите программу на Python для печати указанного списка после удаления 0-го, 4-го и 5-го элементов
#8
Напишите программу на Python, чтобы найти индекс элемента в указанном списке.

'''

#list_items= [1,2,3,4,'Hello']
#items = list_items
'''for i in range(0,11):
    list_items.append(i)
    print(list_items)

'''

#list_items.insert(3,['hello',1,2])
#new_list = [15,7,'apple', False]
#list_items.extend(new_list)

#print(list_items.index('Hello'))

#list_items.remove(3)

#list_items.clear()


'''a = list_items.pop(3)
print(f'Deleted element {a}')'''


'''
#1 sposob
list_spisok = [1,2,5,5,10,15,20,220,150,65,5]
value = int(input())
new_list = [i*2 for i in list_spisok if i!=value]# ne ravno 5
new_list.append(value)
new_list.sort()
print(new_list)
new_list = []
#2 sposob
for i in list_spisok:
    if i!=value:
        new_list.append(i)

new_list.append(value)
new_list.sort()
print(new_list)
'''
'''
list_spisok = [1,2,5,5,10,15,20,220,150,65,5]
print(f'Bez sorta {list_spisok}')
list_spisok.sort(reverse = True)
print(f'S sortirovkoy {list_spisok}')'''

'''
list_spisok = ['Zein', 'Keya', 'bryan','June','Bob','Ben' ,'Alex']
print(f'Bez sorta {list_spisok}')
list_spisok.sort(key = str.lower)
print(f'S sortirovkoy {list_spisok}')
'''

#list_spisok = [1,2,5,5,10,15,20,220,150,65,5]
'''print(max(list_spisok))
print(min(list_spisok))'''

'''list_new = list_spisok.copy()
print(list_new)'''

from random import randint

list_items = []
start,end = int(input('Vvedite nachalo diapazona')),int(input('Vvedite konec diapazona'))
#1 sposob zapolneniya
for i in range(start,end):
    list_items.append(randint(-100,100))
print(f'Nash 1-y spisok = {list_items}')

#2 sposob zapolneniya
list_items = [randint(-100,100) for i in range(start,end)]


second_list = [item for item in list_items if item%2==0]
#second_list = [item if item>0 else item*2 for item in list_items if item%2==0]
print(second_list)

