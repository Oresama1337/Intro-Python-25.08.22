# модули в пайтон
# словари


############################## ВАРИАНТ 1

# import random
#
# value = random.randint(1, 10)
# print(value)
#
# #values = ["qwe", "asd", "zxc"]
# values = "hkjbnsjvhbzhvlhnvjsnvsh"
# value_2 = random.choice(values)
# print(value_2)

############## ВАРИАНТ 2

# from random import randint, choice
#
# value = randint(1, 10)
# print(value)
# value_2 = randint(2, 100)
# print(value_2)
#
# values = "hkjbnsjvhbzhvlhnvjsnvsh"
# value_3 = choice(values)
# print(value_3)

############# ВАРИАНТ 3

# import random as rnd

# import numpy as np
# import pandas as pd
# import tensorflow as tf
# import cv2 as cv

# value = rnd.randint(1, 10)
# print(value)
# value_2 = rnd.randint(2, 100)
# print(value_2)
#
# values = "hkjbnsjvhbzhvlhnvjsnvsh"
# value_3 = rnd.choice(values)
# print(value_3)

# value = {"key": "value"}
# print(value, type(value))


# ключ - уникальное значение, остается последнее значение
# ключем может быть : int, float, str, bool- лучше не использовать, любой не изменяемый объект(tuple)
# ключем НЕ может быть : любой изменяемый объект(list, set)
# значением может быть любой объект

# my_dict = {10: 11,
#            2: 22,
#            3: 33,
#            "4": 44,
#            "5": 55,
#            6.5: 123,
#            False: True,
#            True: False,
#            (1, 2): "tuple",
#            []: "qwe",
#            }
# print(my_dict)

# address_1 = {"city": "Dnipro",
#              "street": "Polya",
#              "building": 123}
# person_1 = {"name": "John",
#             "age": 23,
#             "jobs": ["programmer", "teacher"],
#             "address": address_1}
# #print(person_1["name"], person_1["job"])
#
# address_2 = {"city": "New York",
#              "street": "Polya",
#              "building": 321}
# person_2 = {"name": "Jackob",
#             "age": 32,
#             "jobs": ["programmer"],
#             "address": address_2}
# #print(person_2["name"], person_2["job"])
#
# persons = [person_1, person_2]
#
# for person in persons:
#     print(person["address"]["city"])
#     print(person["jobs"])

address = {"city": "Dnipro",
           "street": "Polya",
           "building": 123}
# address["city"] = None
address["city"] = "London"
# address["city"] = ""
address["zip"] = 49000
address["zip"] = "49000"

address_2 = address.copy()
address_2["city"] = "QQQ"

print(address, address_2)

city = address["city"]
city = "AAA"
print(city, address)

# city = address.get("city")
# print(city, address)
# key = "zip"
# zip_value = address.pop("zip")
# print(address)
#
# if key in address:    # проверка только в ключах!!!
#     address.pop(key)
#     print(address[key])
#
# for _ in address:   # цикл только по ключам!!!
#     print(_)
#
# for key in address:   # цикл только по ключам!!!
#     print(key, address[key])

for some_object in address.keys():  # цикл только по ключам!!!
    print(some_object)

for key, value in address.items():  # цикл только по ключам!!!
    print(key, value)

# keys = list(address.keys())
# print(keys)

values = list(address.values())
print(values)

address_addition = {"zip": "49000",
                    "apartament": 12}
address_info = {"info": "Test"}
address.update(address_addition)
address.update(address_info)
print(address)

new_address = {**address, **address_addition, **address_info}
print(new_address)