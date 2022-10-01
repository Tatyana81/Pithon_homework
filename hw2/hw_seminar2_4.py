# Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов
# на указанных позициях. Позиции хранятся в списке positions - создайте этот список (например:
# positions = [1, 3, 6]).

n = int(input("Введите целое число: "))
my_lst = []
for x in range(n*(-1), n+1):
     my_lst.append(x)

positions = []
num_position = int(input("Сколько будет элементов в списке positions ?: "))
for x in range(1, num_position+1):
    num = int(input(f'Введите номер позиции для списка positions от 0 до {n*2}: '))
    positions.append(num)


work=1
for i in positions:
        work*=my_lst[i]

print (f'Исходный список {my_lst}')
print (f'Список позиций {positions}')
print (f'Произведение элементов исходного списка на указанных позициях равно {work}')