# функция input
# обработка ошибок
# тернарный оператор
# цикл с условием
# методы строк

value = input("Enter a number: ")
try:
    value = int(value)
except:
    print("It is not a number!!!")
    value = 0

result = value * 2
print(value, result)
