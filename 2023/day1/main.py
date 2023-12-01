DATA_FILE_PATH = "./2023/day1/input.txt"


def read_input(file_name):
    with open(file_name, "r") as file_reader:
        data = [line.strip() for line in file_reader]
    return [line for line in data if line]


def find_digit_part_2(word, reverse=False):
    word_to_digit = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    if reverse:
        word_to_digit = {key[::-1]: word_to_digit[key] for key in word_to_digit}
        word = word[::-1]

    for i in range(len(word)):
        for ch, digit in word_to_digit.items():
            if word[i:].startswith(ch):
                return digit
        if word[i].isdigit():
            return word[i]


def find_digit_part_1(word, reverse=False):
    if reverse:
        word = word[::-1]

    for ch in word:
        if ch.isnumeric():
            return ch


def get_part(data, part_2=False):
    total_sum = 0

    for word in data:
        first_digit = find_digit_part_1(word) if not part_2 else find_digit_part_2(word)
        last_digit = (
            find_digit_part_1(word, reverse=True)
            if not part_2
            else find_digit_part_2(word, reverse=True)
        )

        total_sum += int(first_digit + last_digit)

    return total_sum


def main():
    data = read_input(DATA_FILE_PATH)

    result_part_1 = get_part(data)
    result_part_2 = get_part(data, part_2=True)

    print(result_part_1, result_part_2)


if __name__ == "__main__":
    main()
