import os


def get_part1(data):
    count = 0

    for data_list in data:
        start, end, letter, password = data_list
        total_letter_count = password.count(letter)

        if (total_letter_count >= start and total_letter_count <= end):
            count += 1

    return count


def get_part2(data):

    count = 0

    for data_list in data:
        start_pos, end_pos, letter, password = data_list

        start_pos -= 1
        end_pos -= 1

        if (password[start_pos] == letter or password[end_pos] == letter):
            count += 1

        if (password[start_pos] == letter and password[end_pos] == letter):
            count -= 1

    return count


def get_data(file):
    data_list = []

    with open(file) as f:
        for line in f.readlines():
            line.replace('\n', '')

            number, letter, password = line.split()
            start, end = number.split('-')

            data_list.append([int(start), int(end), letter[0], password])

    return data_list


def main():
    file_path = os.path.join(os.getcwd(), 'day2', 'data.txt')

    data = get_data(file_path)

    part1 = get_part1(data)
    part2 = get_part2(data)

    print(f'Part 1 total valid passwords: {part1}')
    print(f'Part 2 total valid passwords: {part2}')


if __name__ == "__main__":
    main()