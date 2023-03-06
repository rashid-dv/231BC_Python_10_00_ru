# Array and List. Stack and Heap
'''
Массив - структура объектов фиксированного размера
Коллекция - структура объектов с динамически изменяющейся размерностью
массивы следует применять там, где будет строго фиксированное количество элементов;
 если предполагается изменение количества элементов, следует применять коллекции.

 две области в оперативной памяти — стек (stack) и кучу (heap).

Stack:
Стек используется для статичного выделения памяти.
Heap:
Куча используется для динамического выделения памяти

Если программа потребляет память не высвобождая её, то, в конечном итоге, она поглотит
все доступные резервы и попытается выйти за пределы памяти.
 Тогда она просто упадет сама, или, что ещё драматичнее, обрушит операционную систему.

Сборка мусора — это процесс автоматического управления памятью в куче,
который заключается в поиске неиспользующихся участков памяти, которые ранее были заняты
под нужды программы.



'''

# List , Ссылочный тип данных list.
'''
Список (list) представляет тип данных, который хранит набор или последовательность элементов.
numbers1 = [1, 2, 3, 4, 5]
numbers2 = list([1, 2, 3, 4, 5])
string = ['Hello']
print(string)
letters = list("Hello")
print(letters) 
'''
# Обращение к элементам списка

# Разложение списка
'''
people = ["Tom", "Bob", "Sam"]
tom, bob, sam = people
'''

# Перебор элементов (for,while)

# Сравнение списков
'''
numbers1 = [1, 2, 3, 4, 5]
numbers2 = list([1, 2, 3, 4, 5])
if numbers1 == numbers2:
    print("numbers1 equal to numbers2")
else:
    print("numbers1 is not equal to numbers2")
'''

# Получение части списка
'''
list[:end]
list[start:end]
list[start:end:step]
'''

# List Comprehension - генератор списков


'''
blokntik = ['kapusta', 'burak', ' kartoshka', 'morkovka', 100, 3.0, True]
print(blokntik)

spisok_korizna = ['Burak', 'Kortoshka', 11, 14]

list_elements = list('Hello')
print(spisok_korizna[3])
print(list_elements)
'''

'''
people = [1, "Chelovek", "Yeda"]
tom, bob, sam = people
print(tom, bob, sam)
'''
'''
list_elements = [20,30, 'batat', 'noj', 'yabloko',False]

for i in range(0,len(list_elements)+1):
    print(list_elements[i], end = ' ')
    
i=0
while i<len(list_elements):
    print(list_elements[i])
    i+=1
'''

'''numbers1 = [1, 2, 3, 4, 5]
numbers2 = list([1, 2, 3, 4])
if numbers1 == numbers2:
    print("numbers1 equal to numbers2")
else:
    print("numbers1 is not equal to numbers2")
    '''
'''
numbers1 = [0, 2, 3, 4, 5]
numbers2 = list([1, 3, 2, 5, 4])
if numbers1[0] > numbers2[1]:
    print("numbers1 greater than numbers2")
elif numbers2[3]>numbers1[2]:
    print("numbers2 greater than numbers1")
else:
    print('idk')'''

'''
numbers1 = [0, 2, 3, 4, 5]*2
print(numbers1)

print(numbers1[:5])
print(numbers1[2:4])
print(numbers1[0:7:2])
'''
#______________________________________
#Practise
'''
В списке целых chisel, заполненном случайными числами 
вычислить:
■ Сумму polojitelnix чисел;
■ Сумму отрицательных чисел;
■ Сумму четных чисел;
■ Сумму нечетных чисел;
■ Произведение элементов с индексами кратными 3;
■ Произведение элементов между минимальным и 
максимальным элементом;
■ Сумму элементов, находящихся между первым и последним положительными элементами
'''
'''
from random import *
list_elements = [randint(-100,100),randint(-100,100), randint(-100,100),randint(-100,100),randint(-100,100)]
summ=0
for i in range(0,len(list_elements)):   #0 - 2
    if list_elements[i]>0:
        summ+=list_elements[i]
        print(f'{summ} - summa poloj')


summ=0
for i in range(0,len(list_elements)):   #0 - 2
    if list_elements[i]<0:
        summ+=list_elements[i]
        print(f'{summ} - summa otric')


summ=0
for i in range(0,len(list_elements)):   #0 - 2
    if list_elements[i]%2==0:
        summ+=list_elements[i]
        print(f'{summ} - summa chetnix')

summ=0
for i in range(0,len(list_elements)):   #0 - 2
    if list_elements[i]%2!=0:
        summ+=list_elements[i]
        print(f'{summ} - summa ne chetnix')
'''
#______________________________________

'''fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x*2 for x in fruits if "a" in x]
print(newlist)
'''


'''elements = [10, 21, 33, 44, 55]
new_elements = []
for i in elements:
    if i%2==0:
        new_elements.append(i*2)

        print(f'Without list comprehension {new_elements}')
        
        '''

from random import *
list_elements = [randint(-100,100),randint(-100,100), randint(-100,100),randint(-100,100),randint(-100,100)]
summ=0
for i in range(0,len(list_elements)):   #0 - 2
    if list_elements[i]>0:
        summ+=list_elements[i]
        print(f'{summ} - summa poloj')

#_______________
'''elements = [10, 21, 33, 44, 55]
newlist = [i*2 for i in elements if i%2==0]
print(f'With comprehension {newlist}')'''

#ewlist = [expression for item in iterable( if condition)]
from random import *
list_elements = [randint(-100,100),randint(-100,100), randint(-100,100),randint(-100,100),randint(-100,100)]
new_list = [i for i in list_elements if i>0]