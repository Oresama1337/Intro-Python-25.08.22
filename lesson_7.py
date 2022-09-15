# my_str = "blablacar"
# my_symbol = "bla"
# number = my_str.count(my_symbol)
# print(number)
#
# for count in range(number):
#     print(my_symbol)
#
# for _ in range(number):
#   print(my_symbol)

# my_str = "bla BLA car"
# result = len(set(my_str.lower()))
# print(result)
##### =
# unique_symbols = []
#
# for symbol in my_str.lower():
#     if symbol not in unique_symbols:
#         unique_symbols.append(symbol)
# print(len(unique_symbols), unique_symbols)


# unique_symbols = ""
#
# for symbol in my_str.lower():
#     if symbol not in unique_symbols:
#         unique_symbols += symbol
# print(len(unique_symbols), unique_symbols)

# my_str = "zhjdsgfz,jhvzxnkzxnj"
# my_list = []

# for symbol in my_str[::2]:
#     my_list.append(symbol)
# print(id(my_list))

# my_list += list(my_str[::2])
# print(id(my_list))


my_str = "qwertyuiop"
str_indexes = [0, 9, 9, 1, 5]
my_list = []
#
# for index in str_indexes:
#     value = my_str[index]
#     my_list.append(value)
# print(my_list)


my_number = 1234567000765432199900012
# print(len(str(my_number)))
#
#
# number_str = str(my_number)
# max_digit = max(number_str)   #ASCII
# print(max_digit)

# print(ord("a"), chr(98))
# for index in range(150, 200):
#     print(index, chr(index))


# str_number = str(my_number)
# reversed_number = str_number[::-1]
# new_number = int(reversed_number)
### =
# new_number = int(str(my_number)[::-1])

# print(new_number, type(new_number))

##### sorting

values = [12, 2, 34, -6, 100]
# new_values = values.copy()
# values.sort()             #doesn't save previous list
# print(values, new_values)

# new_values = sorted(values)
# print(values, new_values)

# str_number = str(my_number)
# sorted_number = sorted(str_number)
# sorted_number = "".join(sorted_number)
#### =
# number = int("".join(sorted(str(my_number))))

# print(number)

# my_list_1 = [1, 2, 3, 4, 5, 6, 7]
# my_list_2 = [10, 20, 30, 40]
# my_result = []
#
# index_count = min(len(my_list_1), len(my_list_2))
#
# # for index in range(len(my_list_1)):
# for index in range(index_count):
#     my_result.append(my_list_1[index])
#     my_result.append(my_list_2[index])
#
# my_result = my_result + my_list_1[index_count:] + my_list_2[index_count:]
#
# print(my_result)

# numbers = [number for number in range(10)]

# for number in range(10):
#    numbers.append(number)
# print(numbers)
#
# squares = [number ** 2 for number in range(11, 21)]
# print(squares)
#
# values = [123, 23, -4, 78, -94, -1, 0]
# positive_numbers = [val for val in values if val > 0 or val < -10]
# print(positive_numbers)


# множество

# values = [1, 2, "3", "2", 3, 3, 1]
# my_set = set(values)
# new_values = list(set(values))
# print(new_values)

# my_set = {1, 2, 3, "ASD"}
# my_set = set()

set_1 = {1, 2, 3, 4}
set_2 = {1, 20, 3, 40}
set_3 = {1, 20, 30, 50}

my_set = set_1 | set_2 | set_3
print(my_set)

# my_set = set_1.union(set_2)
# print(my_set)

# my_set = set_1.intersection(set_2)
# print(my_set)


## разница кто на каком месте
# my_set = set_1.difference(set_2)
# print(my_set)

my_str = "qweeeeeeeeeeeeeeeeeeee"

for symbol in set(my_str):
    print(symbol)