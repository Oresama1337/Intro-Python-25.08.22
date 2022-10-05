# Все пункты сделать как отдельные функции и их вызовы.
#
import os

# 1. Написать функцию, которая получает в виде параметра имя файла названия интернет доменов (domains.txt)
# и возвращает их в виде списка строк (названия возвращать без точки).
#
domains = "domains.txt"


def read_file(domains):
    # data = []
    with open(domains, "r") as file:
        # for line in file.readlines():
        #    data.append(line.strip()[1:])
        data = list(line.strip()[1:] for line in file.readlines())

    return data


#print(read_file(domains))
#
# 2. Написать функцию, которая получает в виде параметра имя файла (names.txt)
# и возвращает список всех фамилий из него.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Разделитель - символ табуляции "\t"
#
names = "names.txt"


def list_of_names(names):
    last_names = []


    with open(names, "r") as file:
        for line in file.readlines():
            last_names.append(line.split("\t")[1])
    # last_names = list(line.split("\t")[1] for line in file.readlines())
    return last_names

print(list_of_names(names))
#
# 3. Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
# словарей вида {"date": date}
# в которых date - это дата из строки (если есть),
# Например [{"date": "1st January 1919"}, {"date": "8th February 1828"},  ...]
#

authors = "authors.txt"


def get_dates(authors):
    result = []
    with open("authors.txt", "r") as file:
        for line in file.readlines():
            if " - " in line:
                date = line.split(" - ")[0]
                result.append({"date": date})
    return result


#print(get_dates("authors.txt"))

#
# По просьбам некоторых студентов начну включать дополнительные задания.
# 4* (*сдавать не обязательно, но если будете сдавать, то ошибки будут учитываться тоже).
# Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
# словарей вида {"date_original": date_original, "date_modified": date_modified}
# в которых date_original - это дата из строки (если есть),
# а date_modified - это та же дата, представленная в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
# Например [{"date_original": "8th February 1828", "date_modified": 08/02/1828},  ...]
