import os


def get_input(path: str):
    with open(path) as f:
        return f.read().splitlines()


def run_program(integers: list, noun: int = 0, verb: int = 0):
    p = 0

    if (noun and verb):
        # part 2
        integers[1] = noun
        integers[2] = verb
    else:
        # part 1
        integers[1] = 12
        integers[2] = 2

    while p + 3 < len(integers):
        integer = integers[p]

        n1 = p + 1
        n2 = p + 2
        n3 = p + 3

        index1 = integers[n1]
        index2 = integers[n2]
        index3 = integers[n3]

        if (integer == 1):

            total = integers[index1] + integers[index2]
            integers[index3] = total

        elif (integer == 2):

            total = integers[index1] * integers[index2]
            integers[index3] = total

        elif (integer == 99):
            break

        p += 4

    return integers[0]


def get_part1(integers: list):
    return run_program(integers[:])


def get_part2(integers: list):
    for noun in range(100):
        for verb in range(100):
            if run_program(integers[:], noun, verb) == 19690720:
                return 100 * noun + verb


def main():
    path = os.path.join(os.getcwd(), '2019', 'day2', 'integers.txt')
    integers = [int(i) for i in ''.join(get_input(path)).split(',')]

    part1 = get_part1(integers)
    part2 = get_part2(integers)

    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')


if __name__ == "__main__":
    main()