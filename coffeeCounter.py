from datetime import date
import json

coffee_base = dict()


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


def save_data(user_date, user_amount):
    with open("coffee_base.json", "r") as read_file:
        data = json.load(read_file)
    data[user_date] = user_amount
    with open("coffee_base.json", "w") as write_file:
        json.dump(data, write_file)


def get_user_input():
    print("1: Track Coffee for today")
    print("2: Track Coffee for another")
    user_input_number = int(input('Please choose a number:'))

    if user_input_number == 1:
        track_coffee_for_today()
    if user_input_number == 2:
        track_coffee_for_another_day()
    if not user_input_number == 1 or user_input_number == 2:
        print('Please try harder next time!')


get_user_input()
