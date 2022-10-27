import random, json
import argparse

start_file = "config.json"

file = "trading_system.json"


def trading_system(start_file, file):
    with open(start_file, "r") as s_file, open(file, "w") as json_file:
        json_file.write(s_file.read())
    return json_file
#trading_system(start_file,file)

with open(file, "r") as json_file:
    data = json.load(json_file)

def current_rate():
    course_get = data["course"]
    return course_get


print("current_rate", current_rate())


def rate_change(current_rate):
    delta = random.uniform(-data["delta"], data["delta"])
    rate = round((current_rate + delta), 2)

    return rate


#rate_change(current_rate())
print("rate_change", rate_change(current_rate()))


def next_roll(item):
    with open(file, "w") as json_file:
        data["course"] = item
        #json_file.write(json.dumps(data))


print("next", next_roll(file))

#
# def available():
#     balance_uah = data["UAH"]
#     balance_usd = data["USD"]
#
#     return balance_uah, balance_usd
#
#
# # print(available())
#
#
# def buy_xxx(available):
#     with open(available, "w+") as json_file:
#         balance_uah = data["UAH"]
#         balance_usd = data["USD"]
#         rate = current_rate()
#         get_usd = 0
#         if (get_usd * rate) <= balance_uah:
#             balance_uah -= (get_usd * rate)
#             balance_usd += get_usd
#         else:
#             print(f"UNAVAILABLE, REQUIRED BALANCE UAH {get_usd * rate}, AVAILABLE {balance_uah}")
#
#         # json_file.write(json.dumps(balance_uah))
#         # json_file.write(json.dumps(balance_usd))
#
#
# # print(buy_xxx(available))
#
# def sell_xxx(available):
#     with open(available, "w+") as json_file:
#         balance_uah = data["UAH"]
#         balance_usd = data["USD"]
#         rate = current_rate()
#         sell_usd = 0
#         balance_usd -= sell_usd
#         balance_uah += sell_usd * rate
#         if sell_usd <= balance_usd:
#             balance_usd -= sell_usd
#             balance_uah += sell_usd * rate
#         else:
#             print(f"UNAVAILABLE, REQUIRED BALANCE USD {sell_usd}, AVAILABLE {balance_usd}")
#
#         # json_file.write(json.dumps(balance_uah))
#         # json_file.write(json.dumps(balance_usd))
#
#
# def buy_all(available):
#     with open(available, "w+") as json_file:
#         balance_uah = data["UAH"]
#         balance_usd = data["USD"]
#         rate = current_rate()
#         result = balance_uah / rate
#         balance_usd += result
#         balance_uah -= result * rate
#
#
# def sell_all(available):
#     with open(available, "w+") as json_file:
#         balance_uah = data["UAH"]
#         balance_usd = data["USD"]
#         rate = current_rate()
#         result = balance_usd * rate
#         balance_usd -= result / rate
#         balance_uah += result * rate
#
#
# def restart(json_file):
#     #trading_system(start_file, file)
#     pass
#
# #restart(json_file)