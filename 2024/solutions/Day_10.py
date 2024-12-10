# Day 10
from collections import deque


def day10(my_input):
    lista = [list(x) for x in my_input.strip().split('\n')]
    lista = [[int(x) for x in y] for y in lista]

    zeros = []
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j] == 0:
                zeros.append((i, j, 0))

    score = 0
    unique_paths = set()
    for zero in zeros:
        vis = set()
        deq = deque()
        i, j, l = zero
        path = set((i, j))
        deq.append((i, j, l, path))
        while deq:
            i, j, l, path = deq.popleft()
            value = lista[i][j]
            if value == 9:
                vis.add((i, j))
                unique_paths.add(frozenset(path))
                continue
            if i < 0 or i >= len(lista) or j < 0 or j >= len(lista[i]):
                continue
            if i - 1 >= 0:
                if lista[i-1][j] == value + 1:
                    new_path = path.copy() 
                    new_path.add((i-1, j))
                    deq.append((i-1, j, l+1, new_path))
            if i + 1 < len(lista):
                if lista[i+1][j] == value + 1:
                    new_path = path.copy()
                    new_path.add((i+1, j))
                    deq.append((i+1, j, l+1, new_path))
            if j - 1 >= 0:
                if lista[i][j-1] == value + 1:
                    new_path = path.copy()
                    new_path.add((i, j-1))
                    deq.append((i, j-1, l+1, new_path))
            if j + 1 < len(lista[i]):
                if lista[i][j+1] == value + 1:
                    new_path = path.copy()
                    new_path.add((i, j+1))
                    deq.append((i, j+1, l+1, new_path))

        score += len(vis)

    return score, len(unique_paths)


sample_input = """0123
1234
8765
9876"""

sample_input_2 = """1190119
1111198
1112117
6543456
7651987
8761111
9871111"""

sample_input_3 = """012345
123456
234567
345678
416789
567891"""

sample_input_4 = """1111101
1143211
1151121
1165431
1171141
1187651
1191111"""

sample_input_5 = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

my_input = open(r"2024/inputs/Day_10.txt").read()

# Tests
assert day10(sample_input)[0] == 1
assert day10(sample_input_2)[0] == 4
assert day10(sample_input_5)[0] == 36
assert day10(sample_input_3)[1] == 227
assert day10(sample_input_4)[1] == 4
assert day10(sample_input_5)[1] == 81

# Results
print(day10(my_input))
