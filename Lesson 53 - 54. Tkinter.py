# PhotoImage
'''
Класс PhotoImage в библиотеке Tkinter используется для работы с изображениями в форматах GIF, PGM, PPM и PNG.

from tkinter import *

root = Tk()

root.geometry('500x400')
root.title('Test2')
root.iconbitmap(default='image_and_icons\programming.ico')

image = PhotoImage(file = 'image_and_icons\my_app.png' )
label = Label(image = image)
label.pack()

root.mainloop()

'''


# Checkbutton
'''
Элемент Checkbutton представляет собой флажок, который может находиться в двух состояниях: отмеченном и неотмеченном.

from tkinter import *

root = Tk()

root.geometry('500x400')
root.title('Test2')
root.iconbitmap(default='image_and_icons\programming.ico')

var = IntVar()

def click_checkbutton():
    print(var.get())
    if var.get() == 1:
        btn.config(state = ACTIVE)
    else:
        btn['state'] = DISABLED
count = 0

def clicker():
    global count
    count += 1
    btn['text'] = f'Clikcs = {count}'

check = Checkbutton(text = 'Put Check to open the button', variable= var,command=click_checkbutton)
check.pack()

btn = Button(text='Click on me',state = DISABLED,command= clicker)
#btn.place(relx = 0.1,rely = 0.2)
btn.pack()

root.mainloop()

'''

# Listbox
'''
ListBox - это виджет, который позволяет пользователю выбирать один 
или несколько элементов из списка. Каждый элемент списка отображается в отдельной строке,
и пользователь может выбрать элемент, щелкнув по нему мышкой или используя клавиши со стрелками на клавиатуре.

import tkinter as tk

root = tk.Tk()

# создание ListBox
listbox = tk.Listbox(root, selectmode=tk.SINGLE)#selectmode=tk.MULTIPLE
listbox.pack()

# добавление элементов
listbox.insert(1, "Элемент 1")
listbox.insert(2, "Элемент 2")

# получение выбранных элементов

def get_selection():
    selected_indices = listbox.curselection()
    selected_items = [listbox.get(i) for i in selected_indices]
    print("Выбранные элементы:", selected_items)
    return selected_items

button = tk.Button(root, text="Получить выбор", command=get_selection)
button.pack()

root.mainloop()
'''

#MassageBox
'''
MessageBox - это диалоговое окно, которое появляется на экране и предназначено для вывода сообщений пользователю. 
showinfo(): выводит информационное сообщение.
showwarning(): выводит сообщение предупреждения.
showerror(): выводит сообщение об ошибке.
askquestion(): выводит диалоговое окно с вопросом и двумя кнопками "Да" и "Нет".
askokcancel(): выводит диалоговое окно с вопросом и двумя кнопками "ОК" и "Отмена".
askyesno(): выводит диалоговое окно с вопросом и двумя кнопками "Да" и "Нет".

import tkinter.messagebox as messagebox
import tkinter as tk

root = tk.Tk()

def ask_question():
    answer = messagebox.askquestion("Вопрос", "Вы уверены, что хотите продолжить?")
    if answer == "yes":
        print("Пользователь нажал 'Да'")
    else:
        print("Пользователь нажал 'Нет'")

def show_message():
    messagebox.showinfo("Сообщение", "Это информационное сообщение.")

button = tk.Button(root, text="Показать сообщение", command=show_message)
button.pack()

root.mainloop()

'''


# Резкое закрытие окна
'''def finish():  # функция в которой с помощью метода destroy() вручную вызываем закрытие окна (а с ним и всего приложения)
    root.destroy()  # ручное закрытие окна и всего приложения
    print("Закрытие приложения")
root.protocol("WM_DELETE_WINDOW", finish)  # Первый параметр -имя события. Второй параметр представляет функцию,
# которая вызывается при возникновении события.  
'''


# Разметка при помощи менеджеров геометрии
'''
#pack
#grid
#place
'''



from tkinter import *

root = Tk()

root.geometry('500x400')
root.title('Test2')
root.iconbitmap(default='image_and_icons\programming.ico')

list_box = Listbox()
list_box.insert(0,'Khinkhali')
list_box.insert(1,'Adjiga')
list_box.insert(2,'Vino')

list_box.place(relx = 0.01,rely=0)


root.mainloop()




#Система Логина, если логин введен, мы нажимаем на кнопку, появляется вторая часть с паролем, мы вводим пароль, поялвяется кнопка сохранения данных