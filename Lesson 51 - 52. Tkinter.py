# Tkinter
'''
Tkinter - это стандартная библиотека Python для создания
 графических пользовательских интерфейсов (GUI).
 Она предоставляет возможность создавать окна,
 кнопки, текстовые поля, меню, диалоговые окна и другие элементы интерфейса.


Tkinter базируется на библиотеке Tcl/Tk, которая написана э
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
# icon = PhotoImage(file = "icon2.png")
# root.iconphoto(False, icon) #Первый параметр казывает, надо ли использовать иконку по умолчанию для всех окон приложения.

root.geometry("350x400")  # устанавливаем размеры окна
root.geometry('500x500+500+200') # Устанавливаем размеры окна и задаем его координаты

root.config(width=300, height=500,bg='black') #используется для изменения настроек виджета, таких как ширина, высота, цвет фона и т.д.
# Mетод geometry() используется для установки размеров и положения окна на экране, а метод config() - 
# для изменения настроек виджета, таких как ширина, высота, цвет фона и т.д.

# root.minsize(300,300) минимальный такой будет
# root.maxsize(800,800) макс и не более


label=Label()
label = Label(text="Hello students")  # создаем текстовую метку
# label.config(text='Hello world',fg='yellow',bg='black',font='Arial 20 bold italic')
label.pack()  # размещаем метку в окне
label.pack(side = LEFT, anchor = SE)
label.place(x = 50, y =100)  

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
root.geometry('400x300')
root.resizable(False,True)
text = Label(text='Life is good',font='Roboto 20',fg='black',bg='yellow')
text.pack()

clicks = 0
def click():
    global clicks
    clicks += 1
    button['text']='Clicks',clicks#f"Clicks {clicks}"

button = Button(text='Click me',command=click)
button.config(background='blue',fg='yellow')
button.pack()
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
'''
'''fruits = ['apple','mango','pear','orange']
colors = ['lightblue','orange','red','black']
label = Label(window, text = 'Fruits', fg = colors[1], font = ('Comic Sans MS' , 18, bold)
    label.pack()

for i in range(len(fruits)):
    label = Label(window, text = f'{i+1}) {fruits[i]}', fg = colors[i], font = ('Comic Sans MS' , 15, bold)
    label.pack()
'''

# Button
'''
Основные параметры виджета Button:

command: функция, которая вызывается при нажатии на кнопку

from tkinter import *
def say_hello():
    print("Hello, World!")
root = Tk()
my_button = Button(root, text="Click Me!", command=say_hello)#say_hello без скобок, т.к. мы передаем ссылку на нашу функцию, если укажем скобки, то программа будет пытаться сразу запустить функцию
my_button = Button(root, text="Click Me!", command= lanbda:say_hello())#say_hello() в лямбде , чтобы можно было передать аргументы в функии 
my_button.pack()
root.mainloop()

image: ссылка на изображение, которое отображается на метке

from tkinter import *
root = Tk()
photo = PhotoImage(file="my_image.png")
my_button = Button(root, text="Click Me!", image=photo, compound="left")
my_button.pack()
root.mainloop()

state: состояние кнопки

from tkinter import *
root = Tk()
my_button = Button(root, text="Click Me!", state="disabled")
my_button.pack()
root.mainloop()

text: устанавливает текст метки
width: ширина виджета

from tkinter import*
window = Tk()
button = Button(text='Click on me',bg='red',font='Roboto 20',width=20,height=5)
button.pack()
window.mainloop()

'''

#Задание
'''
при кликании на кнопку его фон должен поменять
цвет и остаться таким(background)
'''
'''
from tkinter import *
def say_hello():
    button.config(bg='violet', text='wow')
root = Tk()
button = Button(text='Click',bg='red',fg='red',font='Roboto 20',width=20,height=5, command=say_hello)
button.config(activebackground='green',activeforeground='White',bd=5,pady=20,state=ACTIVE)

button.pack()
root.mainloop()'''

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

from tkinter import *
root = Tk()

entry = Entry()
entry.config(background='#afc3e3',font='Roboto 20 bold',justify=LEFT,selectbackground='yellow',selectforeground='blue',bd=15)
entry.insert(0,'0')
entry.pack()

def clear():
    entry.delete(0,END)

button1 = Button(text='Clear',command=clear)
button1.config(background='green')
button1.pack()

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
root.mainloop()

'''





