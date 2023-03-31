#Codition operators
#and - True and True, false and false
#or - false or true, true or false
#not - отрицание
'''
a = int(input())#67

if a >= 0 and a<10:#1-9

    print('cto-to')

elif a>10 and a<20: #11 - 19
    print(a)

elif a>20 and a<100: #21 - 99
    print('b')
else:
    print('c')
'''

'''
#Пользователь вводит два дробных числа.
# Найдите сумму их целых и дробных частей.
# (Например: 1,5 и 3,2 - Целая часть дает в сумме 4,
# дробная часть дает в сумме 0,7)
number_1 = float(input())
number_2 = float(input())

#//
celoye_1 = number_1 // 1
celoye_2 = number_2 // 1

#drobnoya_1 = ((number_1*10)%10)/10
drobnaya_1 = number_1 - celoye_1 # ostatok chisla
drobnaya_2 = number_2 - celoye_2 # ostatok chisla

print(celoye_1+celoye_2, drobnaya_1+drobnaya_2)
'''

'''
print(round(1.5)) # 2
print(round(2.5)) # 2 
'''

'''
#Напишите программу, которая находит F процентов от N числа.
# (ввод F и N пользователем)
chislo = float(input())
percent= float(input())
operation = (chislo * percent)/100
print(operation)
'''
'''
#На экране вводится  число, если оно трехнзначное,
# мы ешл записываем в обратном порядке, а если оно
# 4-х значное то берем сумму его чисел, иначе выводится слово error.
# (например, введено 357, должно отображаться 753)

chislo = int(input()) # 157

# 100 - 999
if chislo >= 100 and chislo < 1000:
    posledneye = chislo % 10  #
    sredneye = (chislo // 10) % 10  #
    pervoye = chislo // 100  #
    print(posledneye * 100 + sredneye * 10 + pervoye)

elif chislo >= 1000 and chislo<10000:
    #1936
    posledneye = chislo % 10  # 6
    sredneye = (chislo // 10) % 10  # 3
    vtoroye = (chislo // 100)%10  # 9
    pervoye = chislo // 1000 #1
    print(pervoye+vtoroye+sredneye+posledneye)
else:
    print('error')
'''

# Вводится целое число, если оно является положительным
# то нужно  вывести соответствующее сообщение и проверить является ли оно четным
#если да, то вывести это число
#если нет, то вывести ошибку
#И если же число не положительное , то проверить является ли оно нечет


counter = 1 # kolichestvo zapolneniy bochka

while counter!=0: #poka bochok ne zapolnitsya do konca
    print("Nalil vodu")
    counter += 1 #counter = counter +1
    print(counter)
    if counter == 10:
        break





print("URA , bochok polon")
