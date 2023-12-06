import re

DATA_FILE_PATH = "./2023/day4/input.txt"


def read_input(file_name):
    with open(file_name, "r") as file_reader:
        return [line.strip() for line in file_reader]


def calculate_card_points(winning_nums, card_nums):
    match_count = count_matches(winning_nums, card_nums)
    return 2 ** (match_count - 1) if match_count > 0 else 0


def parse_line(line):
    parts = line.split("|")
    winning_nums = set(re.findall(r"\d+", parts[0])[1:])
    card_nums = re.findall(r"\d+", parts[1])
    return winning_nums, card_nums


def count_matches(winning_nums, card_nums):
    return sum(num in winning_nums for num in card_nums)


def process_card_recursive(card, data, index, cards_count):
    winning_nums, card_nums = parse_line(card)

    matches = count_matches(winning_nums, card_nums)
    for i in range(1, matches + 1):
        if index + i < len(data):
            cards_count[index + i] += 1
            process_card_recursive(data[index + i], data, index + i, cards_count)


def get_part_1(data):
    total_points = 0

    for line in data:
        winning_nums, card_nums = parse_line(line)
        total_points += calculate_card_points(winning_nums, card_nums)

    return total_points


def get_part_2(data):
    cards_count = [1] * len(data)

    for index, card in enumerate(data):
        process_card_recursive(card, data, index, cards_count)

    return sum(cards_count)


def main():
    data = read_input(DATA_FILE_PATH)

    result_part_1 = get_part_1(data)
    result_part_2 = get_part_2(data)

    print(result_part_1)
    print(result_part_2)


if __name__ == "__main__":
    main()
