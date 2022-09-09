my_str = "I'm a man. My name is Volodymyr"

count = 0
for symbol in my_str:
    if symbol.isupper():
        count += 1
        print(symbol)
print(count)

count = 0
for symbol in my_str:
    if symbol.islower():
        count += 1
        print(symbol)
print(count)

count = 0
for symbol in my_str:
    if symbol in "eyuioa":
        count += 1
        print(symbol)
print(count)

count = 0
for symbol in my_str:
    if symbol.isalpha() and symbol.lower() not in "eyuioa":
        #    if symbol == " ":
        count += 1
    print(symbol)
print(count)
count = my_str.count(' ') + my_str.count('a')
count_space = my_str.count(' ')
count_a = my_str.count('a')
print(count)

my_str = " \t   qwerty\n\n"
# my_str = "aesdeeeeee"

my_str = my_str.strip('ed')
print(my_str)
print("---------")

print(id(my_str))
my_str = my_str.upper()
# new_str = my_str.lower()
print(my_str)
print(id(my_str))

my_str = my_str.capitalize()
print(my_str)

first_name_1 = "Vova"
first_name_2 = "VOvA"
print(first_name_1.upper() == first_name_2.upper())

new_str = my_str.replace("man", "woman", 1)
print(new_str)

my_str = "qwerty"

# for symbol in my_str:
# for symbol in my_str[:3]:
# for symbol in "qwerty"[::2]:   #not good
# 1
for symbol in my_str:
    new_symbol = symbol * 2
    print(new_symbol)

for symbol in my_str[::2]:
    new_symbol = symbol * 2
    print(new_symbol)
# 2
for index in range(len(my_str)):
    if index % 2 == 0 or index % 3 == 0:  # math ))
        if not index % 2 or not index % 3:
            print(index, my_str[index])

    index = 12
    print(index % 2 == 0, not index % 2)

    for item in enumerate(my_str):
        print(item)
    # 3
    for index, symbol in enumerate(my_str):
        print(index, symbol)

    count = 0
    for symbol in my_str:
        if symbol.isalpha() and symbol.lower() not in "eyuioa":
            count += 1
    print(symbol)
    print(count)
