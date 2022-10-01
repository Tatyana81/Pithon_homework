# Подсчитать сумму цифр в вещественном числе.
str = input("Введите вещественное число: ")
str=str.replace('.', '')
str=str.replace('-', '')
n=0
for i in str:
    n+=int(i)
print (n)