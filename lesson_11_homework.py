# Функция generate_txt_data. Создает данные для записи в файл txt.
# Функция генерирует и возвращает строку случайной длинны (не менее 100 но не более 1000 символов).
# В строке должны присутствовать большие и маленькие буквы английского алфавита, цифры, пробелы.
#
# Функция generate_json_data. Создает данные для записи в файл json.
# Создает и возвращает словарь со случайным количеством ключей (не менее 5 но не более 20 ключей).
# Ключи - уникальные случайные строки длинны 5 символов из маленьких букв английского алфавита
# (можно с повторениями символов).
# Значения - или целое число в диапазоне от -100 до 100, или число типа float в диапазоне от 0 до 1,
# или True/False. Выбор значения должен быть равновероятным. Т.е. вероятность того, что значение будет целым
# такая же, как и вероятность того, что будет типа float или типа bool.
#
# Функция generate_and_write_file. Написать функцию которая принимает один параметр - полный путь к файлу.
# В зависимости от расширения файла (txt, json) сгенерировать данные для записи и записать в данный файл.
# Если расширение не соответствует заданным, то вывести текст "Unsupported file format"
#
# Разрешается создавать дополнительные (вспомогательные) функции.

import random, os, json, string

file_txt = "generate_data.txt"


def generate_txt_data(file_txt):
    gen_txt = string.ascii_letters + string.whitespace + string.digits
    rand_string = "".join(random.choice(gen_txt) for sym in range(random.randint(100, 1000)))

    with open(file_txt, "w") as file:
        file.write(rand_string)
    return rand_string


# print(generate_txt_data(file_txt))

filename = "generate_data.json"


def random_keys():
    keys_gen = "".join(random.choice(string.ascii_lowercase) for sym in range(5))
    return keys_gen


def random_value():
    int_value = random.randint(-100, 100)
    float_value = random.uniform(0, 1)
    bool_value = random.choice([True, False])
    random_gen = random.choice([int_value, float_value, bool_value])
    return random_gen


def generate_json_data(filename):
    random_dict = {random_keys(): random_value() for _ in range(random.randint(5, 20))}

    json_file = json.dumps(random_dict, indent=4)

    with open("generate_data.json", "w") as outfile:
        outfile.write(json_file)

    return random_dict


#print(generate_json_data(filename))

file_path = os.path.abspath("\PycharmProjects\Intro-Python-25.08.22\generate_data.json")

def generate_and_write_file(file_path):

    check_json = generate_json_data(filename)
    check_txt = generate_txt_data(file_txt)
    if os.path.splitext("generate_data.json") == ".json":
        with open("generate_data.json", "w") as outfile:
            json.dump(check_json, outfile, indent=4)
        return check_json
    elif os.path.splitext("generate_data.txt") == ".txt":
        with open("generate_data.txt", "w") as file:
            file.write(check_txt)
        return check_txt

    return str("Unsupported file format")

print(generate_and_write_file(file_path))
