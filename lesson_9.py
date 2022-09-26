import random



# A(1;2;-3)
# point_a = (1,2,-3)
# print(point_a[0])

# def print_hello_world():
#     print("Hello world!")
# print_hello_world()

# def create_point_with_random_values(min_value, max_value):
#     point = {"x": random.randint(min_value, max_value),
#              "y": random.randint(min_value, max_value),
#              "z": random.randint(min_value, max_value)}
#     return point
#
# def create_triangle(name, min_value = -10, max_value = 10, debug_mode = False):
#     triangle = {}
#     for letter in name:
#         triangle[letter] = create_point_with_random_values(min_value,max_value)
#
#     # triangle = {"A": create_point_with_random_values(min_value, max_value),
#     #             "B": create_point_with_random_values(min_value, max_value),
#     #             "C": create_point_with_random_values(min_value, max_value)}
#     if debug_mode:
#         for key in triangle:
#             print(f"{key}: {triangle[key]}")
#     return triangle
#
# min_value = -100
# max_value = 100
#
# min_limit = -50
# max_limit = 50

# DRY

# point_a = create_point_with_random_values(min_value, max_value)
# point_b = create_point_with_random_values(min_value, max_value)
# point_c = create_point_with_random_values(-10, 10)
#
# print(point_a, "\n", point_b, "\n", point_c)

# triangle_1 = create_triangle("QWE", max_value=23, debug_mode=True)
# print(triangle_1)
# triangle_2 = create_triangle(min_limit, max_limit)
# triangle_2 = create_triangle(0, 10)
# triangle_2 = create_triangle(max_value=10, min_value=0)
# triangle_2 = create_triangle(max_value=max_limit, min_value=min_limit)
# triangle_2 = create_triangle(max_value=max_value, min_value=min_value)
# print(triangle_2)

###########################################
# def combine_two_lists(list_1: list, list_2: list) -> list: #рамки возврата значения
#     index_count = min(len(my_list_1), len(my_list_2))
#     #if index_count == 0:
#      #   return []
#     my_result = []
#     for index in range(index_count):
#         my_result.append(my_list_1[index])
#         my_result.append(my_list_2[index])
#     my_result = my_result + my_list_1[index_count:] + my_list_2[index_count:]
#     return my_result
#     #return my_result + my_list_1[index_count:] + my_list_2[index_count:]
#
#
# my_list_1 = [1, 2, 3, 4, 5, 6, 7]
# my_list_2 = [10, 20, 30, 40]
#
# my_result = combine_two_lists(my_list_1, my_list_2)
# print(my_result)
