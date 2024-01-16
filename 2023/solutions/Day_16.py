# Day 16
from collections import deque


def track(contraption, i, j, si, sj):
    visited = set()
    q = deque([(i, j, si, sj)])
    while q:
        i, j, si, sj = q.pop()
        assert abs(si + sj) == 1 # always moving
        i, j = i+si, j+sj
        if (i, j, si, sj) in visited:
            continue
        if i < 0 or i >= len(contraption[0]) or j < 0 or j >= len(contraption):
            continue
        visited.add((i, j, si, sj))
        if contraption[i][j] == '.':
            q.append((i, j, si, sj))
        if contraption[i][j] == '|':
            if si == 0:  # right/left on the same level,  -> | <-
                q.append((i, j, -1, 0))
                q.append((i, j, 1, 0))
            if abs(si) == 1:  # pass through
                q.append((i, j, si, sj)) 
        if contraption[i][j] == '-':
            if sj == 0:  # top/down in the same column
                q.append((i, j, 0, -1))
                q.append((i, j, 0, 1))
            if abs(sj) == 1:  # pass through
                q.append((i, j, si, sj))
        if contraption[i][j] == '\\':
            if si == 0 and sj == 1: # -> \
                q.append((i, j, 1, 0))
            if si == 0 and sj == -1: # \ <-
                q.append((i, j, -1, 0))
            if si == -1 and sj == 0: # <- \
                q.append((i, j, 0, -1))
            if si == 1 and sj == 0: # \ ->
                q.append((i, j, 0, 1))
        if contraption[i][j] == '/':
            if si == 0 and sj == 1: # -> /
                q.append((i, j, -1, 0))
            if si == 0 and sj == -1: # / <-
                q.append((i, j, 1, 0))
            if si == 1 and sj == 0: # <- /
                q.append((i, j, 0, -1))
            if si == -1 and sj == 0: # / ->
                q.append((i, j, 0, 1))

    l = set()
    for vis in visited:
        l.add((vis[0], vis[1]))

    return len(l)


def day16(my_input):
    contraption = [list(line) for line in my_input.split('\n')]

    best = []
    for x in range(len(contraption)):
        best.append(track(contraption, x, -1, 0, 1))
        best.append(track(contraption, x, len(contraption), 0, -1))
        best.append(track(contraption, -1, x, 1, 0))
        best.append(track(contraption, len(contraption), x, -1, 0))

    return best[0], max(best)


sample_input = r'''.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....'''


# Tests
assert day16(sample_input) == (46, 51)


# Results
my_input = open(r"2023/inputs/Day_16.txt").read()
print(day16(my_input))
