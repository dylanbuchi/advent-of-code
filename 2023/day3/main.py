from collections import deque


DATA_FILE_PATH = "./2023/day3/input.txt"
DIRECTIONS = [[0, 1], [1, 0], [0, -1], [-1, 0], [-1, 1], [-1, -1], [1, -1], [1, 1]]


def read_input(file_name):
    with open(file_name, "r") as file_reader:
        data = [line.strip() for line in file_reader]
    return [line for line in data if line]


def is_symbol(ch):
    return not ch.isdigit() and ch != "."


def get_part_1(matrix):
    rows, cols = len(matrix), len(matrix[0])
    total_sum = 0

    for row in range(rows):
        col = 0
        while col < cols:
            if matrix[row][col].isdigit():
                number_str = matrix[row][col]
                j = col + 1
                while j < cols and matrix[row][j].isdigit():
                    number_str += matrix[row][j]
                    j += 1

                if any(
                    0 <= row + dx < rows
                    and 0 <= x + dy < cols
                    and is_symbol(matrix[row + dx][x + dy])
                    for dx, dy in DIRECTIONS
                    for x in range(col, j)
                ):
                    total_sum += int(number_str)

                col = j
            else:
                col += 1

    return total_sum


def get_part_2(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    stars = deque()
    seen = set()

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "*":
                stars.append((row, col))

    total_sum = 0

    while stars:
        row, col = stars.popleft()
        nums = []

        for dx, dy in DIRECTIONS:
            new_row, new_col = dx + row, dy + col
            if (new_row, new_col) in seen:
                continue

            seen.add((new_row, new_col))

            if new_row >= 0 and new_row < rows and new_col >= 0 and new_col < cols:
                if matrix[new_row][new_col].isdigit():
                    start = end = new_col

                    while start >= 0 and matrix[new_row][start].isdigit():
                        start -= 1

                    while end < cols and matrix[new_row][end].isdigit():
                        end += 1

                    digit = int("".join(matrix[new_row][start + 1 : end]))

                    if nums and nums[0] == digit:
                        continue

                    nums.append(digit)

            if len(nums) == 2:
                total_sum += nums[0] * nums[1]
                break

    return total_sum


def main():
    data = read_input(DATA_FILE_PATH)
    matrix = [list(x) for x in data]

    result_part_1 = get_part_1(matrix)
    result_part_2 = get_part_2(matrix)

    print(result_part_1, result_part_2)


if __name__ == "__main__":
    main()
