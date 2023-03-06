#break - прерывает незамедлительно работу цикла и выходит из него, игнорируя все, что находится после себя
# continue - заставляет цикл сразу перейти к следующей итерации, игнорируя все что нахходится после себя

# for переменная in набор_значений(набор_значений может быть как строка, как булевый тип данных, как диапозон элементов и как просто числа введенные подряд):
#  instrtions(инструкции к циклу/ тело цикла)

#range(start,end,step)

'''for i in range(1,10):
    if i%2==0:
        print(i)
        break

else:
    print('Loop is over')'''

'''for i in range(1, 10):
    if i%2==0:
        print(i)
        break
else:
    print('Loop is over')'''

'''x = int(input())
y = int(input())
for i in range(x, y):
    print(i)
    if i!=0:
        deleniye = y/i
        print(deleniye)
    else:
        continue

    print(i)
else:
    print('Loop is over')'''

#for i in True,True,False:
 #   print(i)

#for i in range( 11.7, 22.9): # tak pisat nelza!!!!!!!
#    print(i)
#for i in range(False,True+1): # predstavleniye True kak 1, False kak 0
#    print(i)

#for i in range('hello', 'world'):# tak pisat nelza!!!!!!!
#    print(i)

'''for i in range(1,10):
    print(i)

print('____________')

a=int(input())
b=int(input())

for c in range(a,b-1,-1):
    print(c)

print('____________')
#for j in range(1,10,-1):# range ne otrabotayet
#    print(j)'''

# PRACTISE


#1. Пользователь вводит с клавиатуры два числа.
# Нужно показать все четные числа в указанном
# диапазоне в порядке убывания.

'''start = int(input())
end = int(input())
for i in range(end,start-1, -1):
    if i%2==0:
        print(i)
'''


#2.Пользователь вводит число. Посчитать сумму чисел в диапозоне от 1 до этого числа и
# найти среднее-арифметическое.

'''number = int(input())
summ =0
for i in range(1,number+1):
    summ += i


print('summa= ', summ,'sredne-arifm =',summ/number)'''

'''
from random import randint # из библиотеки/модуль импортировать функцию  randint()

random_number = randint(2,6)

print(random_number)
'''



'''#Пользователь вводит с клавиатуры число. Требуется
#посчитать факториал числа. Например, если введено 3,
#факториал числа 1*2*3 = 6.
#Формула для расчета факториала: n! = 1*2*3…*n, где
#n — число для расчета факториала.
from random import randint

number = int(input())
random_number = randint(-number,number)
faktorial = 1

if random_number<=0:
    for i in range(random_number,0):
        faktorial*=i
        print(faktorial)
else:
    for i in range(1,random_number+1):
        faktorial*=i
        print(faktorial)'''


'''# 1*.Вводится два числа х и у , возведите все числа в диапозоне от х к у в степень y ,не используя оператор **
# 2. Написать программу – конвертер валют(5 valyut vsego)

USD= 1.78
TEL =1.78


while True:
    number = int(input("Summa v manatax"))
    choice = int(input('VIBOR:'
                       '\n1)USD'
                       '\n2)TEL'
                       '\n3) Viyti iz obmennika\n'))
    if choice == 1:
        print(number*USD)
    elif choice ==2:
        print(number*TEL)
    elif choice == 3:
        break'''