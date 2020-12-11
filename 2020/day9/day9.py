import os


def get_part1(numbers: list[int]):

    left = 0
    right = 24

    index = 25

    while right < len(numbers):
        sum_in_numbers = two_sum(numbers, left, right, numbers[index])

        if (sum_in_numbers):
            index += 1

        left += 1
        right += 1

    return numbers[index]


def get_part2(numbers: list[int]):
    invalid_number = get_part1(numbers)
    numbers_list = list(filter(lambda x: x < invalid_number, numbers))

    contiguous_set = []

    index = 0

    while index < len(numbers_list):
        total = 0
        temp_index = index
        temp_list = []

        while temp_index < len(numbers_list):
            temp_list.append(numbers_list[temp_index])
            total += numbers_list[temp_index]

            if total == invalid_number:
                contiguous_set = temp_list
                break

            temp_index += 1

        index += 1

    result = max(contiguous_set) + min(contiguous_set)
    return result


def two_sum(numbers: list[int], left: int, right: int, target: int):
    seen = {}

    for i in range(left, right + 1):
        number = numbers[i]
        complement = target - number

        if seen.get(complement):
            return True

        seen[number] = complement

    return False


def get_numbers(file: str):
    with open(file) as f:
        numbers = [int(i) for i in f.read().splitlines()]
    return numbers


def main():
    file = os.path.join(os.getcwd(), '2020', 'day9', 'numbers.txt')

    numbers = get_numbers(file)

    part1 = get_part1(numbers)
    part2 = get_part2(numbers)

    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')


if __name__ == "__main__":
    main()
