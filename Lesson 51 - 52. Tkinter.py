# Tkinter
'''
Tkinter - это стандартная библиотека Python для создания
 графических пользовательских интерфейсов (GUI).
 Она предоставляет возможность создавать окна,
 кнопки, текстовые поля, меню, диалоговые окна и другие элементы интерфейса.


Tkinter базируется на библиотеке Tcl/Tk, которая написана на
на языке программирования Tcl и является кросс-платформенной,
что означает, что приложения, созданные с помощью Tkinter,
могут работать на разных операционных системах, таких как Windows, Linux и Mac.
'''

# Отличия консольных и GUI приложений.
'''
Консольные приложения (CLI - Command Line Interface) и приложения с 
графическим интерфейсом (GUI)  представляют собой два разных 
подхода к созданию программного обеспечения. 

Основные отличия между ними:

Взаимодействие с пользователем:
В консольных приложениях пользователь вводит команды в командной строке,
то время как в GUI приложениях пользователь может использовать
мышь и клавиатуру, чтобы взаимодействовать с элементами интерфейса.

Визуальный интерфейс:
GUI приложения имеют графический интерфейс, что позволяет 
пользователям легко управлять приложением с помощью кнопок,
меню и других элементов интерфейса.
Консольные приложения, напротив, не имеют графического
интерфейса и представляют собой текстовую командную строку.

Сложность:
GUI приложения могут быть более сложными в создании, поскольку 
они требуют создания графического интерфейса и управления 
элементами интерфейса. Консольные приложения могут быть более 
простыми в создании, так как они просто выполняют задачи на
основе команд, введенных пользователем в командной строке.


Переносимость: 
Консольные приложения могут быть более переносимыми, поскольку
они не зависят от графического интерфейса операционной системы 
и могут быть запущены на разных платформах. 
GUI приложения могут быть менее переносимыми, поскольку графический
 интерфейс может быть зависимым от операционной системы.

Возможности: 
GUI приложения могут обеспечивать более широкий спектр функций и 
возможностей, так как они могут использовать графический интерфейс 
для предоставления дополнительных функций и удобств. 
Консольные приложения, напротив, могут быть более ограниченными в своих 
возможностях, так как они ограничены текстовой командной строкой.

'''

# Создание окна
'''
from tkinter import *

root = Tk()  # создаем корневой объект - окно

root.title("First application")  # устанавливаем заголовок окна
root.iconbitmap(default="file.ico") # Установка иконки.  параметр default в метод iconbitmap передается путь к иконки

#Alternative iconbitmap:
image = PhotoImage(file = 'image_and_icons\my_app.png')
root.iconphoto(False,image) #Первый параметр казывает, надо ли использовать иконку по умолчанию для всех окон приложения.

root.geometry("350x400")  # устанавливаем размеры окна
root.geometry('500x500+500+200') # Устанавливаем размеры окна и задаем его координаты

root.config(width=300, height=500,bg='black') #используется для изменения настроек виджета, таких как ширина, высота, цвет фона и т.д.
# Mетод geometry() используется для установки размеров и положения окна на экране, а метод config() - 
# для изменения настроек виджета, таких как ширина, высота, цвет фона и т.д.

# root.minsize(300,300) минимальный такой будет
# root.maxsize(800,800) макс и не более

root.mainloop()

'''

# Создание и использование виджетов
'''
Виджет - это элемент пользовательского интерфейса в графическом 
оконном приложении. Виджеты обычно представляют собой кнопки, 
поля ввода, переключатели, флажки, таблицы, меню и многие другие 
элементы, которые пользователь может использовать для взаимодействия с приложением.

#Button

#Entry

#Label

#PhotoImage

#Checkbutton

#Listbox

#Text
'''

