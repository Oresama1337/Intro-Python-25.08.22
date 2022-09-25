# 1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate или range.
#
my_list = ["321", "123", "qwe", "asd", "qwe", "asd", "qwe", "asd"]
new_list = []
for index, item in enumerate(my_list):
    if index % 2 != 0:
        new_list.append(item[::-1])
    else:
        new_list.append(item)
print(new_list, "\t" "№1")
#
# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".
#
my_list = ["asd", "weq", "123", "azx", "qwa", "abca"]
new_list = [sym for sym in my_list if sym[0] == "a"]
print(new_list, "\t" "№2")
#
# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.
#
my_list = ["qwe", "qaz", "asd", "cba", "zasa", "ababa", "zxc"]
new_list = [word for word in my_list if "a" in word]
print(new_list, "\t" "№3")
#
# 4) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
#
persons = [{"name": "John", "age": 15},
           {"name": "Jack", "age": 45},
           {"name": "Sam", "age": 10},
           {"name": "Sall", "age": 10},
           {"name": "Jakubovich", "age": 45},
           {"name": "Jackob", "age": 15},
           {"name": "Emanuellll", "age": 40}]
min_age = float("inf")
max_len = float("-inf")
sum_age = 0
for person in persons:
    if person["age"] < min_age:
        min_age = person["age"]
    if len(person["name"]) > max_len:
        max_len = len(person["name"])
    sum_age += person.get("age")
# а) Создать список и поместить туда имя самого молодого человека. Если возраст совпадает - поместить все имена самых молодых.
names_min_age = [person["name"] for person in persons if person["age"] == min_age]
# б) Создать список и поместить туда самое длинное имя. Если длина имени совпадает - поместить все такие имена.
names_max_len = [person["name"] for person in persons if len(person["name"]) == max_len]
# в) Посчитать среднее количество лет всех людей из начального списка.
print(names_min_age, "№4A""\n", names_max_len, "№4Б" "\n", (sum_age / len(persons)), "№4В")
#
# 5) Даны два словаря my_dict_1 и my_dict_2.
#
my_dict_1 = {"name": "John", "age": 30}
my_dict_2 = {"name": "John", "job": "programmer"}
# key_list_inter = list((key, my_dict_1[key]) for key in my_dict_1 if key in my_dict_2)
# print(key_list_inter, type(key_list_inter))
# key_list_differ = list((key, my_dict_1[key]) for key in my_dict_1 if key not in my_dict_2)
# print(key_list_differ, type(key_list_differ))
#
# а) Создать список из ключей, которые есть в обоих словарях.
keys_inter = list(my_dict_1.keys() & my_dict_2.keys())
print(keys_inter, "\t" "№5A")
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
keys_diff = list(my_dict_1.keys() - my_dict_2.keys())
print(keys_diff, "\t" "№5Б")
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
my_dict_3 = {key: my_dict_1[key] for key in set(my_dict_1) - set(my_dict_2)}
print(my_dict_3, "\t" "№5В")
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
# my_dict_4 = {}
# for key in my_dict_1.keys() | my_dict_2.keys():
#     if key in my_dict_1:
#         if key in my_dict_2:
#             my_dict_4[key] = [my_dict_1[key], my_dict_2[key]]
#         else:
#             my_dict_4[key] = my_dict_1[key]
#     else:
#         my_dict_4[key] = my_dict_2[key]


my_dict_4 = {}
d_keys = my_dict_1.keys() & my_dict_2
my_dict_4 = my_dict_1.copy()
my_dict_4.update(my_dict_2)
my_dict_4.update({key: [my_dict_1[key], my_dict_2[key]] for key in d_keys})


print(my_dict_4, "\t" "№5Г")