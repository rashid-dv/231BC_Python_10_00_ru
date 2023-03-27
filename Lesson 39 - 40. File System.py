# 1.Файлы.
'''
Файл — это именованная область, расположенная во внешней памяти,
и обладающая следующими характеристиками:
■ имя файла (на определенном диске), которое позволяет программам идентифицировать файл
■ длина файла может быть ограничена только объемом диска.
'''
# 1.1Типы файлов, текстовые и бинарные.
'''
Текстовые файлы — это файлы хранящий в себе последовательность символов.
При передаче символов из потока на экран, часть из
них не выводится (например, символ сдвига на табуляцию, перевода строки).
Бинарные файлы - это файлы хранящие в себе  последовательность байтов,
которые однозначно соответствуют тому, что находится на внешнем устройстве
'''
# 1.2.Файловая система, особенности реализации форматов.
'''
Примеры текстовых файлов: (человек способен прочитать в любом текстовом редакторе)
■ web документы, стандарты: html, XML, CSS, JSON etc.
■ файлы исходных кодов: c, app, js, py, java etc.
■ текстовые документы: txt, tex, RTF etc.
■ текстовые представления табличных данных (файлы
с разделителями): csv, tsv etc.
■ файлы настроек и конфигураций: ini, cfg, reg etc

Примеры двоичных файлов:(человек не способен прочитать  в любом текстовом редакторе)
■ документы и электронные таблицы: .pdf, .doc, .xls etc.;
■ изображения: .png, .jpg, .gif, .bmp etc.;
■ видео: .mp4, .3gp, .mkv, .avi etc.;
■ аудио: .mp3, .wav, .mka, .aac etc.;
■ базы данных: .mdb, .accde, .frm, .sqlite etc.;
■ архивы: .zip, .rar, .iso, .7z etc.;
■ исполняемые файлы программ: .exe, .dll, .class etc.
'''
# 1.3.Работа с файлами:

'''
#открытие:
open(путь_к_файлу или переменная хранящая путь, режим открытия файла)
fileObj = open(fileName, mode)
fileName — это имя файла (или путь к нему), который вы хотите открыть.
При этом с именем вы должны указать и расширение. 
#закрытие;

#чтение:
read()
#запись:
write()
#закрытие:
close()

Режимы(моды):
Text file:
r - Открытие текстового файла только для
чтения. Если такого файла не существует, то
будет сгенерировано исключение
(обработка данных начинается с начала файла)

w - Открытие текстового файла только для
записи. Если такой файл не существует, то
он будет создан. Иначе его содержимое
будет удалено и файл будет перезаписан.
(обработка данных начинается с начала файла)

a - Открытие текстового файла для добавления.
Если такой файл не существует, то он будет
создан.
(обработка данных начинается с конца файла)

r+ - Открытие текстового файла для чтения и
записи. Если такого файла не существует, то
будет выведена ошибка.
(обработка данных начинается с начала файла)

w+ - Открытие текстового файла для чтения и
записи. Если такой файл не существует, то
он будет создан. Иначе его содержимое
будет удалено и файл будет перезаписан.
(обработка данных начинается с начала файла)

a+ - Открытие текстового файла для чтения и
добавления. Если такой файл не существует,
то он будет создан.
(обработка данных начинается с конца файла)


Binary file:
rb - Открытие двоичного файла для чтения.
Если такого файла не существует, то будет
выведена ошибка.
(обработка данных начинается с начала файла)

wb - Открытие двоичного файла для записи.
Если такой файл не существует, то он
будет создан. Иначе его содержимое будет
удалено и файл будет перезаписан.
(обработка данных начинается с начала файла)


ab - Открытие двоичного файла для добавления.
Если такой файл не существует, то он будет
создан. Иначе данные из него будут удалены
(обработка данных начинается с конца файла) 

wb+ - Открытие двоичного файла для чтения и
записи. Если такой файл не существует, то
он будет создан. Иначе его содержимое
будет удалено и файл будет перезаписан.
(обработка данных начинается с начала файла)

ab+ - Открытие двоичного файла для чтения и
добавления. Если такой файл не существует,
то он будет создан. Иначе его содержимое
будет удалено
(обработка данных начинается с конца файла)
'''

