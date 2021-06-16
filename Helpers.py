def get_name():
    name = input("Please type your name: ")
    return name


def print_game_description():
    print("\nPlease choose a game to play:"
          "\n\t1. Memory Game - a sequence of numbers will appear for 1 second and you have to"
          "\nguess it back"
          "\n\t2. Guess Game - guess a number and see if you chose like the computer"
          "\n\t3. Currency Roulette - try and guess the value of a random amount of USD in ILS")


def get_game_number(game_number=0):
    if 1 <= game_number <= 3:
        return game_number

    game_number = int(input("Enter game number from 1 to 3: "))

    return get_game_number(game_number)


def get_game_difficulty(game_difficulty=0):
    if 1 <= game_difficulty <= 5:
        return game_difficulty
    game_difficulty = int(input("Please choose game difficulty from 1 to 5: "))

    return get_game_difficulty(game_difficulty)


