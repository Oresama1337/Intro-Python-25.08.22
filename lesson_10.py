# module os
# work with files

import os

#
# path = "."
# files = os.listdir(path)  # sorted(os.listdir(path))
# print(files)
#
# filemane = "lesson_9.txt"
#
# #1 - можно, но осторожно
# file = open(filemane, "r")
# data = file.read()
# print(data)
# file.close() #!!!!
#
# #2 - much better
#
# with open(filemane, "r") as file:
#     data = file.read()
# print(data)
# filename_out = "test.txt"
# text = "qwerty\nTEST"
# with open(filename_out, "w") as file_txt:
#     file_txt.write(text)
###########################################
# filename = "test.txt"
# with open(filename,"r") as file:
#     # data = [line.strip() for line in file.readlines()]
#     data = file.readlines()
# print(data)
#
# filename_out = "test.txt"
# data.append("\nTEST")
# with open(filename_out, "w") as file_txt:
#     file_txt.writelines(data)
#     file_txt.writelines([f"{line}\n" for line in data])
################################################
# filename = "test.txt"
# with open(filename, "r") as file:
#     data = file.read().splitlines()
# print(data)
#
# filename_out = "test.txt"
# data.append("\nTEST")
# with open(filename_out, "w") as file_txt:
#     file_txt.writelines("\n".join(data))
#
#
# def read_file(filename):
#     with open(filename, "r") as file:
#         data = file.read().splitlines()
#     return data
#
#
# data = read_file(filename)
# print(data)

###################################################
# Past homeworks

# 1. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.

my_list = ["asd", "zxc", "a_test", "123"]

# 1
new_list = []
for index, str_ in enumerate(my_list):
    if index % 2:
        new_list.append(str_[::-1])
    else:
        new_list.append(str_)
# print(new_list)
# 2
new_list = my_list.copy()
for index, str_ in enumerate(my_list):
    if index % 2:
        my_list[index] = str_[::-1]
# print(new_list)

# 2. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list у которых первый символ - буква "a"
