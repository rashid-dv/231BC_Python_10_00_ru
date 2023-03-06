'''
ASCII - Так как первые вычислительные машины были малоемкими,
для представления в их памяти всего набора требуемых знаков хватало 7 бит (или 128 символов).
 Сюда входил весь английский алфавит в верхнем и нижнем регистрах, цифры, знаки, вспомогательные символы.


 import string

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

Основная беда: имея 128 вариантов обозначить символ, мы никак не сумеем внедрить туда буквы других языков.
 В частности, какой-нибудь символ под номером 201 в кириллице даст совсем не русскую букву, если отослать его в Румынию.

UNICODE – связь символа и определенного числа без возможного повторения.
 Если мы кого-то попросим показать символ, скрытый под номером «1000», то в любой точке планеты он будет одним и тем же графическим элементом.
 \

 UTF 8 - UTF-8 – кодировка символов юникод в двоичном виде. Использует от 1 до 4 байт.
 Так как наиболее часто используемые символы занимают 1 байт (в частности, аски-символы),
 то UTF-8 оптимальна для английского текста, но не для азиатского.
'''
'''
Строки - неизменяемый тип данных




получение подстроки:

string[:end]: начиная с 0-го индекса по индекс end(не включительно)

string[start:end]:  начиная с индекса start по индекс end (не включительно)

string[start:end:step]: начиная с индекса start по индекс end через шаг step(не включительно)




Эскейп последовательность
Сырые строки

path = "C:\python\name.txt"
print(path)

path = r"C:\python\name.txt"
print(path)

Функции строк


upper() - Converts a string into upper case
casefold()	Converts string into lower case
capitalize()
lower()
title() -	Converts the first character of each word to upper case
swapcase() -	Swaps cases, lower case becomes upper case and vice versa
len()
print(ord("A"))  # 65 -Unicode
strip() - method removes any whitespace from the beginning or the end
replace()
split()
find() -	Searches the string for a specified value and returns the position of where it was found
'''




'''
string = "hello"
string_1 = 'hello'
string[-1] = "R"

print(string)'''


'''string = 'infinity'
print(string[:3])
print(string[2:6])
print(string[0:8:2])
print(string[0:12])
stroka = input()

print(len(stroka))'''
'''
string_1 = 'zAB'
string_2 = 'Zabz'

print(string_1>string_2)
'''
'''
string = 'first jiraf'
a = 'f'

print(a in string)
'''
# Пользователь вводит строку, проверить сколько раз тот или иной символ встречается в этой строке
'''
string = input('Vvedi slovo')
symbol = input('Vvedi symvol')
count = 0
for i in string:
    if i == symbol:
        count+=1
else:
    print(count)'''
'''
string = input('Vvedi slovo')

for i in range(0, len(string)):
    print(string[i], end='')
'''
# Polzovatel vvodit stroku, vivesti yeye v obratnoy zapisi

'''string = input()
#1
print(string[::-1])'''
#string = input()
#2
'''for i in range(1, len(string)+1):
    print(string[-i],end ='')'''
#3
'''string = input()
for i in range(len(string)-1,-1, -1):
    print(string[i], end='')
'''


'''
Escape sequence 

\n - перенести все что после меня на новую строку
\t - табуляция
\b - удалить предыдущий символ
\'
\"		
\\
'''

'''print('hello\nworld')
print('hello\tworld')
print('hello','\b','world')'''
'''string = '\"Мертвые Души\"'
print(string)

string_2 = input()
print('\'',string_2)'''

'''path = "C:\python\name.txt"
print(path)


path = r"C:\python\name.txt"
print(path)'''


'''upper() - Converts a string into upper case
casefold()	Converts string into lower case
capitalize() - first letter to upper case 
lower() - first letter to lower case
title() -	Converts the first character of each word to upper case
swapcase() -	Swaps cases, lower case becomes upper case and vice versa
len() - length of the string
print(ord("A"))  # 65 -Unicode
strip() - method removes any whitespace from the beginning or the end
replace()
split()
find() -	Searches the string for a specified value and returns the position of where it was found'''
'''
string = 'Hello'
string_1 = 'step'
string_2 = 'ACADEMY'
string_3 = 'ya hochu poest hinkali'
string_4 = '      yeda eto horosho'

print(str.lower(string))
print(str.capitalize(string_1))
print(str.upper(string_1))
print(str.casefold(string_2))
print(str.title(string_3))
print(str.swapcase(string_3))
print(ord("R"))
print(str.strip(string_4))

text = 'borsh'
print(text.replace('borsh','hinkali'))'''

'''string = input()
print(str.split(string))
print(string.find('o',0,5))'''


# Пользователь вводит с клавиатуры строку.
# Посчитайте сколько букв,символов и цифр есть в строке.
# Выведите оба количества на экран

bukvi = 'abcdefjhigklmnopjurszyvABCDEFJHIKLMOPKARSTVXYZ'
digits = '1234567890'

# Пользователь вводит с клавиатуры строку и символ
# для поиска. Посчитайте сколько раз в строке встречается
# искомый символ. Полученное число выведите на экран.