import os


def get_total_by_slope(number, data):
    locations = data[1::]

    i = number
    total = 0

    for location in locations:
        if location[0][i] == '#':
            total += 1
        if (i + number >= len(location[0])):
            i = (i - len(location[0])) % number
        else:
            i += number
    return total


def get_total_by_slope_right_1_down_2(data: list):

    locations = [x for i, x in enumerate(data[2:]) if i % 2 == 0]

    i = 1
    total = 0

    for location in locations:
        if location[0][i] == '#':
            total += 1
        if (i + 1 >= len(location[0])):
            i = (i - len(location[0])) % 1
        else:
            i += 1

    return total


def get_part1(data: list):
    return get_total_by_slope(3, data)


def get_part2(data: list):

    s1 = get_total_by_slope(1, data)
    s3 = get_total_by_slope(3, data)
    s5 = get_total_by_slope(5, data)
    s7 = get_total_by_slope(7, data)
    s1_2 = get_total_by_slope_right_1_down_2(data)

    total = s1 * s3 * s5 * s7 * s1_2

    return total


def get_data(file):
    locations = []

    with open(file) as f:
        for line in f.readlines():
            if ('\n' in line):
                locations.append([line[:-1]])
            else:
                locations.append([line])

    return locations


def main():
    path = os.path.join(os.getcwd(), 'day3', 'locations.txt')

    locations = get_data(path)

    part1 = get_part1(locations)
    part2 = get_part2(locations)

    print(f'Part 1: {part1} ')
    print(f'Part 2: {part2} ')


if __name__ == "__main__":
    main()