# Label
'''
Label - это виджет в библиотеке Tkinter, который используется для отображения
 текста или изображения на графическом интерфейсе.

from tkinter import *

root = Tk()
root.geometry('600x400')
root.resizable(False,False)
root.title('Test')
root.iconbitmap(default='image_and_icons\programming.ico')


lbl = Label(text = 'No name')
lbl.config(fg= '#003366',bg='#006600',font = ('Arial',32,'bold', 'italic', 'underline'))
lbl.pack()
lbl.place(x= 100, y = 100)

root.mainloop()
'''

#Задание
'''
Сделайте так, чтобы у вас на экране высветилось следующее:

Fruits
1)apple
2)mango
3)pear
4)orange

каждое слово должно быть разных цветов

from tkinter import *
root = Tk()
root.geometry('600x400')
root.resizable(False,False)
root.title('Test')
root.iconbitmap(default='image_and_icons\programming.ico')

fruits = ['fruits','apple','mango','banana']
colors = ['Black','red','Orange','Yellow']


for i in range(len(fruits)):
    lbl = Label(text= f'{i+1}) {fruits[i]}',fg = colors[i])
    lbl.pack()

root.mainloop()

'''


# Button
'''
Основные параметры виджета Button:

command: функция, которая вызывается при нажатии на кнопку

def say_hello():
    print("Hello, World!")
my_button = Button(root, text="Click Me!", command=say_hello)#say_hello без скобок, т.к. мы передаем ссылку на нашу функцию, если укажем скобки, то программа будет пытаться сразу запустить функцию
my_button = Button(root, text="Click Me!", command= lanbda:say_hello())#say_hello() в лямбде , чтобы можно было передать аргументы в функии 

image: ссылка на изображение, которое отображается на метке

photo = PhotoImage(file="my_image.png")
my_button = Button(root, text="Click Me!", image=photo, compound="left")

state: состояние кнопки
my_button = Button(root, text="Click Me!", state="disabled")

text: устанавливает текст метки
width: ширина виджета

button = Button(text='Click on me',bg='red',font='Roboto 20',width=20,height=5)


'''

#Задание
'''
при кликании на кнопку его фон должен поменять
цвет и остаться таким(background)
'''

# Entry
'''
Entry - это виджет для создания поля ввода
текста, куда пользователь может вводить текст или числа.

background: фоновый цвет
foreground: цвет текста
font: шрифт текста
justify: устанавливает выравнивание текста. Значение LEFT, CENTER, RIGHT 
show: задает маску для вводимых символов
state: состояние элемента, может принимать значения NORMAL (по умолчанию) и DISABLED
width: ширина элемента
insert(index, str): вставляет в текстовое поле строку по определенному индексу
get(): возвращает введенный в текстовое поле текст
delete(first, last=None): удаляет символ по индексу first. Чтобы удалить до конца, в качестве второго параметрa END.
selectbackground-при выделении текста изменение его заднего фона
selectforeground-при выделении текста изменение его цвета шрифта

'''



'''from tkinter import *

root = Tk()
root.geometry('600x400')
root.resizable(False,False)
root.title('Test')
root.iconbitmap(default='image_and_icons\programming.ico')

count = 0
def clicker():
    global count
    count+=1
    btn['text']= 'Clicks = ', count # f'Clikcs = {count}'


btn = Button(root, text= 'Click on me', state = DISABLED,command=clicker, width = 20, height=10)
btn['state']= ACTIVE
btn.pack()


root.mainloop()'''



from tkinter import *

root = Tk()
root.geometry('600x400')
root.resizable(False,False)
root.title('Test')
root.iconbitmap(default='image_and_icons\programming.ico')

entry = Entry()
entry.pack()

def clear():
    entry.delete(0,END)

def on_button_click():
    text = entry.get()
    res_str = 'Name - ' + text
    res_name_lbl.config(text = res_str)
    print(text)
    entry.delete(0,END)

name_lbl = Label(text = 'Name: ')
name_lbl.pack()
button2 = Button(text="Click to save info!", command=on_button_click)
button2.pack()
res_name_lbl = Label(text = 'No name')
res_name_lbl.pack()

btn = Button(root, text= 'Click on me',command=clear)
btn.pack()


root.mainloop()