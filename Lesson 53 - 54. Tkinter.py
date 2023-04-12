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

from tkinter import *

root = Tk()

root.geometry('500x400')
root.title('Test2')
root.iconbitmap(default='image_and_icons\programming.ico')

def on_click():
    selected_element = list_box.curselection()
    selected_list = [list_box.get(i) for i in selected_element]
    print(selected_list)
    return selected_list

list_box = Listbox(selectmode=MULTIPLE)

list_box.insert(0,'Khinkhali')
list_box.insert(1,'Adjiga')
list_box.insert(2,'Vino')
list_box.place(relx = 0.01,rely=0)

btn = Button(text = 'Click on me', command= on_click)
btn.pack()

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

from tkinter import *
from tkinter import messagebox
root = Tk()

root.geometry('500x400')
root.title('Test2')
root.iconbitmap(default='image_and_icons\programming.ico')

def ask():
    answer = messagebox.askquestion('Ask window', 'Могу заполнить всю комнату или единственное сердце. '
                                                  'Однажды забрав, мной нельзя поделиться, что я?'
                                                  'Это одиночество?')
    if answer == 'Yes' or answer == 'yes':
        print('Thats ride, you solve the riddle')
    else:
        print('try again later')

def show():
    messagebox.showinfo('Information','Khinkhali Vkusno')

btn = Button(text = 'Show widow with question', command=show)
btn.pack()

root.mainloop()
'''


# Резкое закрытие окна
'''from tkinter import *

root = Tk()

root.geometry('500x400')
root.title('Test2')
root.iconbitmap(default='image_and_icons\programming.ico')

def finish():  # функция в которой с помощью метода destroy() вручную вызываем закрытие окна (а с ним и всего приложения)
    root.destroy()  # ручное закрытие окна и всего приложения
    print("Закрытие приложения")
root.protocol("WM_DELETE_WINDOW", finish)  # Первый параметр -имя события. Второй параметр представляет функцию,
# которая вызывается при возникновении события.  

btn = Button(text = 'Click',command=finish)
btn.pack()
root.mainloop()

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
root.title('Registration form')
root.iconbitmap(default='image_and_icons\programming.ico')
root.resizable(False,False)

lbl_reg = Label(text = 'Registration form',font = 'bold')
lbl_reg.place(relx= 0.3,rely= 0.1)

lbl_name = Label(text = 'Name and Surname',font = 'bold')
lbl_reg.place(relx= 0.2,rely= 0.2)

lbl_email = Label(text = 'Email',font = 'bold')
lbl_reg.place(relx= 0.2,rely= 0.3)

lbl_gender = Label(text = 'Gender',font = 'bold')
lbl_reg.place(relx= 0.2,rely= 0.4)

lbl_age = Label(text = 'Age',font = 'bold')
lbl_reg.place(relx= 0.2,rely= 0.5)

'''btn1 = Button(text = 'Hello')
btn1.grid(row = 5, column= 0,columnspan=2,sticky='w')
btn2 = Button(text = 'Goodbye')
btn2.grid(row = 6, column=1)'''

root.mainloop()


#Система Логина, если логин введен, мы нажимаем на кнопку, появляется вторая часть с паролем, мы вводим пароль, поялвяется кнопка сохранения данных