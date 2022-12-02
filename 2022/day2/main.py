import os

DATA_FILE_PATH = os.path.join(os.getcwd(), "2022", "day2", "input.txt")

ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"

ROCK_POINTS = 1
PAPER_POINTS = 2
SCISSORS_POINTS = 3


WIN = "win"
DRAW = "draw"
LOST = "lost"

WIN_POINTS = 6
DRAW_POINTS = 3
LOST_POINTS = 0


OPPONENT_SETTINGS = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,
}

PART_1_SETTINGS = {
    **OPPONENT_SETTINGS,
    # player
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSORS,
}


PART_2_SETTINGS = {
    **OPPONENT_SETTINGS,
    # player
    "X": LOST,
    "Y": DRAW,
    "Z": WIN,
}


GAME_POINTS = {
    # shape points
    ROCK: ROCK_POINTS,
    PAPER: PAPER_POINTS,
    SCISSORS: SCISSORS_POINTS,
    # end game points
    WIN: WIN_POINTS,
    DRAW: DRAW_POINTS,
    LOST: LOST_POINTS,
}

GAME_FIGHT_RULES = {
    # shape key beats shape value
    ROCK: SCISSORS,
    PAPER: ROCK,
    SCISSORS: PAPER,
}


def get_winner(player, opponent):
    if player == opponent:
        return DRAW

    return player if GAME_FIGHT_RULES[player] == opponent else opponent


def get_data():
    with open(DATA_FILE_PATH) as data_file:
        output = []
        for item in data_file.read().splitlines():
            output.append(tuple(item.split(" ")))
        return output


def play_game(strategy_guide):
    player_total_points = 0

    for opponent_char, player_char in strategy_guide:
        opponent = PART_1_SETTINGS[opponent_char]
        player = PART_1_SETTINGS[player_char]

        winner = get_winner(player, opponent)
        player_total_points += GAME_POINTS[player]

        if winner == opponent:
            continue

        player_total_points += GAME_POINTS[DRAW] if winner == DRAW else GAME_POINTS[WIN]

    return player_total_points


def get_shape_that_beats(other_shape):
    return GAME_FIGHT_RULES[GAME_FIGHT_RULES[other_shape]]


def play_game_2(strategy_guide):
    player_total_points = 0

    for opponent_char, player_char in strategy_guide:
        opponent = PART_2_SETTINGS[opponent_char]

        todo = PART_2_SETTINGS[player_char]

        if todo == WIN:
            win_shape = get_shape_that_beats(opponent)
            player_total_points += GAME_POINTS[win_shape] + GAME_POINTS[WIN]
            continue

        if todo == DRAW:
            player_total_points += GAME_POINTS[opponent] + GAME_POINTS[DRAW]
            continue

        if todo == LOST:
            loser_shape = GAME_FIGHT_RULES[opponent]
            player_total_points += GAME_POINTS[loser_shape]

    return player_total_points


def main():
    strategy_guide = get_data()

    output_part_1 = play_game(strategy_guide)
    output_part_2 = play_game_2(strategy_guide)

    print("Answer part 1:", output_part_1)
    print("Answer part 2:", output_part_2)


if __name__ == "__main__":
    main()
