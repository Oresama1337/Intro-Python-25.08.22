# Для задания 1-7 за основу можете взять код из предідущих ДЗ.
#
# 1. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
#
def turning_string_list(my_list):
    new_list = []
    for index, item in enumerate(my_list):
        if index % 2 != 0:
            new_list.append(item[::-1])
        else:
            new_list.append(item)
    return new_list


my_list = ["321", "123", "qwe", "asd", "qwe", "asd", "qwe", "asd"]
new_list = turning_string_list(my_list)
print(new_list, "\t" "№1")


#
# 2. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list у которых первый символ - буква "a".
#
def first_element_a(my_list):
    new_list = [sym for sym in my_list if sym[0] == "a"]
    return new_list


my_list = ["asd", "weq", "123", "azx", "qwa", "abca"]
new_list = first_element_a(my_list)
print(new_list, "\t" "№2")


#
# 3. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list в которых есть символ - буква "a" на любом месте.
#
def element_a(my_list):
    new_list = [word for word in my_list if "a" in word]
    return new_list


my_list = ["qwe", "qaz", "asd", "cba", "zasa", "ababa", "zxc"]
new_list = element_a(my_list)
print(new_list, "\t" "№3")


#
# 4. Написать функцию которой передается один параметр - список строк my_list в
# котором могут быть как строки (type str) так и целые числа (type int).
# Функция возвращает новый список в котором содержаться только строки из my_list.
#
def list_of_strings(my_list):
    new_list = [sym for sym in my_list if type(sym) == str]
    return new_list


my_list = [1, 2, 3, "11", "22", "33", 4, 5, 6, "Hello"]
new_list = list_of_strings(my_list)
print(new_list, "\t" "№4")


#
# 5. Написать функцию которой передается один параметр - строка my_str.
# Функция возвращает новый список в котором содержаться те символы из my_str,
# которые встречаются в строке только один раз.
#
def unic_symbols(my_str):
    my_set = set(my_str)
    my_list = []
    for sym in my_set:
        if my_str.count(sym) == 1:
            my_list.append(sym)
    return my_list


my_str = "aabbccddeeQWERTY"
my_list = unic_symbols(my_str)
print(my_list, "\t" "№5")


#
# 6. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
#
def same_symbols(my_str, my_str_2):
    set_1 = set(my_str)
    set_2 = set(my_str_2)
    ones = set_1 | set_2
    return list(ones)


my_str = "aaaaaab"
my_str_2 = "cddd"
ones = same_symbols(my_str, my_str_2)
print(ones, "\t" "№6")


#
# 7. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.
#
def unic_ones(str_1, str_2):
    set_1 = set(str_1)
    set_2 = set(str_2)
    my_list = []
    for sym in (set_1 & set_2):
        if (str_1.count(sym) == 1) & (str_2.count(sym) == 1):
            my_list.append(sym)
    return my_list


str_1 = "aaasdfw1"
str_2 = "asdfffw1"
my_list = unic_ones(str_1, str_2)
print(my_list, "\t" "№7")
#
# 8. Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
#
# Пример использования функции:
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
# e_mail = create_email(domains, names)
# print(e_mail)
# >>>miller.249@sgdyyur.com


import random
import string

names = ["nika", "sonja", "alex", "roma", "elly", "vlad", "andrey"]
domains = [".ru", ".com", ".net", ".ua", ".fi"]


def create_email(names, domains):
    name_gen = random.choice(names)
    dom_gen = random.choice(domains)
    numbers = str(random.randint(100, 999))
    random_letters = "".join(random.choice(string.ascii_lowercase) for letter in range(random.randint(5, 7 + 1)))

    email = (f"{name_gen}.{numbers}@{random_letters}{dom_gen}")
    return email


email = create_email(names, domains)
print(email)

# print(f"{name_gen}."
#       f"{numbers}@"
#       f"{random_letters}"
#       f"{dom_gen}")
