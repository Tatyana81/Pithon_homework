# # Реализовать алгоритм перемешивания списка.
import random
def mix(my_lst):
    copy_my_lst=my_lst #создаем копию списка
    for i in range(len(copy_my_lst)):
        #получение случайного индекса
        index_mix=random.randint(0, len(copy_my_lst) - 1)
        # Замена
        temp = copy_my_lst[i]
        copy_my_lst[i] = copy_my_lst[index_mix]
        copy_my_lst[index_mix] = temp
    return copy_my_lst
list = [1,2,3,4,5,6,7,8,9]
print("Исходный список: ")
print(list)
mixed_list = mix(list)
print("Перемешанный список: ")
print(mixed_list)


# import random
# def mix_list(list_original):
#     # Создаем копию, поскольку мы не должны изменять оригинал
#     list = list_original[:]
#     # Цикл от 0 до длины списка -1
#     list_length = len(list)
#     for i in range(list_length):
#         # Получение случайного индекса
#         index_aleatory = random.randint(0, list_length - 1)
#         # Замена
#         temp = list[i]
#         list[i] = list[index_aleatory]
#         list[index_aleatory] = temp
#     # Возвращаем список
#     return list
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# mixed_list = mix_list(list)
# print("Исходный список: ")
# print(list)
# print("Перемешанный список: ")
# print(mixed_list)