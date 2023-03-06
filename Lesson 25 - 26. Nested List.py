'''
_______________________________________________________
from random import shuffle

size = int(input('Enter the size of your list: '))
list_el = []
for i in range(size):
    list_el.append(int(input('Enter your elements: ')))
print(list_el)


shuffle(list_el)
print(list_el)


names = ['Java', 'Python']
delimiter = '_____'
single_str = delimiter.join(names)
print(single_str)# result is not list it is string.

s = 'i Learn Python language'
print(s.capitalize())
___________________________________________________________________
'''
# Practise:
'''
1. На вход программе подается одна строка с буквами английского языка. Напишите программу, которая определяет количество гласных и согласных букв.
2. На вход программе подается одна строка. Напишите программу, которая определяет сколько в ней одинаковых соседних символов.(aabbcc - 3 , aabb - 2 ,abcd - 0)
3. На вход программе подается один список. Напишите программу, которая определяет сколько в нем одинаковых соседних символов.
4. На вход программе подается натуральное число, записанное в десятичной системе счисления. 
Напишите программу, которая переводит данное число в двоичную систему счисления.
'''
# Nested List
'''
list1 = ['Person 1','Surname 1', 20, 'Aze']
list2 = ['Person 2','Surname 2', 30, 'USA']
overall = [list1,list2]
print(overall)
'''

'''Students_data = [['Name 1','Surname 1','20 years old'],
                ['Name 2','Surname 2','40 years old'],
                ['Name 3','Surname 3','50 years old']]

for i in range(len(Students_data)):
    for j in range(len(Students_data[i])):
        Students_data[1].append(4)
        print(Students_data[i][j], end=' ')
    print()


'''
# Заполнение вложенного списка рандомными числами:

'''
#1 способ:
m, n = 3, 4  # размерность списка
lst = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(random.randint(1, 10))
    lst.append(row)

#2 способ:
lst = [[random.randint(1, 10) for j in range(n)] for i in range(m)]

'''

# Practise:
# 1.Вводится двумерный список(список внутри которого еще один список) размера m на n. Его значения заполнены случайными числами.
#   1.1. Найти сумму элементов всех его чисел.
#   1.2. Найти сумму всех положительных.
#   1.3. Найти сумму всех отрицательных.
#   1.4. Найти сумму всех четных.
#   1.5. Найти сумму всех не четных.
#   1.6. Найти сумму всех простых чисел
#   1.7. Определить количество простых чисел в списке.

'''
knijnaya_polka = [['Code Da\'Vinchi', 'Den Brown#1', 400, 2000],
                  ['Inferno ', 'Den Brown#2', 600, 2001],
                  ['Shantaram', 'Ne znayem', 601, 2005],
                  ['Война и Мир', 'Л. Толстой', 430, 1965]]

kniga_1= ['Code Da\'Vinchi', 'Den Brown#1', 400, 2000]
kniga_2 = ['Inferno ', 'Den Brown#2', 600, 2001]
kniga_3 = [kniga_1+kniga_2]
print(kniga_3)'''
'''
n, m = map(int, input().split())
for i in range(n):  # len knijnoy polki = 4 , i budet raven = 0,1,2,3
    # i=0 if
    for j in range(m):  # j=0,1,2,3, pri etom obrashayemsya k kajdomu vlojennomu spisku po otdelnosti
        
        print(knijnaya_polka[i][j], end=' ')

    print()'''


from random import  randint
n,m = map(int,input().split())
list_el = [[randint(-100,100) for j in range(m) ]for i in range(n)]
print(list_el)
summ =0

for i in range(0,len(list_el)):# 0 - 4
    for j in range(0,len(list_el[i])):# 0 - 5
        summ+=list_el[i][j] #summ+= list_el[0][0], [0][1],[0][2]

print(f'Overall summ = {summ}')