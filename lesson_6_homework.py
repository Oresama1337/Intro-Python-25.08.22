# 1

my_list = [1, 3, 5, 7, 9, 10, 20, 40, 60, 80, 101, 200, 300, 400, 500, 1000]
for i in my_list:
    if i > 100:
        print(i)
# 2

my_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 101, 300, 500]
my_result = []

for index in my_list1:
    if index > 100:
        my_result.append(index)
print(my_result)

# 3

my_list2 = [3, 5, 6, 10]
if len(my_list2) < 2:
    new_list = my_list2.append(0)
else:
    my_list2.append(my_list2[len(my_list2) - 1] + my_list2[len(my_list2) - 2])
print(my_list2)
