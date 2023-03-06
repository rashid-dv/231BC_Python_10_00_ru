''' Форматирование строк


# f"stroka....{x} stroka...  {y} stroka..." - 1 sposob
# text = "Hello, {first_name}.".format(first_name="Tom") - 2 sposob (immenovanniy)
#info = "Name: {0}\t Age: {1}".format("Bob", 23) - takje vtoroy sposob(parametr po poziciyi)
'''

# placeholders:
'''
s: для вставки строк
d: для вставки целых чисел
f: для вставки дробных чисел.
%: умножает значение на 100 и добавляет знак процента
e: выводит число в экспоненциальной записи

{"placeholder}
{:[количество_символов][запятая][.число_знаков_в_дробной_части] плейсхолдер}


string = "Hello {:s}"
name = "Tom"
formatted_string = string.format(name)
print(formatted_welcome)

takje rabotayet:
source = "{:d} символов"
source = "{:,d} символов" - zapataya dlya ukazaniya razradov chisla
number_1 = 11.213124142
print("{:.3f}".format(number))
print(f"{number_1:%}")
print(f"{number_1:.0%}")
print(f"{number_1:.1%}")



bez metodov format:
info = "Имя: %s \t Возраст: %d" % ("Tom", 35)
print(info)
'''

#Sep,End

#String library
'''
#biblioteka string pomogayet ispolzovat ves alfavit i ascii table tak je yego simvoli
import string
print(string.ascii_uppercase) #zaglavniye bukvi
print(string.ascii_lowercase) #malenkiye bukvi
print(string.ascii_letters) #vse bolshiye i malenkiye bukvi
print(string.digits) # 0-9 vse cifri
print(string.punctuation) #punktuaciya
print(string.hexdigits) #16-ch sistema schisleniya
print(string.octdigits) #8-richnaya sistema schisleniya
#vsevozmojniye dla printa
'''



#Functions
'''
isalpha(): возвращает True, если строка состоит только из алфавитных символов
islower(): возвращает True, если строка состоит только из символов в нижнем регистре
isupper(): возвращает True, если все символы строки в верхнем регистр
isdigit(): возвращает True, если все символы строки - цифры

lstrip(): удаляет начальные пробелы из строки
rstrip(): удаляет конечные пробелы из строки

join(strs): объединяет строки в одну строку, вставляя между ними определенный разделитель
myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)
'''





'''
digits = 5
symbols =2
print('Bez formata:')
print('Number of digits = digits \nNumber of symbols symbols ')
print('S formatom:')
print(f'Number of digits = {digits},\nNumber of symbols {symbols} ')
print(f'Number of digits = {digits},\nNumber of symbols {symbols}, overall symbols = {symbols+digits-} ')
'''

'''
number_1,number_2 = int(input()), float(input())
print('Number of chisel = {digit},\nNumber of simvoli {symbol}'.format(digit = number_1 ,symbol = number_2))
'''
'''
name=input("Dayte imya")
age=int(input("Dayte vozrast"))
height= float(input("Dayte rost"))
info = "Name: {0}\t Age: {1}, surname {0}, rost {2}".format(name, age, height) # takje vtoroy sposob(parametr po poziciyi)
print(info)
'''

'''string = "Zdrasti {:s}"
name = "Tom"
formatted_string = string.format(name)
print(formatted_string)
'''
'''

string = "Zdrasti agent {:d}"
code = int(input())
formatted_string = string.format(code)
print(formatted_string)

source = "{:,d} символов" # zapataya dlya ukazaniya razradov chisla
number = int(input())
formatted_source = source.format(number)
print(formatted_source)

'''
# vvoditsya diapozon chisel kotoriye vozvedut v stepen #1 -10
# vvoditsya vtporoy diapazon chisel kotoriy yavlayetsya stepenyu chisel pervogo diapazona # 3-5
#vivedite danniye ispolzuya formatirovaniye strok
'''
number_1 = int(input())
number_2 = int(input())

stepen_1 = int(input())
stepen_2 = int(input())

for i in range(number_1, number_2+1):
    for j in range(stepen_1,stepen_2+1):
        print(f'Number {i} in power {j} = {i**j}')
'''

#print("{:.9f}".format(number_1))
'''
number_1 = 125.12312314
#print(f"{number_1:.9f}")
print(f"{number_1:%}")

print(f"{number_1:.0%}")
print(f"{number_1:.1%}")
print(f"{number_1:.10%}")'''

'''
stroka = "Имя: %s Возраст: %d + %f" % ("Tom", 35, 25.97)
print(stroka)
'''


#print('Hello','World',"Pizza", sep= "\t-" , end=" ---Ya v konce stroki---- ")


#biblioteka string pomogayet ispolzovat ves alfavit i ascii table tak je yego simvoli

#from string import *
'''print(ascii_uppercase) #zaglavniye bukvi ascii table
print(ascii_lowercase) #malenkiye bukvi ascii table
print(ascii_letters) #vse bolshiye i malenkiye bukvi ascii stable
print(digits) # 0-9 vse cifri ascii table
print(punctuation) #punktuacionniye simvoli ascii table
print(hexdigits) #16-ch sistema schisleniya
print(octdigits) #8-richnaya sistema schisleniya
#vsevozmojniye dla printa
'''


#print("--------password generator--------")
import string
import random
'''upperCase = string.ascii_uppercase
lowerCase = string.ascii_lowercase
numbers =string.digits
symbols = string.punctuation
allSymbol = upperCase + lowerCase + numbers + symbols
print(allSymbol)
'''
'''#method_2
allSymbol=string.printable
password = ''
length = int(input("Vvedite dlinu parola:"))#10
for i in range(length+1):
    password+=random.choice(allSymbol)
print(password)
'''

'''strs = 'Tom'
myTuple = ("John", "Peter", "Vicky")

print(strs.join(myTuple))'''

'''
stroka = '         tom poel hinkali          '
text = stroka.title().strip()
print(text)
'''

'''for i in range(1,10):
    print('*'*i)'''
