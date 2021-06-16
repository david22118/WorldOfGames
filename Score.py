import Utils


def calculate_points_of_winning(difficulty):
    return (difficulty * 3) + 5


def add_score(difficulty):
    points_of_winning = calculate_points_of_winning(difficulty)
    file = open(Utils.SCORES_FILE_NAME, 'a+')
    file.seek(0, 0)
    score = file.read()
    if len(score) == 0:
        file.write(f"{str(points_of_winning)}")
    else:
        new_points_of_winning = points_of_winning + int(score)
        file.truncate(0)
        file.write(f"{str(new_points_of_winning)}")

    file.close
