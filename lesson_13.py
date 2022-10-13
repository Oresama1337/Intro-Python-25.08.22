# values = [2, -3, 6, 100, 45]
# sorted_values = values.copy()
# sorted_values.sort(reverse=True)

# values.sort(reverse=True)   #change object
# sorted_values = sorted(values, reverse=True)
# print(values, sorted_values)
#########################################
# values = ["qwe123", "1asd", "z", "!ZX"]
# sorted_values = sorted(values, key=len, reverse=True)
# print(sorted_values)

############################################
# values = [2, -30, 6, 100, 45]
# sorted_values = sorted(values, key=abs)
# print(sorted_values)
###########################################
import re
import json

filename = "data.json"
with open(filename, "r") as json_file:
    values = json.load(json_file)
    # print(values)

    # def sort_by_age(item):
    #     age = item["age"]
    #     return age
    #
    #
    # sorted_values = sorted(values, key=sort_by_age)
    # print(sorted_values)
    #
    #
    # ############################################
    # def sort_by_name(item):
    #     name = item["name"]
    #     return len(name), name
    #
    #
    # sorted_values = sorted(values, key=sort_by_name)
    # print(sorted_values)
    # ###########################################
    # values = [(2, -30), (6, 100), (45, 200), (30, -6)]
    # sorted_values = sorted(values)
    # print(sorted_values)
    #################################################
    # def sort_by_age(item):
    #   return item["age"]


    # sorted_values = sorted(values, key=lambda item: item["age"])
    # print(sorted_values)

    # sorted_values = sorted(values, key=lambda item: (len(item["name"]), item["name"]))
    # print(sorted_values)
    ##########################################################


# def sort_by_zip_number(item):
#     zip_code = item["zip"]
#     template = r"[0-9]+"
#     result = re.findall(template, zip_code)
#     if result:
#         result = result[0]
#     else:
#         result = ""
#     return result

def sort_by_zip_number(item):
    zip_code = item["zip"]
    template = r"[0-9]+"
    zip_val = re.findall(template, zip_code)
    result = ""
    if zip_val:
        result = zip_val[0]
    return result

sorted_values = sorted(values, key=sort_by_zip_number)
print(sorted_values)

#zip_code = "29000PDI1"
#template = r"[0-9]{2}"
#template = r"[0-9]+"
#template = r"[1-9]+"
#template = r"[A-Za-z]+"
#template = r"\d+"
#template = r"\w+"
#result = re.findall(template,zip_code)
#print(result)