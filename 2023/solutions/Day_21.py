# Day 21
from collections import deque
import numpy as np


def start(garden_map):
    for i in range(len(garden_map)):
        for j in range(len(garden_map[0])):
            if garden_map[i][j] == 'S':
                return (j, i, 0)
            

def find_quadratic_function(points):
    x = np.array([p[0] for p in points])
    y = np.array([p[1] for p in points])

    A = np.vstack([x**2, x, np.ones(len(points))]).T

    (a, b, c) = np.linalg.solve(A, y)

    return (a, b, c)


def expand_list(input_list):
    rows = len(input_list)
    cols = len(input_list[0])

    expanded_list = [[0] * (cols * 3) for _ in range(rows * 3)]

    # Copy the input list to the center
    for row in range(rows):
        for col in range(cols):
            expanded_list[row + rows][col + cols] = input_list[row][col]

    # Expand horizontally
    for row in range(rows):
        for col in range(cols):
            expanded_list[row + rows][col] = input_list[row][col]
            expanded_list[row + rows][col + cols*2] = input_list[row][col]

    # Expand vertically
    for row in range(rows):
        for col in range(cols):
            expanded_list[row][col + cols] = input_list[row][col]
            expanded_list[row + rows*2][col + cols] = input_list[row][col]

    # Expand diagonally
    for row in range(rows):
        for col in range(cols):
            expanded_list[row][col] = input_list[row][col]
            expanded_list[row + rows*2][col + cols*2] = input_list[row][col]
            expanded_list[row][col + cols*2] = input_list[row][col]
            expanded_list[row + rows*2][col] = input_list[row][col]

    return expanded_list


def garden_plots(garden_map, steps):
    result = 0
    queue = deque()
    queue.append(start(garden_map))
    visited = set()
    while len(queue) > 0:
        i, j, dist = queue.popleft()
        
        if (i, j, dist) in visited:
                continue
        visited.add((i, j, dist))

        if dist == steps: 
            result += 1

        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for neighbor in neighbors:
            ii, jj = i + neighbor[0], j + neighbor[1]
            if ii < 0 or ii >= len(garden_map[0]) or jj < 0 or jj >= len(garden_map):
                continue

            if garden_map[ii][jj] == '#':
                continue

            if (ii, jj, dist+1) in visited:
                continue
        
            if dist < steps:
                queue.append((ii, jj, dist+1))

    return result


def day21(my_input, part, step=None):
    if part == 1:
        return garden_plots(my_input.split('\n'), step)
    elif part == 2:
        steps = [65, 65+131, 65+131+131] # 131 is a size of my input
        actual_steps = 26501365
        garden_map = expand_list(expand_list([list(row) for row in my_input.replace('S', '.').split('\n')]))
        garden_map[len(garden_map)//2][len(garden_map)//2] = 'S'
        points = []
        for step in steps: 
            points.append((step, garden_plots(garden_map, step)))

        (a, b, c) = find_quadratic_function(points)

        return int(a * actual_steps**2 + b * actual_steps + c)
    

sample_input = '''...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........'''


# Test
assert(day21(sample_input, 1, 6) == 16)


# Results
my_input = open(r"2023/inputs/Day_21.txt").read()
print(day21(my_input, 1, 64))
print(day21(my_input, 2))
