# Tuple(кортеж)
'''
Кортеж (tuple) представляет последовательность элементов,
 которая во многом похожа на список за тем исключением,
 что кортеж является неизменяемым (immutable) типом.
Мы не можем добавлять или удалять элементы в кортеже, изменять его.


Кортеж очень часто используется для защиты хранимых данных приложения от незапланированных или непреднамеренных изменений.
Кортеж также требует выделения значительно меньшего количества памяти.


info = 'Raf',21
print(type(info))

info = ('Raf',21)
print(type(info))
'''

# Set(множество)
'''
Set(множество) представляют очередной вид набора элементов, который хранит только уникальные элементы.
names = {"Raf", "Ne Raf", "Raf", "Rafael"}
print(names)
print(type(names))

add() -	Добавляет элемент в набор
clear() -	Удаляет все элементы из набора
copy() -	Возвращает копию набора
difference() -	Возвращает набор, содержащий разницу между двумя или более наборами
difference_update() -	Удаляет элементы в этом наборе, которые также входят в другой указанный набор
intersection() -	Возвращает набор, являющийся пересечением двух других наборов
intersection_update() -	Удаляет элементы в этом наборе, которых нет в других указанных наборах.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)
print(z)
z = x.difference_update(y)
print(z)
z = x.intersection(y)
print(z)
x.intersection_update(y)
print(x)

discard() -	Удалить указанный элемент
remove() -	Удалить указанный элемент
pop() - Удаляет и возвращает произвольный элемент набора.
isdisjoint() -	Возвращает, имеют ли два набора пересечение или нет
issubset() -	Возвращает, содержит ли другой набор этот набор или нет
issuperset() -	Возвращает, содержит ли этот набор другой набор или нет

union() -	Вернуть объединение наборов как новый набор.
update() -	Обновить набор с объединением себя и других
'''

# Frozen set
'''
Frozen set является видом множеств, которое не может быть изменено.
В такое множество мы не можем добавить новые элементы, как и удалить из него уже имеющиеся.
names = frozenset({"Rafael", "Tengiz", "Orhan"})
'''

# Dictionary(словарь)
'''
Словарь (dictionary) тип данных который хранит коллекцию элементов,
 где каждый элемент имеет уникальный ключ и некоторое значение,которое хранится за ключом.

#Синтаксис:
dictionary = { ключ1:значение1, ключ2:значение2, ....}
Ключом может быть int,str,float (не может быть дубликатов ключей)
Значением могут быть -  int,str,float,bool and other collections (могут быть дубликаты значений)

#Комлпексные словари
users = {
    "Tom": {
        "phone": "+971478745",
        "email": "tom12@gmail.com"
    }
}

#Преобразований списков/кортежей в словари и добавление элементов вручную:
users_tuple = (
    ("+994", "AZE"),
    ("+5", "USA"),
    ("+49", "Germany"),
)
users_dict = dict(users_tuple)
print(users_dict)
print(users_dict['+5'])
users_dict['+380']='Ukraine'
print(users_dict)


#Loops in Dictionaries

#Dictionary methods
clear()	Удаляет все элементы из словаря
copy()	Возвращает копию словаря
fromkeys() Возвращает словарь с указанными ключами и значением
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

get()	Возвращает значение указанного ключа
items()	Возвращает список, содержащий кортеж для каждой пары ключ-значение.
for key,value in dict.items():
    print(x,y)

keys()	Возвращает список, содержащий ключи словаря
values()	Возвращает список всех значений в словаре
pop()	Удаляет элемент с указанным ключом
popitem()	Удаляет последний элемент
setdefault()	Возвращает значение указанного ключа. Если ключ не существует: вставьте ключ с указанным значением
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("model", "Bronco")
print(x)

update()	Обновляет словарь указанными парами ключ-значение.
car.update({"color": "White"})

'''



# Practise
'''
Задание 1.
Пользователь вводит с клавиатуры название фрукта.
Необходимо вывести на экран количество раз, сколько
фрукт встречается в кортеже в качестве элемента.

Задание 2.
Добавьте к заданию 1 подсчет количества раз, когда
название фрукта является частью элемента. Например:
banana, apple, bananamango, mango, strawberry-banana.
В примере выше banana встречается три раза.

Задание 3.
Есть кортеж с названиями производителей автомобилей (название производителя может встречаться от 0
до N раз). Пользователь вводит с клавиатуры название
производителя и слово для замены. Необходимо заменить
в кортеже все элементы с этим названием на слово для
замены. Совпадение по названию должно быть полным.

Задание 4.
Есть множество, содержащее название стран. Необходимо предоставить пользователю возможности:
■ Добавление стран;
■ Удаления стран;
■ Поиска стран по введенным символам;
■ Проверки существует ли страна внутри множества

Задание 5.
Существует два множества, содержащие названия
городов. Необходимо создать третье множество: 
■  содержащее названия, которые есть в обоих множествах.
■  содержащее названия, которые есть в первом множестве, но
нет во втором.
■ содержащее названия, которые есть во втором множестве, но
нет в первом.
■ содержащее уникальные названия для каждого множества

Задание 6.
Создайте программу, хранящую информацию о великих баскетболистах. Нужно хранить ФИО баскетболиста и
его рост. Требуется реализовать возможность добавления,
удаления, поиска, замены данных. Используйте словарь
для хранения информации.

Задание 7.
Создайте программу «Фирма». Нужно хранить информацию о человеке: ФИО, телефон, рабочий email,
название должности, номер кабинета, skype. Требуется
реализовать возможность добавления, удаления, поиска, замены данных. Используйте словарь для хранения
информации.

Задание 8.
Создайте программу «Книжная коллекция». Нужно
хранить информацию о книгах: автор, название книги,
жанр, год выпуска, количество страниц, издательство.
Требуется реализовать возможность добавления, удаления, поиска, замены данных. Используйте словарь для
хранения информации.
'''

