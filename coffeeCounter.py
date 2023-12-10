from datetime import date
import json
import os.path


COFFEE_BASE_FILE = "coffee_base.json"


def track_coffee_for_today():
    value = int(input('Please enter your amount of coffee for today: '))
    key = str(date.today())
    save_data(key, value)
    print('Your amount has been saved in the coffee base!')


def track_coffee_for_another_day():
    key = input('Please enter the date you want to track your coffee for (yyyy-mm-dd): ')
    value = int(input('Please enter your amount of coffee for this day: '))
    save_data(key, value)
    print('Your amount has been saved in the coffee base!')


def print_coffee_consumption():
    with open(COFFEE_BASE_FILE, "r") as read_file:
        data = json.load(read_file)

    sorted_data = dict(sorted(data.items()))
    summed_up = 0

    for data_entry in sorted_data.items():
        print(
            "{}:{}".format(
                str(data_entry[0]).ljust(15, " "),
                str(data_entry[1]).rjust(3, " ")
            )
        )
        summed_up += data_entry[1]

    print(
        "{}:{}".format(
            "Total Coffees".ljust(15, " "),
            str(summed_up).rjust(3, " ")
        )
    )


def save_data(user_date, user_amount):
    if not os.path.isfile(COFFEE_BASE_FILE):
        with open(COFFEE_BASE_FILE, "w") as write_file:
            json.dump({}, write_file)

    with open(COFFEE_BASE_FILE, "r") as read_file:
        data = json.load(read_file)

    data[user_date] = user_amount

    with open(COFFEE_BASE_FILE, "w") as write_file:
        json.dump(data, write_file)


if __name__ == "__main__":
    print("[1] Track Coffee for today")
    print("[2] Track Coffee for another day")
    print("[3] Show Coffee consumption")
    user_input_number = int(input('Please choose a number: '))

    if user_input_number == 1:
        track_coffee_for_today()
    elif user_input_number == 2:
        track_coffee_for_another_day()
    elif user_input_number == 3:
        print_coffee_consumption()
    else:
        print('Please try harder next time!')
