import random


def generate_number(difficulty_number):
    return random.randint(1, difficulty_number)


def get_guess_from_user(difficulty_number, player_number=0):
    if 1 <= player_number <= difficulty_number:
        return player_number

    player_number = int(input(f"Please guess a number from 1 to {difficulty_number}: "))

    return get_guess_from_user(difficulty_number, player_number)


def compare_results(secret_number, player_number):
    return secret_number == player_number


def play(difficulty_number):
    secret_number = generate_number(difficulty_number)
    player_number = get_guess_from_user(difficulty_number)
    return compare_results(secret_number, player_number)
