import random, json

start_file = "config.json"

file = "trading_system.json"


def trading_system(start_file, file):
    with open(start_file, "r") as s_file, open(file, "w") as json_file:
        json_file.write(s_file.read())
        # return json_file


with open(file, "r") as json_file:
    data = json.load(json_file)


def current_rate():
    course_get = data["course"]
    return course_get


print(current_rate())


def rate_change(current_rate):
    delta = random.uniform(-data["delta"], data["delta"])
    rate = (current_rate + delta)

    return rate


# print(rate_change(current_rate()))


def next_roll(item):
    with open("trading_system.json", "w+") as json_file:
        data["course"] = item
        print(item)
        json_file.write(json.dumps(data))


next_roll(rate_change(current_rate()))


def available():
    balance_uah = data["UAH"]
    balance_usd = data["USD"]

    return balance_uah, balance_usd


print(available())


def buy_xxx(available):
    with open(available, "w") as json_file:
        balance_uah = data["UAH"]
        balance_usd = data["USD"]
        rate = current_rate()
        amount = 100
        result = rate * amount
        if result < balance_uah:
            balance_usd += amount
            balance_uah -= result
        else:
            print(f"UNAVAILABLE, REQUIRED BALANCE UAH {result}, AVAILABLE {balance_uah}")

        json_file.write(json.dumps(balance_uah))
        json_file.write(json.dumps(balance_usd))


#print(buy_xxx(available))


def sell_xxx(json_file):
    pass


def buy_all(json_file):
    pass


def sell_all(json_file):
    pass


def restart(json_file):
    # trading_system(start_file, file)
    pass
