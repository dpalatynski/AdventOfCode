# Day 3
from re import finditer
from collections import defaultdict
from math import prod


def day3(my_input):
    engine_schematic = my_input.split('\n')
    symbols = set()
    for row in range(len(engine_schematic)):
        for col in range(len(engine_schematic[0])):
            if engine_schematic[row][col] not in '01234566789.':
                symbols.add((row, col))

    neighbors = [(0, -1), (0, 1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    numbers = defaultdict(list)
    for row in range(len(engine_schematic)):
        for m in finditer(r'\d+', engine_schematic[row]):
            range_points = set()   
            for neighbor in neighbors:
                for x in range(m.start(), m.end()):
                    range_points.add((row + neighbor[0], x + neighbor[1]))

            for c in symbols & range_points:
                numbers[c].append(int(m[0]))

    part1 = sum([sum(number) for number in numbers.values()])
    part2 = sum([prod(number) for number in numbers.values() if len(number) == 2])

    return part1, part2


sample_input = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''


# Test
assert(day3(sample_input) == (4361, 467835))


# Results
my_input = open(r"2023/inputs/Day_03.txt").read()
print(day3(my_input))