# 1.4.Менеджер контекста with.
'''
Оператор with используется при обработке исключений, чтобы сделать код более чистым и читабельным.
 Это упрощает управление общими ресурсами, такими как файловые потоки.
Преимущество использования ключевого слова with перед вызовом функции open() в том, что функция file.close() 
 вызовется автоматически и освободит занятые ресурсы после того, как отработает код.

 без with:
try:
    somefile = open("test.txt", "w")
    try:
        somefile.write("hello world")
    except Exception as e:
        print(e)
    finally:
        somefile.close()
except Exception as ex:
    print(ex)

с with:
with open(file, mode) as file_obj:
    инструкции

#Porblem of coding 
with open(filename, encoding="utf8") as file:
'''

# 1.4.1 Функции для чтения файлов
'''
with open("hello.txt", "r") as file:
    for line in file:
        print(line, end="")

readline(): считывает одну строку из файла

read(): считывает все содержимое файла в виде одной единой строки

readlines(): считывает все строки файла в список
with open("hello.txt", "r") as file:
    contents = file.readlines()
    str1 = contents[0]
    str2 = contents[1]
    print(str1, end="")



'''

# 1.4.2 Функции для записи файлов
'''
1. write()

2. writelines(набор_элементов)
with open("hello.txt","a") as FileHandler:
    myStrs = ["Appended line 1\n", "Appended line 2\n"]
    FileHandler.writelines(myStrs)
'''

# 1.5.Практические примеры использования.
'''
1. Поиск и замена слов в содержимом текстового файла
2. Подсчет количества слов в содержимом текстового файла, которые не являются числами
3. Вывести слова содержимого файла в обратном порядке
4.  Удаление заданной по номеру строки из файла
'''

# 2.Бинарные файлы
'''
Бинарные файлы в отличие от текстовых хранят информацию в виде набора байт.
'''
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


import pickle

FILENAME = "users.doc"

users = [
    ["Tom", 28, True],
    ["Alice", 23, False],
    ["Bob", 34, False]
]

with open(FILENAME, "wb") as file:
    pickle.dump(users, file)

with open(FILENAME, "rb") as file:
    users_from_file = pickle.load(file)
    for user in users_from_file:
        print("Имя:", user[0], "\tВозраст:", user[1], "\tЖенат(замужем):", user[2])
'''

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

# https://metanit.com/python/tutorial/4.3.php
# https://metanit.com/python/tutorial/4.6.php
# https://metanit.com/python/tutorial/4.5.php
# https://metanit.com/python/tutorial/4.7.php


'''def fileWork(file,fileMode,info = None):
    fileHandler = open(file,fileMode)
    if fileMode == "w":
        fileHandler.write(info)
    elif fileMode =="r":
        print(fileHandler.read())
    elif fileMode == "a":
        fileHandler.write(info)
    else:
        return -1
    fileHandler.close()

fileName = input('Write file name: ')

while True:
    choice = int(input("what do you want to do with file:\n1.Rewrite info\n2.Print info.\n3.Add info\n"))
    if choice==1:
        info = input("Rewrite info from file to:\n")
        fileWork(fileName,"w",info)
    elif choice==2:
        fileWork(fileName,"r")
    elif choice == 3:
        info = input("Rewrite info from file to:\n")
        fileWork(fileName,"a",info)
    else:
        break
'''

'''
try:
    fileHandler= open("FileSys3.txt","w")
    try:
        fileHandler.write("Нет лучше еды на свете, чем хинкали")
    except Exception as e:
        print(f"1.Program interrupted by the error: {e}")
    finally:
        fileHandler.close()
except Exception as ex:
    print(f"2.Program interrupted by the error: {ex}")'''

#with open(r"C:\Users\Aghashirinov_r\PycharmProjects\pythonProject\files\FileSys.txt","r") as fileHandler:
 #   print(fileHandler.read())

#with open(r"C:\Users\Aghashirinov_r\PycharmProjects\pythonProject\files\FileSys3.txt", "r") as file:
#print(file.readline())
#print(file.readlines())
#print(file.read())


# with open(r"C:\Users\Aghashirinov_r\PycharmProjects\pythonProject\files\FileSys3.txt","a") as FileHandler:
#     myStrs = {"First":"\nHello","Second":"\nWorld"}
#     FileHandler.writelines(myStrs)


# Example
# записывать введенный пользователем массив строк и считывать его обратно из файла на консоль:

my_file_path = r"C:\Users\Aghashirinov_r\PycharmProjects\pythonProject\files\FileArrayString.txt"
list_strings = list()

for i in range(4):
    str = input("Add line info:\n")
    list_strings.append(str)


with open(my_file_path,"a") as file:
    for i in list_strings:
        file.write(i)

with open(my_file_path,"r") as file:
    print(file.read())
    data = file.read()
    data.isalpha()


