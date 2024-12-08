# Day 8
from itertools import combinations


def day8(my_input):
    def calculate_distance(point_1, point_2):
        x1, y1 = point_1
        x2, y2 = point_2
        return (x1 - x2), (y1 - y2)
    
    lista = [list(x) for x in my_input.strip().split('\n')]

    antenas = {}
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j] != '.':
                if lista[i][j] in antenas:
                    antenas[lista[i][j]].append((i, j))
                else:
                    antenas[lista[i][j]] = [(i, j)]

    part1_antinodes = set()
    part2_antinodes = set()
    for key in antenas:
        comb = list(combinations(antenas[key], 2))
        for c in comb:
            dist = calculate_distance(c[0], c[1])
            part1_antinode1 = calculate_distance(c[0], (-dist[0], -dist[1]))
            part1_antinode2 = calculate_distance(c[1], (dist[0], dist[1]))
            for i in range(0, len(lista)):
                antinode1 = (-i*dist[0] + part1_antinode1[0], -i*dist[1] + part1_antinode1[1])
                antinode2 = (i*dist[0] + part1_antinode2[0], i*dist[1] + part1_antinode2[1])

                if antinode1[0] < 0 or antinode1[1] < 0 or antinode1[0] > len(lista)-1 or antinode1[1] > len(lista[0])-1:
                    pass
                else:
                    if i == 0:
                        part1_antinodes.add(antinode1)
                    part2_antinodes.add(antinode1)
                if antinode2[0] < 0 or antinode2[1] < 0 or antinode2[0] > len(lista)-1 or antinode2[1] > len(lista[0])-1:
                    pass
                else:
                    if i == 0:
                        part1_antinodes.add(antinode2)
                    part2_antinodes.add(antinode2)

    return len(part1_antinodes), len(part2_antinodes)


sample_input = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""

my_input = open(r"2024/inputs/Day_08.txt").read()

# Tests
assert day8(sample_input) == (14, 34)

# Results
print(day8(my_input))
