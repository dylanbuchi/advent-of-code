import os


def get_part1(boarding_passes: list[str]):
    return max(get_seats_ID(boarding_passes))


def get_part2(boarding_passes: list[str]):
    seats_ID = sorted(get_seats_ID(boarding_passes))

    for i in range(1, len(seats_ID)):
        if seats_ID[i - 1] + 1 != seats_ID[i]:
            return seats_ID[i] - 1


def get_boarding_passes(file: str):
    with open(file) as f:
        boarding_passes = f.read().splitlines()

    return boarding_passes


def get_seats_ID(boarding_passes: list[str]):
    seats_ID = []

    for bp in boarding_passes:
        row = bp[:-3]
        col = bp[-3:]

        row_data = get_row_data(row)
        col_data = get_col_data(col)

        seat_ID = row_data * 8 + col_data
        seats_ID.append(seat_ID)

    return seats_ID


def get_binary_data(data: str, boarding_passes_map: dict):
    bin = []

    for ch in data:
        bin.append(boarding_passes_map[ch])

    return bin


def get_row_data(row: str):
    front_back = {'F': '0', 'B': '1'}
    bin = get_binary_data(row, front_back)

    return int(''.join(bin), 2)


def get_col_data(col: str):
    left_right = {'L': '0', 'R': '1'}
    bin = get_binary_data(col, left_right)

    return int(''.join(bin), 2)


def main():
    file = os.path.join(os.getcwd(), 'day5', 'boarding_passes.txt')
    boarding_passes = get_boarding_passes(file)

    part1 = get_part1(boarding_passes)
    part2 = get_part2(boarding_passes)

    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')


if __name__ == "__main__":
    main()