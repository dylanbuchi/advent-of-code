import os
import heapq

DATA_FILE_PATH = os.path.join(os.getcwd(), "2022", "day1", "input.txt")


def get_data() -> list[int]:
    with open(DATA_FILE_PATH) as data_file:
        return list(
            map(
                lambda item: int(item) if len(item) else -1,
                data_file.read().splitlines(),
            )
        )


def get_max_calories(calories: list[int]) -> list[int]:
    max_calories = []

    current_max = 0

    for calory in calories:
        if calory == -1:
            max_calories.append(current_max)
            current_max = 0
        else:
            current_max += calory

    return max_calories


def get_part_2_answer(max_calories: list[int], top_amount: int):
    output = []
    heapq.heapify(max_calories)

    for _ in range(top_amount):
        output.append(heapq.heappop(max_calories) * -1)

    return sum(output)


def main() -> None:
    calories = get_data()

    max_calories = get_max_calories(calories)

    output_part_1 = max(max_calories)
    output_part_2 = get_part_2_answer([num * -1 for num in max_calories], 3)

    print("Answer part 1:", output_part_1)
    print("Answer part 2:", output_part_2)


if __name__ == "__main__":
    main()
