# 1
# value = 100
# new_value = value / 2 if value < 100 else value * (-1)
# print(new_value)
#############################
# 2
#############################

# value = 10
# new_value = 1 if value < 100 else 0
# print(new_value)
##############################
# 3
#############################

# value = 10
# new_value = True if value < 100 else False
# print(new_value)
##############################
# 4
###############################

# my_str = "qwer"
# if len(my_str) < 5:
#     new_str = my_str + my_str
# else:
#     new_str = my_str
# print(new_str)
################################
# 5
###############################

my_str = "qwerty"
if len(my_str) < 5:
    new_str = my_str + my_str[::-1]
else:
    new_str = my_str
print(new_str)
