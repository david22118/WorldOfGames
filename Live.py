import Helpers
import GuessGame
import MemoryGame
import CurrencyRouletteGame
import Score


def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WoG)."
          f"\nHere you can find many cool games to play.")


def play_selected_game(number, *args):
    switcher = {
        1: MemoryGame.play,
        2: GuessGame.play,
        3: CurrencyRouletteGame.play
    }
    selected_game = switcher.get(number)
    return selected_game(*args)


def load_game():
    Helpers.print_game_description()
    game_number = Helpers.get_game_number()
    game_difficulty = Helpers.get_game_difficulty()

    if play_selected_game(game_number, game_difficulty):
        Score.add_score(game_difficulty)
    else:
        print("You lost , try again")
