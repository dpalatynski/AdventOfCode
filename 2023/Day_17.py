# Day 17
from heapq import heappop, heappush


def inr(pos, arr):
	return pos[0] in range(len(arr)) and pos[1] in range(len(arr[0]))


def day17(my_input, mindist, maxdist):
	ll = [[int(y) for y in x] for x in my_input.strip().split('\n')]
	neighbours = [(0, 1), (1, 0), (0, -1), (-1, 0)]

	q = [(0, 0, 0, -1)]
	seen = set()
	costs = {}
	while q:
		cost, x, y, dd = heappop(q)
		if x == len(ll) - 1 and y == len(ll[0]) - 1:
			return cost
		if (x, y, dd) in seen:
			continue
		seen.add((x, y, dd))
		for direction in range(4):
			costincrease = 0
			if direction == dd or (direction + 2) % 4 == dd:
				continue
			for distance in range(1, maxdist + 1):
				xx = x + neighbours[direction][0] * distance
				yy = y + neighbours[direction][1] * distance
				if inr((xx, yy), ll):
					costincrease += ll[xx][yy]
					if distance < mindist:
						continue
					nc = cost + costincrease
					if costs.get((xx, yy, direction), 1e100) <= nc:
						continue
					costs[(xx, yy, direction)] = nc
					heappush(q, (nc, xx, yy, direction))


sample_input = '''2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533'''


sample_input_2 = '''111111111111
999999999991
999999999991
999999999991
999999999991'''


# Tests
assert(day17(sample_input, 1, 3) == 102)
assert(day17(sample_input, 4, 10) == 94)
assert(day17(sample_input_2, 4, 10) == 71)


# Results
my_input = open(r"2023/inputs/Day_17.txt").read()
print(day17(my_input, 1, 3))
print(day17(my_input, 4, 10))
