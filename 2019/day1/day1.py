import os


def get_part1(masses: list):
    return sum(calculate(i) for i in masses)


def get_part2(masses: list):
    fuels = []

    for mass in masses:
        fuels.append(sum(calculate_recursive(mass, [])))

    return sum(fuels)


def calculate(mass: int):
    return (mass // 3) - 2


def get_masses(file: str):
    with open(file) as f:
        return [int(i) for i in f.read().splitlines()]


def calculate_recursive(mass: int, total: list):
    if (mass <= 0):
        return total[1:]

    total.append(mass)

    return calculate_recursive((mass // 3) - 2, total)


def main():

    file = os.path.join(os.getcwd(), '2019', 'day1', 'masses.txt')
    masses = get_masses(file)

    part1 = get_part1(masses)
    part2 = get_part2(masses)

    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')


if __name__ == "__main__":
    main()
