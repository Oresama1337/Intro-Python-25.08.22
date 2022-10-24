# data.json - файл с данными о некоторых математиках прошлого.
# 1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.
# 2. Написать "функцию сортировки" данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
# Если фамилии нет, то использовать имя, например Euclid.
# 3. Написать функцию сортировки по количеству слов в поле "text".
# 4. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.
#
#
# Кроме функций сортировки также надо написать их использование.
import json, re

filename = "data_13.json"
with open(filename, "r") as json_file:
    info = json.load(json_file)


def name_split(sp):
    return sp["name"].split()[-1]


sorted_names = sorted(info, key=name_split)


def text_split(tx):
    text = tx["text"].split()
    template = r"[A-Za-z]+"
    world = re.findall(template, text)

    return world.count(text)


sorted_text = sorted(info, key=text_split)
print(text_split(info))


def death_date(dd):
    date = dd["years"]
    template = r"\d+"
    dates = re.findall(template, date)
    result = int(dates[1])
    if date.split()[-1] == "BC.":
        result = -int(dates[1])
    return result


sorted_death = sorted(info, key=death_date)
