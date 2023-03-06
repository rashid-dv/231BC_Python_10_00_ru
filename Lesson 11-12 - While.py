
'''
number_1 = float(input('Введите первое число:')) # -7
#number_2 = float(input('Введите второе число:')) # 2

celaya = number_1//2 # -7.2 // 2 = - 4
celaya_2 = abs(number_1)//2 # -7.2 // 2 = - 4

print(celaya, celaya_2)

'''

'''
if int(input())>0:
    print()
    s = 10+2
    if int(input())%2 == 0:
        print('chetnoye')
'''


'''
number = 1

while number!=5: # true , to yest poka number ne raven 5
    number += 1 #  number = number +1 => 1+1 = 2
    print(number) # 2
    break # stop loop and ignore everything after it
else:
    print('hello loop is over')

print('loop was working ', number , 'times')

'''

'''
number = int(input('input number:'))
while number<1000:

    if number>10 and number<100:
        continue
    else:
        print(number)
'''

#Practise 1. Пользователь вводит однозначное  число, если
# это число четное то на экран выводится таблица умножения этого числа
# Как только умножение дошло до 10 числа , цикл останавливается
#Example: number = 7, result: 7,14,21,28,35,42,49,56,63,70.

'''
number= int(input())
counter = 1
if number<10 and number>0:
    if number%2==0:
        while counter<=10:
            print(number,'*',counter,'=', number*counter)# 7*1, 7*2, 7*3, 7*4
            counter+=1
        else:
            print('Loop is over')
    else:
        print('cto-to')
else:
    print('bolshoye chislo')
'''
#Написать программу, которая по выбору
# пользователя возводит введенное им число(вводить можно сколько угодно раз)
# в степень от нулевой до седьмой включительно.

'''
count=0
while  count<10: # 1 raz otrabotal=>2
    stepen = 0
    number = float(input())
    while stepen>=0 and stepen<7: # 7 raz otrabotal, 7 raz otrabotal
        print(number**stepen)
        stepen+=1
    else:
        print('vtoroy cikl otrabotal ', stepen, 'raz')
    count+=1
    print('perviy cikl otrabotal ', count, 'raz')
    if count == 3 :
        break

else:
    print('ves perviy ciklotrabotal ', count, 'raz')
'''



'''
range_1 = int(input("Please, Enter the Range Value: ")) #10
range_2= int(input("Please, Enter the Range Value: "))#10
number = 2
number2 = 1
print("The Простые числа in the range are: ")
while number<=range_1:# 2<10
  counter=0
  if number==2:
    print(number)
  number += 1 # 3
  while number2<=range_2: #1 - 10
    if number%number2==0:
        counter=1
        continue
    number2+=1
  if counter==0:
    print(number)
'''
