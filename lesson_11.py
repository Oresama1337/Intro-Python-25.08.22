# from lesson_11_tanos import create_directory
#
# print("lesson_11", __name__)
# dirname = "TEST2"
#
# create_directory(dirname)

import json

# values_str = "[1,2,3]"
# values_str = '{"key": "values"}'
# values = json.loads(values_str)
# print(values['key'], values)
############################################
# address_1 = {'city': 'Dnipro',
#              'street': 'Polya',
#              'building': 123}
# data = json.dumps(address_1)
# print(data, type(data))

def read_json(filename):
    with open(filename, "r") as json_file:
        #pass
        data = json.load(json_file)
    return data

def write_json(filename,data):
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)

#filename_output = "data.json"
# data = read_json(filename)
#print(data)
data = {"name":"John", "address": {"city": "Dnipro", "street": "Polya", "building": 123}}
filename_output = "out.json"
write_json(filename_output,data)