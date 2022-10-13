# Создайте программу для игры в "Крестики-нолики"
tic_tac_toe_game = [['  1  |', '     |','      '], ['     |', '  2  |','      '], ['     |', '     |','  3   ']]
print ()
for i in range(0,3):
    for j in range(0,3):
            print(tic_tac_toe_game[i][j], end='')
    print(sep='/n')
    if i != 2:
        print(17*'-')
print ()

def range_check (a): # проверка диапазона от 1 до 3
    1<=a<=3
        # print('Неверный дипазон. Еще одна попытка!')

address = [] # список для хранения уже введенных "адресов" крестиков и ноликов

# for number_of_moves in range(9):

def address1(): # запрашивает координаты крестика от 1 игрока и выводит в список
    print("Ход ПЕРВОГО игрока! \nВведите номер строки и столбца, куда вы будете ставить КРЕСТИК  ")
    c = str(input("Номер строки от 1 до 3 (первая строка - это самая верхняя строка)  "))
    # while not range_check(int(str_igrok1)):
    #     str_igrok1 = str(input("Номер строки от 1 до 3 (первая строка - это самая верхняя строка)  "))
      

    b = str(input("Номер столбца от 1 до 3 (первый столбец слева)   "))
    # while not range_check(int(column_igrok1)):
    #    column_igrok1 = str(input("Номер столбца от 1 до 3 (первый столбец слева)   "))
    #    range_check(int(column_igrok1))
    return [c, b]

def address2(): # запрашивает координаты нолика от 2 игрока и выводит в список    
    print("Ход ВТОРОГО игрока! \nВведите номер строки и столбца, куда вы будете ставить НОЛИК  ")
    c = str(input("Номер строки от 1 до 3 (первая строка - это самая верхняя строка)  "))
    b = str(input("Номер столбца от 1 до 3 (первый столбец слева)   "))
    return [c, b]




# address.append((int(str_igrok1), int(column_igrok1)))
# print(address)


def cross(x,y): # рисуем новую сетку игры с крестиком по введенным данным от первого игрока
    print()
    for i in range(0,3):
        for j in range(0,3):
                if j == int(y)-1 and i == int(x)-1:
                    tic_tac_toe_game[i][j] = tic_tac_toe_game[i][j][:2] + 'X' + tic_tac_toe_game[i][j][3:]
                print(tic_tac_toe_game[i][j], end='')
        print(sep='/n')
        if i != 2:
            print(17*'-')
    print ()

def zero(x,y): # рисуем новую сетку игры с ноликом по введенным данным от второго  игрока
    print()
    for i in range(0,3):
        for j in range(0,3):
                if j == int(y)-1 and i == int(x)-1:
                    tic_tac_toe_game[i][j] = tic_tac_toe_game[i][j][:2] + 'О' + tic_tac_toe_game[i][j][3:]
                print(tic_tac_toe_game[i][j], end='')
        print(sep='/n')
        if i != 2:
            print(17*'-')
    print ()

win = [('11', '12', '13'), ('21', '22', '23'), ('31', '32', '33'), ('11', '21', '31'), ('12', '22', '32'), ('13', '23', '33'), ('11', '22', '33'), ('13', '22', '13')]
# print(win(0))
wincross = []
zerocross = []
count = 1

while count < 9:
    count_break = 0
    f1 = []
    f2 = []
    f1 = address1() #список из координат, которые ввел первый игрок
    str_igrok1 = f1[0]
    column_igrok1 = f1[1]

    if (int(str_igrok1), int(column_igrok1)) in address:
        print()
        print('введите новые значения, это место уже занято')
        print()
        f1 = address1() #список из координат, которые ввел первый игрок
        str_igrok1 = f1[0]
        column_igrok1 = f1[1]

    
    cross(str_igrok1, column_igrok1) # вызвали функцию после хода первого игрока, вывели игровое поле на экран
    wincross.append(int((str_igrok1) + (column_igrok1)))
    print(wincross)

    for i in range(0, len(win)): # проверяем победу крестиков
        if int(win[i][1]) in wincross and int(win[i][0]) in wincross and int(win[i][2]) in wincross:
            print ('крестики победили!!!')
            count_break += 1
    if count_break == 1 or count == 9:
        break
        
    address.append((int(str_igrok1), int(column_igrok1))) # добавили в список введенный адрес (строка, колонка)
    count +=1

    f2 = address2() #список из координат, которые ввел первый игрок
    str_igrok2 = f2[0]
    column_igrok2 = f2[1]

    if (int(str_igrok2), int(column_igrok2)) in address:
        print()
        print('введите новые значения, это место уже занято')
        print()
        f2 = address2() #список из координат, которые ввел первый игрок
        str_igrok2 = f2[0]
        column_igrok2 = f2[1]

    zero(str_igrok2, column_igrok2) # вызвали функцию после хода второго игрока, вывели игровое поле на экран
    
    zerocross.append(int((str_igrok2) + (column_igrok2)))
    for i in range(0, len(win)): # проверяем победу ноликов
        # print(int(win[i][1]))
        # print(int(win[i][0]))
        # print(int(win[i][2]))
        if int(win[i][1]) in zerocross and int(win[i][0]) in zerocross and int(win[i][2]) in zerocross:
            print ('Нолики, вы супер! Победа за вами!!!')
            count_break += 1
    if count_break == 1:
        break
    
    address.append((int(str_igrok2), int(column_igrok2))) # добавили в список введенный адрес (строка, колонка)
    count +=1


