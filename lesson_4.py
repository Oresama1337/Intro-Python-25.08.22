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

value = -12
###########
if value >= 0:
    result = value
else:
    result = value * 2
print(result)
##########
# new_line = positive if result else negative
result = value if value >= 0 else value * 2
print(result)