#Tuple
'''
info= 1,2,3,4,6,True,'helo',('world',23)
print(info)

tuple_el = (1,2,3,4,5)
print(tuple_el)
print(type(tuple_el))

for i in tuple_el:
    print(i)

print(tuple_el[4])
del tuple_el[2]

print(tuple_el)
'''

#Set
'''set_el = {54,(1,232,False,4,False),True,False,0,1,213.321,'Hello'}
print(set_el)
print(type(set_el))
set_el.add('Pelmeni')
print(set_el)
a =set_el.copy()
set_el.clear()
print(set_el)
print(a)
new_set = {55,'Khinkhali',True,False,0,1,213.321,'Hello'}
print(a.difference(new_set))
print(new_set.difference(a))
a.difference_update(new_set)
print(a)

x = a.intersection(new_set)
print(x)
x= a.intersection_update(new_set)

set_1 = {"apple", "banana", "cherry"}
set_2 = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)
z = x.difference_update(y)
print(z)
z = set_1.intersection(set_2)
print(z)
set_2.intersection_update(set_1)
print(set_2)

set_1.discard('google')
print(set_1)
set_2.remove('banana')
print(set_2)

a= set_1.union(set_2)
print(a)
set_1.update(set_2)
print(set_1)

'''

#Frozen set
'''
names = frozenset({"Rafael", "Tengiz", "Orhan"})
print(names)
'''

#Dictionary

'''dict_el = {
    'bmw':['m5','m8','m3'],
    "rollce royce":
        {
        'fantom':2017,
        'ghost': 1950
            },
    'mclaren':'b1',
    'pagani':'huayra',
    'b':'m5'
}

print(dict_el['bmw'][2])
print(dict_el['rollce royce']['fantom'])

user_info = {
    'Emin':{
        'telephone':+994272673273,
        'email':'emineminchin@gmail.com',
        'home key':'home access'
    }
}'''

'''tel_code_tuple = [
    ("+994", "AZE"),
    ("+5", "USA"),
    ("+49", "Germany"),
)
users_dict = dict(tel_code_tuple)
print(users_dict)

users_dict['+380']='Ukraine'
print(users_dict)
users_dict['+380']='Ukraine country'
print(users_dict)'''

'''dict_el = {
    'bmw':['m5','m8','m3'],
    "rollce royce":
        {
        'fantom':2017,
        'ghost': 1950
            },
    'mclaren':'b1',
    'pagani':'huayra'
}
'''
#print(len(dict_el))
#print(dict_el['rollce royce'])
'''for key in dict_el.keys():
    print(key)
print('_'*50)
for value in dict_el.values():
    print(value)

for key,value in dict_el.items():
    print(f'key = {key} value = {value}')

key_sequences = range(1,5)
value = 10,124,90.1
thisdict = dict.fromkeys(key_sequences, value)
print(thisdict)

a = dict_el.get('bmw')
print(a)

b = dict_el.pop('mclaren')
print(b)
print(dict_el)


dict_el.popitem()
print(dict_el)


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

dict_el.update(car)
print(dict_el)'''


# Example
'''
Создайте программу «Англо-Русский словарь».
Нужно хранить слово на английском языке и его перевод
на русском. Требуется реализовать возможность добавления,
удаления, поиска, замены данных в словаре. Используйте
словарь для хранения информации.
'''
'''
# Создаем пустой словарь
dictionary = {}

# Определяем функцию для добавления новых слов
def add_word():
    pass
# Определяем функцию для удаления слов
def remove_word():
    pass

# Определяем функцию для поиска слов
def search_word():
    pass

# Определяем функцию для замены перевода слова
def replace_word():
    pass

# Определяем функцию main c бесконечным циклом для взаимодействия с пользователем (menu)
def main():
    pass'''
'''
dictionary = {}

def add_items():
    eng_word=input('Write a word in english ')
    rus_word=input('Write the translation of the word in russian ')
    dictionary[eng_word] = rus_word
    print(f'{eng_word} words translation is {dictionary[eng_word]}')
def del_items():
    eng_word = input('Write a word in english ')

    if eng_word in dictionary:
        del dictionary[eng_word]
        print(f'word {eng_word} was deleted from dictionary')
    else:
        print(f'word {eng_word} was not found in dictionary')
def find_items():
    eng_word = input('Write a word in english ')
    if eng_word in dictionary:
        print(f'word {eng_word} was found with translation {dictionary[eng_word]}')
    else:
        print(f'word {eng_word} was not found in dictionary')

def change_items():
    eng_word = input('Write a word in english ')
    rus_word = input('Write the translation of the word in russian ')
    if eng_word in dictionary:
        dictionary[eng_word] = rus_word
        print(f'word {eng_word} changed translation to {dictionary[eng_word]}')
    else:
        print(f'word {eng_word} was not found in dictionary,let`s add it')
        add_items()
def print_dict():
    print(dictionary)

def main():
    while True:
        choice = int(input('Choose option:'
                       '\n1. Add item'
                       '\n2. Delete item'
                       '\n3. Find item'
                       '\n4. Change item'
                       '\n5. Print all word in dictionary'
                       '\n--Write any number to exit--\n'))
        if choice==1:
            add_items()
        elif choice==2:
            del_items()
        elif choice==3:
            find_items()
        elif choice==4:
            change_items()
        elif choice==5:
            print_dict()
        else:
            print('Bye')
            break

main()'''