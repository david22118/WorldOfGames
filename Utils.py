import os
from time import sleep

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = "404"


def screen_cleaner():
    sleep(1)
    os.system("cls")
    sleep(1)
