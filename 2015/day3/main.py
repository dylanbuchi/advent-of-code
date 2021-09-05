INPUT_FILE_PATH = './2015/day3/input.txt'


def get_input_data(path: str) -> list:
    with open(path, 'r') as input_file:
        return [line.strip() for line in input_file]


def main():
    input_data = get_input_data(INPUT_FILE_PATH)
    directions = input_data[0]

    part_1 = len(get_part_1(directions))
    part_2 = get_part_2(directions)

    print(f"{part_1 = }\n{part_2 = }")


def get_part_1(directions: str) -> set:
    directions_map = {'^': (1, 1), 'v': (1, -1), '<': (0, -1), '>': (0, 1)}

    current_x_y_pos = [0, 0]
    result_set = {tuple(current_x_y_pos)}

    for direction in directions:

        x_or_y, value = directions_map[direction][:2]
        current_x_y_pos[x_or_y] += value

        result_set.add(tuple(current_x_y_pos))

    return result_set


def get_part_2(directions: str) -> int:
    santa_part = ''.join(d for i, d in enumerate(directions) if i % 2)
    robot_part = ''.join(d for i, d in enumerate(directions) if not i % 2)

    santa_set = get_part_1(santa_part)
    robot_set = get_part_1(robot_part)

    return len(robot_set | santa_set)


if __name__ == "__main__":
    main()
