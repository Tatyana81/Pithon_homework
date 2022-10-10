# 5.Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
with open('polynomial_1.txt', 'r') as data:
    polynomial_1 = str(data.readlines()) #если считываю без str, то тип получается list
with open('polynomial_2.txt', 'r') as data:
    polynomial_2 = str(data.readlines())
    
print(polynomial_1)
print(type(polynomial_1))
print(polynomial_2)
print(type(polynomial_2))
#        5x^3 +  3x^2 - 1x + 10 = 0
# x^10        +  8x^2 + 5x - 20 = 0
# x^10 + 5x^3 + 11x^2 + 4x - 10 = 0
polynomial_1 = polynomial_1 + '+' + polynomial_2
print(polynomial_1)
print(type(polynomial_1))
polynomial_1=polynomial_1.replace("'", '') # не пойму как считать строку из файла без элементов [, ], '
polynomial_1=polynomial_1.replace("[", '')
polynomial_1=polynomial_1.replace("]", '')
polynomial_1=polynomial_1.replace("^", '')
print(polynomial_1) # строка, с которой будем работать 5x3+3x2-x+10+x10+8x2+5x-20

# polynomial_1 = '5x3+3x3+2'

my_list = [] # находим наибольшую степень у Х
for i in range(len(polynomial_1)):
    k = ''
    if polynomial_1[i] == 'x':
        if polynomial_1[i+1].isdigit():
            k += polynomial_1[i+1]
            if polynomial_1[i+2].isdigit():
                k += polynomial_1[i+2]
        else:
            k = '1'  
    if k != '':
        my_list.append(k)

max_stepen = max(int(x) for x in my_list) # наибольшая степень у Х

# складываем
itog = ''
for i in range(len(polynomial_1)):
    k = ''
    koff = ''
    sum = 0
    if polynomial_1[i] == 'x':
        if polynomial_1[i+1].isdigit():
            k += polynomial_1[i+1]
            if polynomial_1[i+2].isdigit():
                k += polynomial_1[i+2]

        if polynomial_1[i-1].isdigit():
            koff += polynomial_1[i-1]
            if polynomial_1[i-2].isdigit():
                koff += polynomial_1[i-2] 
    print(k)
    for j in range(1, max_stepen):
        if k != '' and int(k) == j:
            sum = sum + int(koff)
        itog = itog + str(sum) + ' x ^ ' + str(j) + ' + '


print(itog)
    



