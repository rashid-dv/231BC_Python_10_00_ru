'''
number1 = 1
number2 = 1
while number1<=10:#1<10 #2<10#3
    while number2<=10 and number1%2==0:#1<10
        print(number1*number2,end ='\t')
        number2+=1 #10
    else:
        print('\n')
        number2 = 1
        number1 += 1
'''
'''2	4	6	8	10	12	14	16	18	20	



4	8	12	16	20	24	28	32	36	40	



6	12	18	24	30	36	42	48	54	60	



8	16	24	32	40	48	56	64	72	80	



10	20	30	40	50	60	70	80	90	100	
-'''


# Проверить вышепоказанную программу на четность,
# если первое число четное , то мы выполняем умножение,
# в противном случае принудительно возвращаемся к первому циклу

'''
rabota_kajdiy_den =1# den nedeli - ponedelnik
chasov_na_rabote = 1# nachalo raboti v 8
while rabota_kajdiy_den<=5:#1 - ponedelnik, 5 - patnica
    while chasov_na_rabote<10: #           na ejednevnoy osnove mi 
        print('pyem kofe')
        chasov_na_rabote+=1
    rabota_kajdiy_den+=1
#  sidim na rabote 10 chasov, 1- nachalo rabochego dna, 
#  10 - konec rabochego dna
'''


'''lower_value = int(input("Please, Enter the Lowest Range Value: "))# 1
upper_value = int(input("Please, Enter the Upper Range Value: "))# 32
number_1 = 0
number_2 = 2
print("The Prime Numbers in the range are: ")

while lower_value <= upper_value: # 1 <= 32, 2<=32
    number_1 = lower_value#1,2,3,4,5
    if number_1 > 1:
        while number_2 < number_1:
            if number_1 % number_2 == 0:
                break
            number_2 += 1#3
        else:
            print(number_1)

    number_2 = 2
    lower_value += 1'''



# for переменная in  диапазон/элемент/массив значений :
#    инструкции for/ тело цикла for
# range(start_range, end_range, steps)

for i in range(1,10):
    for j in range(1,10):
        print(i,'*',j,'=',i*j, end='\n')#i = 'A', i = 'm'

