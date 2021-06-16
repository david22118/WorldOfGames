import random
import numpy as np
import Utils


def generate_sequence(difficulty_number):
    random_lis_of_numbers = []
    while len(random_lis_of_numbers) < difficulty_number:
        random_lis_of_numbers.append(random.randint(1, 101))
    print(random_lis_of_numbers)
    return random_lis_of_numbers


def get_list_from_user(difficulty_number):
    print(f"Please enter {difficulty_number} numbers you remembered in the appropriate order-left to right")

    list_from_user = []
    for number in range(difficulty_number):
        list_from_user.append(int(input(f"In {1 + number}th place on the list, list-left to right:")))
    return list_from_user


def is_list_equal(generate_list, user_list):
    return np.array_equiv(generate_list, user_list)


def play(difficulty_number):
    generate_list = generate_sequence(difficulty_number)
    Utils.screen_cleaner()
    user_list = get_list_from_user(difficulty_number)
    return is_list_equal(generate_list, user_list)
