from collections import deque

NUMBERS_FILEPATH = "./2021/day1/input.txt"


class Numbers:
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath
        self.numbers = self.get_numbers()

    def get_numbers(self) -> list[int]:
        with open(self.filepath) as numbers:
            return list(map(int, numbers.read().splitlines()))

    def is_numbers_valid(self) -> bool:
        return bool(self.numbers)


def get_part1(numbers_object: Numbers) -> int | None:
    numbers = numbers_object.numbers

    if not numbers_object.is_numbers_valid():
        return

    previous_number = numbers[0]
    count = 0

    for i in range(1, len(numbers)):
        number = numbers[i]

        if number > previous_number:
            count += 1

        previous_number = number

    return count


def get_part2(numbers_object: Numbers, k: int) -> int | None:
    numbers = numbers_object.numbers

    if not numbers_object.is_numbers_valid():
        return

    previous_sum = sum(numbers[:k])
    current_sum = count = 0

    temp = deque()

    for i in range(1, len(numbers)):
        temp.append(numbers[i])

        if len(temp) == k:
            current_sum = sum(temp)

            if current_sum > previous_sum:
                count += 1

            previous_sum = current_sum
            temp.popleft()

    return count


def main() -> None:

    numbers_object = Numbers(NUMBERS_FILEPATH)

    print(get_part1(numbers_object))
    print(get_part2(numbers_object, 3))


if __name__ == "__main__":
    main()