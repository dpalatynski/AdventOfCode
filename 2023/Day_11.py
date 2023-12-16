# Day 11
from itertools import combinations


def calculate_empty_rows(image):
    no_empty = []
    current = 0
    for line in image:
        if "#" not in line:
            current += 1
        no_empty.append(current)

    return no_empty


def shortest_path(y1, x1, y2, x2, rows, columns, expand):
    dist = abs(y2 - y1) + abs(x2 - x1) # Manhattan distance if expand = 0

    # Number of additional rows/columns added
    # Multiplication of number of rows to expand and number of empty
    # entries found between two points 
    # expand - 1 because one is in fact empty from the beginning
    dist += (expand-1) * (columns[max(x2, x1)] - columns[min(x2, x1)]) 
    dist += (expand-1) * (rows[max(y2, y1)] - rows[min(y2, y1)])

    return dist


def day11(my_input, expand):
    image = my_input.split('\n')
    rows = calculate_empty_rows(image)
    columns = calculate_empty_rows(list(map(list, zip(*image))))

    hash_coordinates = [(i, j) for i, row in enumerate(image) for j, char in enumerate(row) if char == '#']
    unique_pairs = list(set(combinations(hash_coordinates, 2)))

    lengths = 0
    for (y1, x1), (y2, x2)  in unique_pairs:
        lengths += shortest_path(y1, x1, y2, x2, rows, columns, expand)

    return lengths


sample_input = '''...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....'''


# Tests
assert day11(sample_input, 2) == 374
assert day11(sample_input, 10) == 1030
assert day11(sample_input, 100) == 8410


# Results
my_input = open(r"2023/inputs/Day_11.txt").read()
print(day11(my_input, 2))
print(day11(my_input, 10**6))
