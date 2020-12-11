import os


def get_part1(joltages):
    sorted_joltages = sorted(joltages)

    l = 0
    r = 1

    differences = []

    while r < len(sorted_joltages):
        joltage = sorted_joltages[l]
        next_joltage = sorted_joltages[r]

        diff = next_joltage - joltage

        differences.append(diff)

        l += 1
        r += 1

    one_differences = len(list(filter(lambda x: x == 1, differences))) + 1
    three_differences = len(list(filter(lambda x: x == 3, differences))) + 1

    return one_differences * three_differences


def get_joltages(file):
    with open(file) as f:
        return [int(i) for i in f.read().splitlines()]


def main():

    file = os.path.join(os.getcwd(), '2020', 'day10', 'joltages.txt')
    joltages = get_joltages(file)

    part1 = get_part1(joltages)

    print(part1)


if __name__ == "__main__":
    main()