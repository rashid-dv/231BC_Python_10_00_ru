# 2.Бинарные файлы
'''
Бинарные файлы в отличие от текстовых хранят информацию в виде набора байт.
'''
# from pickle import dump,load
# car = 'Tesla'
# year = 2016
#
# with open(r"C:\Users\Aghashirinov_r\PycharmProjects\pythonProject\files\test.png", "wb") as fileHandler:
#     dump(car,fileHandler)
#     dump(year,fileHandler)
#
# with open(r"C:\Users\Aghashirinov_r\PycharmProjects\pythonProject\files\test.png", "rb") as fileHandler:
#     print(load(fileHandler))
#     second = load(fileHandler)
#     print(f'{second} this type has value = {second}')

# 2.1.Binary methods
'''
import pickle - модуль необходимый для работы с бинарными файлами

dump(obj, file): записывает объект obj в бинарный файл file
load(file): считывает данные из бинарного файла в объект

import pickle

FILENAME = "user.dat"

name = "Tom"
age = 19

with open(FILENAME, "wb") as file:
    pickle.dump(name, file)
    pickle.dump(age, file)

with open(FILENAME, "rb") as file:
    name = pickle.load(file)
    age = pickle.load(file)
    print("Имя:", name, "\tВозраст:", age)



'''

#from pickle import dump,load

#doc_file = r'C:\Users\Aghashirinov_r\PycharmProjects\pythonProject\files\test.doc'
'''
Car = ['BMW','Rolls-Royce','Porshe','Bugatti']
Cars_info = [['BMW','m5',2022,2.8],
             ['Rolls-Royce','GHOST',2020,4.5],
             ['Porshe','Taycan',2019,2.7],
             ['Bugatti','Chiron',2018,2.1]]

with open(doc_file,"wb") as fileHandler:
    for i in Cars_info:
        dump(i,fileHandler)

with open(doc_file,"rb") as fileHandler:
    for i in range(len(Cars_info)-1):
        x = load(fileHandler)
        print(x)
        for j in range(len(Cars_info[i])):
            print(f'position number = {j} has element with value = {x[j]}')
'''

#image = r'C:\Users\Aghashirinov_r\Downloads\python.png'
'''with open(doc_file,'wb') as file:
    with open(image, 'rb') as image:
        file.write(image.read())'''

'''1. Поиск и замена слов списка в содержимом бинарного файла
2. Подсчет количества слов и чисел(по отдельности) в содержимом бинарного файла
3. Вывести слова спрятанные за ключами в словаре в содержимом бинарном файле
'''

from pickle import dump,load
doc_file = r'C:\Users\Aghashirinov_r\PycharmProjects\pythonProject\files\test.doc'

list_el = ['a','b','c',1,2,3,4]
with open(doc_file,"wb") as fileHandler:

        dump(list_el,fileHandler)

with open(doc_file,'rb') as fileHandler:
    temp = load(fileHandler)
    slovo_nayti = input()
    slobo_zamenit = input()
    for i in range(len(list_el)):
        if temp[i]==slovo_nayti:
            temp[i]=slobo_zamenit
    with open(doc_file,'wb') as fileHandler:
        dump(temp,fileHandler)

with open(doc_file, 'rb') as fileHandler:
    print(load(fileHandler))
# 3.Установщик пакетов pip
'''
Система управления пакетами, которая используется для установки и
 управления программными пакетами, написанными на Python
'''
# 3.1.Необходимость использования
'''
Update pip:
python -m pip install --upgrade pip

Install Specific Version of a Package:
pip install <package-name>==<version>

Uninstall a Package:
pip uninstall <package-name

Information About an Installed Package
pip show <package name>

List All Installed Packages
pip list

Searching for Packages
pip search "query"

py -m pip install SomePackage-1.0-py2.py3-none-any.whl

'''

