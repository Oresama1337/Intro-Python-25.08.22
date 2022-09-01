# bool
# if


# my_value = None
# print(my_value, type(my_value))

##################################

# value_1 = 3
# value_2 = 4
# result = print(value_1 + value_2)
# print(result)

##############################

# my_bool_value = False
# print(my_bool_value, type(my_bool_value))


# my_bool_value = 10 == 2

## <, >, <=, >=, ==, !=

## not
# new_value = not my_bool_value
# print(my_bool_value, new_value)

# val_1 = True
# val_2 = False

# result = val_1 and val_2  # logic AND

# print(result)

#########################################

# val_1 = True
# val_2 = False

# result = val_1 or val_2  # logic OR

# print(result)

########################################

# number = 6
# colour = "red"
# result = ((number == 6) or
#           not (number == 1) and
#           (colour == "red"))
# print(result)

#################################
#
# value = 123
#
# if value > 100:
#     print(f"Value more than 100")
# else:
#     print("Value less or equal than 100")

#if условие
#   блок если да
# elif условие 2
#   блок если да
#----------------------
#else:
#   если нет


# value = 0
#
# if value > 0:
#     print(f"Value is positive number")
# elif value < 0:
#     print(f"Value is negative number")
# else:
#     print("Value is 0")

######################
#Приведение типов
#####################

# value_int = 10
# value_float = float(value_int)
# print(value_float, type(value_float), value_int)
#
# value = 10
# value = float(value)
# print(value)
#
#
# value = -10.3
# value = int(value)
# print(value, type(value))

# value = -10.3
# value = str(value)
# print(value, type(value))

# value = "100_000"
# value = int(value)
# print(value, type(value))


# value = "100.099"
# value = float(value)
# print(value, type(value))


# value = True
# value = float(value)
# print(value, type(value))
###################################

# value = 1         #int в bool всегда тру кроме 0
# value = bool(value)
# print(value, type(value))

# value = 10.4         #float в bool всегда тру кроме 0.0
# value = bool(value)
# print(value, type(value))

# value = None         #none -> always False
# value = bool(value)
# print(value, type(value))


# value = ""         #str в bool всегда тру кроме пустой строки ""
# value = bool(value)
# print(value, type(value))


# str = "qwerty"    #error str set as name
# number = 123
# my_value = str(number)
# print(my_value, type(my_value))

# value = "qwerty"
# if not value:
#     print("Value is none")
# if value:
#     print(f"This value {value} is not 0")

################################
## in

my_str = "bjksnvjkuhksjnvuehwoijlzxc"
sub_str = "zxc"

if sub_str in my_str:
    print("!!!!!!!!!!!!!!!!!!!!!!")