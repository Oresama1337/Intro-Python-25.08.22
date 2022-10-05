# 1. Дано целое число (int). Определить сколько нулей в этом числе.
#
number = 1234509876102030405060708090
count_zeroes = str(number).count('0')
print(count_zeroes)
#
# 2. Дано целое число (int). Определить сколько нулей в конце этого числа. Например для числа 1002000 - три нуля
#
number_1 = 1002000
str_number = str(number_1)
print(len(str_number) - len(str_number.rstrip('0')))
#
# 3. Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.
#
my_list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
my_result = []
for number in my_list_1[::2]:
    my_result.append(number)
for number in my_list_2[1::2]:
    my_result.append(number)
print(my_result)
#
# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]
#
my_list = [1, 2, 3, 4]
new_list = my_list.copy()
new_list.append(new_list.pop(0))
print(my_list, new_list)
#
# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)
#
my_list = [1, 2, 3, 4]
my_list.append(my_list.pop(0))
print(my_list)
#
# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133. (используйте split и проверку isdigit)
#
my_str = "43 больше чем 34 но меньше чем 56"
value = my_str.split(" ")
my_sum = []
for numbers in value:
    if numbers.isdigit():
        my_sum.append(int(numbers))
print(sum(my_sum))
#
# 7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin". (rfind, find - методы строк)
#
my_str = "asdfghjkl W poiuytreq W asdfghjkl"
l_limit = "l"
r_limit = "a"

sub_str = my_str[my_str.find(l_limit):my_str.rfind(r_limit) + 1]
print(sub_str)
#
# 8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
# (используйте срезы длинны 2)
#
my_str = "abcdefghw"
my_list = []
for symbol in range(0, len(my_str), 2):
    sym = my_str[symbol:symbol + 2]
    if len(sym) == 1:
        my_list.append(sym + "_")
    else:
        my_list.append(sym)
print(my_list)
#
# 9. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.
#
my_numbers = [2, 4, 1, 5, 3, 9, 0, 7]
big_numbers = 0
for num in range(1, len(my_numbers) - 1):
    if (my_numbers[num - 1]) < (my_numbers[num]) and (my_numbers[num]) > (my_numbers[num + 1]):
        big_numbers += 1
print(big_numbers)
#
# 10. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
# Например [1, 2, 3, "11", "22", 33]
# Создать новый список в который поместить только строки из my_list.
#
my_list = [1, 2, 3, "11", "22", "33", 4, 5, 6, "Hello"]
new_list = [sym for sym in my_list if type(sym) == str]
print(new_list)
#
# 11. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке ТОЛЬКО ОДИН раз. for symbol in set(my_str)
#
my_str = "aabbccddeeQWERTY"
my_set = set(my_str)
my_list = []
for sym in my_set:
    if my_str.count(sym) == 1:
        my_list.append(sym)
print(my_list)
#
# 12. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
#
my_str = "aaaaaab"
my_str_2 = "cddd"
set_1 = set(my_str)
set_2 = set(my_str_2)
ones = set_1 | set_2
print(ones)
#
# 13. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой ТОЛЬКО ПО ОДНОМУ разу.
# Пример: для строк "aaaasdf1" и "asdfff2" ответ ["s", "d"], т.к. эти символы есть в каждой строке по одному разу

str_1 = "aaasdfw"
str_2 = "asdfffw"
set_1 = set(str_1)
set_2 = set(str_2)
my_list = []
for sym in (set_1 & set_2):
    if (str_1.count(sym) == 1) & (str_2.count(sym) == 1):
        my_list.append(sym)
print(my_list)

# str_1 = "aaasdfw"
# str_2 = "asdfffw"
# common_elements = list(set(str_1) & (str_2))
# unique_common_elements = []
# for