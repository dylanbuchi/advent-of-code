import os

DATA_FILE_PATH = os.path.join(os.getcwd(), "2022", "day3", "input.txt")


def get_data():
    with open(DATA_FILE_PATH) as data_file:
        return data_file.read().splitlines()


def set_sum_to(alphabet, letter):
    index = ord(letter.lower()) - ord("a")
    amount = index + 1

    alphabet[index] += (
        amount + 26 if abs(ord(letter) - ord(letter.lower())) == 32 else amount
    )


def create_list(size):
    return [0] * size


def get_common_letter(*sets):
    return list(set.intersection(*sets)).pop()


def get_part_1(rucksack):
    alphabet = create_list(26)

    for item in rucksack:
        mid = len(item) // 2

        first_part = set(item[:mid])
        last_part = set(item[mid:])

        common_letter = get_common_letter(first_part, last_part)
        set_sum_to(alphabet, common_letter)

    return sum(alphabet)


def get_part_2(rucksack):
    alphabet = create_list(26)
    temp = []

    for index, item in enumerate(rucksack):
        temp.append(set(item))

        if (index + 1) % 3 == 0:
            common_letter = get_common_letter(*temp)
            set_sum_to(alphabet, common_letter)
            temp = []

    return sum(alphabet)


def main():

    rucksack = get_data()

    output_part_1 = get_part_1(rucksack)
    output_part_2 = get_part_2(rucksack)

    print("Part 1:", output_part_1)
    print("Part 2:", output_part_2)


if __name__ == "__main__":
    main()
