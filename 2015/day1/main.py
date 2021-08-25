INPUT_FILE_PATH = './2015/day1/input.txt'


def get_input_data(path: str) -> str:
    with open(path, 'r') as input_file:
        return input_file.readline()


def main():
    input_data = get_input_data(INPUT_FILE_PATH)
    rules = {'(': 1, ')': -1}

    part_1 = get_part_1(input_data, rules)
    part_2 = get_part_2(input_data, rules)

    print(f"{part_1 = }\n{part_2 = }")


def get_part_1(input_data: str, rules: dict) -> int:
    return sum(rules[p] for p in input_data)


def get_part_2(input_data: str, rules: dict) -> int:
    total = 0
    for i, p in enumerate(input_data):
        total += rules[p]
        if total == -1:
            return i + 1
    return 0


if __name__ == "__main__":
    main()