import os


def get_part1(instructions: list[str]):
    index = 0
    seen_indexes = []
    accumulator = 0

    while index not in seen_indexes:
        argument, number = instructions[index].split(' ')
        seen_indexes.append(index)

        index, accumulator = operation(argument, int(number), index,
                                       accumulator)
    return accumulator


def get_part2(instructions: list[str]):

    for index, instruction in enumerate(instructions):
        argument, number = instruction.split(' ')

        temp_instructions = instructions[:]
        temp_argument = temp_number = None

        if argument == "nop":
            temp_argument, temp_number = 'jmp', number

        elif argument == "jmp":
            temp_argument, temp_number = 'nop', number

        elif argument == "acc":
            continue

        temp_instructions[index] = f'{temp_argument} {temp_number}'

        accumulator, is_valid = get_valid_accumulator(temp_instructions)

        if is_valid:
            return accumulator


def operation(argument: str, number: int, index: int, acc: int):
    if (argument == 'acc'):
        acc += number
        index += 1

    elif (argument == 'jmp'):
        index += number

    elif argument == 'nop':
        index += 1

    return [index, acc]


def get_valid_accumulator(instructions):
    accumulator = 0
    index = 0
    seen_indexes = []
    is_valid = False

    while True:
        seen_indexes.append(index)
        argument, number = instructions[index].split(' ')

        index, accumulator = operation(argument, int(number), index,
                                       accumulator)
        if index in seen_indexes:
            is_valid = False
            break

        if index >= len(instructions) - 1:
            is_valid = True
            break

    return accumulator, is_valid


def get_instructions(file):
    with open(file) as f:
        instructions = f.read().splitlines()
    return instructions


def main():
    file = os.path.join(os.getcwd(), 'day8', 'instructions.txt')
    instructions = get_instructions(file)

    part1 = get_part1(instructions)
    part2 = get_part2(instructions)

    print(f'Part1: {part1}')
    print(f'Part2: {part2}')


if __name__ == "__main__":
    main()