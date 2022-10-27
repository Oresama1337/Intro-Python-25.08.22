import utils


if __name__ == "__main__":
    launch_setup()
    command = assignement_command_argument()

    if command == "RATE":
        print(current_rate())

    elif command == "AVAILABLE":
        print(available())

    elif command.split()[0] == "BUY":
        if command.split()[1] == "ALL":
            buy_all_usd()
        else:
            buy_usd(float(command.split()[1]))
    elif command.split()[0] == "SELL":
        if command.split()[1] == "ALL":
            sell_all_usd()
        else:
            sell_usd(float(command.split()[1]))
    elif command == "NEXT":
        next_roll()
    elif command == "RESTART":
        restart()


