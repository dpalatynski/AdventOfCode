def day23(my_input, part):
    data = my_input.split('\n')
    edges = {}
    for r, row in enumerate(data):
        for c, v in enumerate(row):
            if part == 2:
                if v in ".<>v^":
                    for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                        ar, ac = r + dr, c + dc
                        if not (0 <= ar < len(data) and 0 <= ac < len(row)):
                            continue
                        if data[ar][ac] in '.<>v^':
                            edges.setdefault((r, c), set()).add((ar, ac))
                            edges.setdefault((ar, ac), set()).add((r, c))
            elif part == 1:
                if v == ".":
                    for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                        ar, ac = r + dr, c + dc
                        if not (0 <= ar < len(data) and 0 <= ac < len(row)):
                            continue
                        if data[ar][ac] == ".":
                            edges.setdefault((r, c), set()).add((ar, ac))
                            edges.setdefault((ar, ac), set()).add((r, c))
                if v == ">":
                    edges.setdefault((r, c), set()).add((r, c + 1))
                    edges.setdefault((r, c - 1), set()).add((r, c))
                if v == "v":
                    edges.setdefault((r, c), set()).add((r + 1, c))
                    edges.setdefault((r - 1, c), set()).add((r, c))

    n, m = len(data), len(data[0])

    q = [(0, 1, 0)]
    visited = set()
    best = 0
    while q:
        r, c, d = q.pop()
        if d == -1:
            visited.remove((r, c))
            continue
        if (r, c) == (n - 1, m - 2):
            best = max(best, d)
            continue
        if (r, c) in visited:
            continue
        visited.add((r, c))
        q.append((r, c, -1))
        for ar, ac in edges[(r, c)]:
            q.append((ar, ac, d + 1))

    return best


sample_input = '''#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#'''


# Test
assert(day23(sample_input, 1) == 94)
assert(day23(sample_input, 2) == 154)


# Results
my_input = open(r"2023/inputs/Day_23.txt").read()
print(day23(my_input, 1))
print(day23(my_input, 2))

