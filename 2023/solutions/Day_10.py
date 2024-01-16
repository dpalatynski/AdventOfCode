# Day 10
from collections import defaultdict, deque


def day10_part1(my_input):
    tiles = [tile for tile in my_input.split('\n')]

    adj = {}
    for i, row in enumerate(tiles):
        for j, cell in enumerate(row):
            neighbors = []
            if cell == "|":
                neighbors = [(i-1, j), (i+1, j)]
            elif cell == "-":
                neighbors = [(i, j-1), (i, j+1)]
            elif cell == "L":
                neighbors = [(i-1, j), (i, j+1)]
            elif cell == "J":
                neighbors = [(i-1, j), (i, j-1)]
            elif cell == "7":
                neighbors = [(i+1, j), (i, j-1)]
            elif cell == "F":
                neighbors = [(i+1, j), (i, j+1)]
            elif cell == "S":
                start = (i, j)
            for x, y in neighbors:
                if x >= 0 and x < len(tiles) and y >= 0 and y < len(row):
                    if (i, j) not in adj:
                        adj[(i, j)] = [(x, y)]
                    else:
                        adj[(i, j)].append((x, y))

    adj_start = []
    for vert in adj:
        for vert2 in adj[vert]:
            if vert2 == start:
                adj_start.append(vert)
    adj[start] = adj_start


    dst = defaultdict(lambda: -1)
    bfs_q = deque()
    bfs_q.append(start)
    dst[start] = 0
    ans = (0, start)
    while len(bfs_q) > 0:
        curcell = bfs_q.popleft()
        for nxt in adj[curcell]:
            if dst[nxt] == -1:
                dst[nxt] = dst[curcell] + 1
                ans = max(ans, (dst[nxt], nxt))
                bfs_q.append(nxt)
    
    return ans[0]


def day10_part2(my_input):
    tiles = [tile for tile in my_input.split('\n')]

    adj = defaultdict(list)
    for i, row in enumerate(tiles):
        for j, cell in enumerate(row):
            neighbors = []
            if cell == "|":
                neighbors = [(2*i-1, 2*j), (2*i+1, 2*j)]
            elif cell == "-":
                neighbors = [(2*i, 2*j-1), (2*i, 2*j+1)]
            elif cell == "L":
                neighbors = [(2*i-1, 2*j), (2*i, 2*j+1)]
            elif cell == "J":
                neighbors = [(2*i-1, 2*j), (2*i, 2*j-1)]
            elif cell == "7":
                neighbors = [(2*i+1, 2*j), (2*i, 2*j-1)]
            elif cell == "F":
                neighbors = [(2*i+1, 2*j), (2*i, 2*j+1)]
            elif cell == "S":
                start = (2*i, 2*j)
            for x, y in neighbors:
                if x >= 0 and x < 2*len(tiles) and y >= 0 and y < 2*len(row):
                    adj[(2*i, 2*j)].append((x, y))

    for i, row in enumerate(tiles):
        for j, cell in enumerate(row):
            xs = []
            if i > 0: xs.append(2*i-1)
            if i+1 < len(tiles): xs.append(2*i+1)
            ys = []
            if j > 0: ys.append(2*j-1)
            if j+1 < len(row): ys.append(2*j+1)
            for nx in xs:
                adj[(nx, 2*j)].append((2*i, 2*j))
            for ny in ys:
                adj[(2*i, ny)].append((2*i, 2*j))
                
    inv_start = []
    indeg = defaultdict(int)
    for vert in adj:
        for vert2 in adj[vert]:
            indeg[vert2] += 1
            if vert2 == start:
                inv_start.append(vert)
    for vert in inv_start:
        if indeg[vert] > 0:
            adj[start].append(vert)

    dst = defaultdict(lambda: 1000000000)
    bfs_q = deque()
    bfs_q.append(start)
    dst[start] = 0
    ans = (0, start)
    inloop = set()
    while len(bfs_q) > 0:
        curcell = bfs_q.popleft()
        inloop.add(curcell)
        for nxt in adj[curcell]:
            if dst[nxt] == 1000000000:
                dst[nxt] = dst[curcell] + 1
                ans = max(ans, (dst[nxt], nxt))
                bfs_q.append(nxt)

    ans2 = 0
    vis = set()
    for i, row in enumerate(tiles):
        for j, cell in enumerate(row):
            if (2*i, 2*j) in inloop or (2*i, 2*j) in vis:
                continue
            added_to_q = set()
            cur_q = deque()
            cur_q.append((2*i, 2*j))
            added_to_q.add((2*i, 2*j))
            enclosed = True
            while len(cur_q) > 0:
                cx, cy = cur_q.popleft()
                for nx, ny in [(cx-1, cy), (cx+1, cy), (cx, cy-1), (cx, cy+1)]:
                    if (nx, ny) in inloop or (nx, ny) in added_to_q:
                        continue
                    assert((nx, ny) not in vis)
                    if nx < 0 or nx >= 2*len(tiles) or ny < 0 or ny >= 2*len(row):
                        enclosed = False
                        continue
                    cur_q.append((nx, ny))
                    added_to_q.add((nx, ny))
            for c in added_to_q:
                if c[0] % 2 == 0 and c[1] % 2 == 0 and enclosed:
                    ans2 += 1
                vis.add(c)

    return ans2


sample_input_1 = '''-L|F7
7S-7|
L|7||
-L-J|
L|-JF'''


sample_input_2 = '''7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ'''


sample_input_3 = '''...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........'''


sample_input_4 = '''..........
.S------7.
.|F----7|.
.||OOOO||.
.||OOOO||.
.|L-7F-J|.
.|II||II|.
.L--JL--J.
..........'''


sample_input_5 = '''.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...'''


sample_input_6 = '''FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L'''


# Tests
assert day10_part1(sample_input_1) == 4
assert day10_part1(sample_input_2) == 8
assert day10_part2(sample_input_3) == 4
assert day10_part2(sample_input_4) == 4
assert day10_part2(sample_input_5) == 8
assert day10_part2(sample_input_6) == 10


# Results
my_input = open(r"2023/inputs/Day_10.txt").read()
print(day10_part1(my_input))
print(day10_part2(my_input))
