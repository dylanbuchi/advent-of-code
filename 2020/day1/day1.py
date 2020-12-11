import os


def get_part1(nums: list, target: int):
    seen = {}

    for _, num in enumerate(nums):
        complement = target - num

        if seen.get(num, -1) != -1:
            return seen[num] * num

        seen[complement] = num

    return 'None'


def get_part2(nums: list, target: int):
    size = len(nums)

    for i in range(0, size - 2):
        for j in range(i + 1, size - 1):
            for k in range(j + 1, size):
                total = nums[i] + nums[j] + nums[k]

                if total == target:
                    return nums[i] * nums[j] * nums[k]
    return 'None'


def get_numbers(file):
    numbers = []

    with open(file) as f:
        for line in f.readlines():
            num = line.replace('\n', '')
            numbers.append(int(num))

    return numbers


def main():
    file_path = os.path.join(os.getcwd(), '2020', 'day1', 'numbers.txt')
    numbers = get_numbers(file_path)

    part1 = get_part1(numbers, 2020)
    part2 = get_part2(numbers, 2020)

    print(f'Part 1: {part1}\nPart 2: {part2}')


if __name__ == "__main__":
    main()
