# 1

my_list = [1, 3, 5, 7, 9, 10, 20, 40, 60, 80, 101, 200, 300, 400, 500, 1000]
for numbers in my_list:
    if numbers > 100:
        print(numbers)
# 2

my_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 101, 300, 500]
my_result = []

for large_numbers in my_list1:
    if large_numbers > 100:
        my_result.append(large_numbers)
print(my_result)

# 3

my_list2 = [3, 2, 10, 5]
if len(my_list2) < 2:
    my_list2.append(0)
else:
    my_list2.append((my_list2[-1]) + my_list2[-2])
print(my_list2)
