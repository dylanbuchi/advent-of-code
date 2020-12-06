import os


def get_part1(file):
    with open(file) as f:
        questions = f.read()

        result = [
            set.union(*[set(i) for i in q.split()])
            for q in questions.split('\n\n')
        ]

    return sum([len(i) for i in result])


def get_part2(file):
    with open(file) as f:
        questions = f.read()

        result = [
            set.intersection(*[set(i) for i in q.split()])
            for q in questions.split('\n\n')
        ]

    return sum([len(i) for i in result])


def main():
    file = os.path.join(os.getcwd(), 'day6', 'questions.txt')

    part1 = get_part1(file)
    part2 = get_part2(file)

    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')


if __name__ == "__main__":
    main()