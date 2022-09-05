# # функция input
# # обработка ошибок
# # тернарный оператор
# # цикл с условием
# # методы строк
#
# value = input("Enter a full number: ")
# try:
#     value = int(value)
#     result = 1 / value
#     print(value, result)
#
# except ValueError:
#     print("It is not a full number!!!")
#
# except ZeroDivisionError:
#     print("Can not devide on zero!!!")


############################ тернарный оператор

# value = -12
# ###########
# if value >= 0:
#     result = value
# else:
#     result = value * 2
# print(result)
# ##########
# # new_line = positive if result else negative
# result = value if value >= 0 else value * 2
# print(result)

######################цикл с условием

value = 10
# while value >= 0:
#     print(value)
#     value -=1

## not very good

# while True:
#     print(value)
#     value -=1
#     if value < 0:
#         break
#
# situative
#
# do_while = True
# while do_while:
#     print(value)
#     value -= 1
#     if value < 0:
#         do_while = False


################### методы строк


my_str = "qwerty"
# index = 0
index = -1  #отсчет от конца строки

symbol = my_str[index]  # получение значения по индексу
print(symbol)

# if index < len(my_str):
#     symbol = my_str[index]  # получение значения по индексу
#     print(symbol)

# symbol_count = len(my_str)
# print(symbol_count)
