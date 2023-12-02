DATA_FILE_PATH = "./2023/day2/input.txt"


def read_input(file_name):
    with open(file_name, "r") as file_reader:
        data = [line.strip() for line in file_reader]
    return [line for line in data if line]


def get_part_2(data):
    total_power = 0

    for item in data:
        parts = item.split(":")[1].split(";")

        max_cubes = {"red": 0, "green": 0, "blue": 0}

        for part in parts:
            current_cubes = {"red": 0, "green": 0, "blue": 0}
            pairs = part.split(",")

            for pair in pairs:
                count, color = pair.strip().split()
                current_cubes[color] += int(count)

            for color in max_cubes:
                max_cubes[color] = max(max_cubes[color], current_cubes[color])

        game_power = max_cubes["red"] * max_cubes["green"] * max_cubes["blue"]
        total_power += game_power

    return total_power


def get_part_1(data):
    total_sum = 0

    for item in data:
        base_cube_counts = {"red": 12, "green": 13, "blue": 14}
        valid_game = True

        parts = item.split(":")
        game_index = int(parts[0].split()[1])

        parts = parts[1].split(";")

        for part in parts:
            cube_counts = base_cube_counts.copy()
            pairs = part.split(",")

            for pair in pairs:
                count, color = pair.strip().split()
                cube_counts[color] -= int(count)
                if cube_counts[color] < 0:
                    valid_game = False
                    break

            if not valid_game:
                break

        if valid_game:
            total_sum += game_index

    return total_sum


def main():
    data = read_input(DATA_FILE_PATH)

    result_part_1 = get_part_1(data)
    result_part_2 = get_part_2(data)

    print(result_part_1, result_part_2)


if __name__ == "__main__":
    main()
