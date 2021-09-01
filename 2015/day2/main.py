from functools import reduce

INPUT_FILE_PATH = './2015/day2/input.txt'


def get_input_data(path: str) -> list:
    with open(path, 'r') as input_file:
        return [line.strip() for line in input_file]


def main():
    input_data = get_input_data(INPUT_FILE_PATH)

    part_1 = get_part_1(input_data)
    part_2 = get_part_2(input_data)

    print(f"{part_1 = }\n{part_2 = }")


def get_part_1(input_data: list) -> int:
    result = 0
    for expression in input_data:
        l, w, h = [int(i) for i in expression.split("x")][:3]

        slack = min((l * w), (w * h), (h * l))
        result += 2 * ((l * w) + (w * h) + (h * l)) + slack

    return result


def get_part_2(input_data: list) -> int:
    result = 0

    for expression in input_data:
        numbers = [int(i) for i in expression.split("x")]
        l, w, h = numbers[:3]

        ribbon = 2 * min((l + w), (w + h), (h + l))
        ribbon_bow = reduce(lambda a, b: a * b, numbers)

        result += ribbon + ribbon_bow

    return result


if __name__ == "__main__":
    main()
