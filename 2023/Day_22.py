# Day 22
import re
from collections import defaultdict


def ints(s):
	return list(map(int, re.findall(r'\d+', s)))


def down(brick):
	return (brick[0], brick[1], brick[2] - 1, brick[3], brick[4], brick[5] - 1, brick[6])


def positions(brick):
	for x in range(brick[0], brick[3] + 1):
		for y in range(brick[1], brick[4] + 1):
			for z in range(brick[2], brick[5] + 1):
				yield (x,y,z)


def whatif(disintegrated, above, below):
	falling = set()
	def falls(brick):
		if brick in falling:
			return
		falling.add(brick)
		for parent in above[brick]:
			if not len(below[parent] - falling):
				# if everything below the parent is falling, so is the parent
				falls(parent)
	falls(disintegrated)
	return len(falling)


def day22(my_input):
	ll = [tuple(ints(x) + [i]) for i, x in enumerate(my_input.split('\n'))]

	occupied = {}
	fallen = []

	for brick in sorted(ll, key=lambda brick: brick[2]):
		while True:
			nxt = down(brick)
			if not any(pos in occupied for pos in positions(nxt)) and nxt[2] > 0:
				brick = nxt
			else:
				for pos in positions(brick):
					occupied[pos] = brick
				fallen.append(brick)
				break

	above = defaultdict(set)
	below = defaultdict(set)
	for brick in fallen:
		inthisbrick = set(positions(brick))
		for pos in positions(down(brick)):
			if pos in occupied and pos not in inthisbrick:
				above[occupied[pos]].add(brick)
				below[brick].add(occupied[pos])

	p1 = 0
	p2 = 0
	for brick in fallen:
		wouldfall = whatif(brick,  above, below)
		p1 += wouldfall == 1
		p2 += wouldfall - 1

	return p1, p2


sample_input = '''1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9'''


# Test
assert(day22(sample_input) == (5, 7))


# Results
my_input = open(r"2023/inputs/Day_22.txt").read()
print(day22(my_input))
