import os


def get_part1(file):
    bags = ['shiny gold']
    flag = True

    while flag:
        flag = False

        with open(file) as f:
            for line in f:
                line = line.replace('.', '').strip()
                bag_name = line[:line.index('bags', )].strip()

                if bag_name in bags or line.replace(' ', '').isalpha():
                    continue

                elif any(bag in line for bag in bags):
                    bags.append(bag_name)
                    flag = True

    return len(bags) - 1


def main():
    file = os.path.join(os.getcwd(), 'day7', 'bags.txt')
    part1 = get_part1(file)

    print(f'Part1: {part1}')


if __name__ == "__main__":
    main()
