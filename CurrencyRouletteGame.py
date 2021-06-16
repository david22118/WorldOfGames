import requests
import json
import random


def get_current_exchange_rate():
    response = requests.get(
        'https://free.currconv.com/api/v7/convert?q=USD_ILS&compact=ultra&apiKey=75072ddc8046a6e46127').content
    data = str(json.loads(response)['USD_ILS'])
    return data


def generate_random_money_value():
    random_value = random.randint(1, 101)
    return random_value


def generate_total_money_value(money_value, exchange_rate):
    return money_value * float(exchange_rate)


def generate_interval(difficulty_number, total_money_value):
    interval = {"lower_boundary": float(total_money_value - (5 - difficulty_number)),
                "upper_boundary": float(total_money_value + (5 - difficulty_number)),
                }
    return interval


def get_money_interval(difficulty, total_money_value):
    interval = generate_interval(difficulty, total_money_value)
    return interval


def get_guess_from_user(money_value):
    user_guess = input(f"what is the value of the generated number,{money_value},from USD to ILS:")
    return int(user_guess)


def check_answer(interval, user_guess):
    if interval["lower_boundary"] <= user_guess <= interval["upper_boundary"]:
        return True
    else:
        return False


def play(difficulty_number):
    exchange_rate = get_current_exchange_rate()
    random_money_value = generate_random_money_value()
    total_money_value = generate_total_money_value(random_money_value, exchange_rate)
    interval = generate_interval(difficulty_number, total_money_value)
    user_guess = get_guess_from_user(random_money_value)
    return check_answer(interval, user_guess)


