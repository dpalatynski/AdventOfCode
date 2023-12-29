# Day 7
from collections import Counter
from itertools import product


def score(hand, vals):
	counts = Counter(hand)

	# 5 of a kind
	if len(counts) == 1:
		return (7, *map(vals.get, hand))

	if len(counts) == 2:
		# 4 of a kind
		if 4 in counts.values():
			return (6, *map(vals.get, hand))
		# full house
		return (5, *map(vals.get, hand))

	if len(counts) == 3:
		# tris AAAxx
		if 3 in counts.values():
			return (4, *map(vals.get, hand))

		# 2 pair AABBx
		if 2 in counts.values():
			return (3, *map(vals.get, hand))

	# pair AAxyz
	if len(counts) == 4:
		return (2, *map(vals.get, hand))

	return (0, *map(vals.get, hand))


def day7_part1(my_input):
    hands = {}
    ans = 0
	
    for hand, bet in map(str.split, my_input.split('\n')):
        hands[hand] = int(bet)

    ordered = sorted(hands.items(), key=lambda hb: score(hb[0], values))

    for i, (h, b) in enumerate(ordered, 1):
        ans += i * b

    return ans

def day7_part2(my_input):
	lines = my_input.split('\n')
	hands = {}
	ans = 0

	for hand, bet in map(str.split, lines):
		assert hand not in hands
		hands[hand] = int(bet)

	ordered = sorted(hands.items(), key=lambda hb: score2(hb[0], values))

	for i, (h, b) in enumerate(ordered, 1):
		ans += i * b

	return ans


def score2(hand, vals):
    if 'J' not in hand:
        return list(score(hand, values2))

    js = []
    for i, c in enumerate(hand):
        if c == 'J':
            js.append(i)

    hand = [*hand]
    best = [-1]

    for x in product(*(['AKQT98765432'] * len(js))):
        for i, v in zip(js, x):
            hand[i] = v

        s = list(score(hand, values2))
        for i in js:
            s[i + 1] = values2['J']

        best = max(best, s)

    return best

values = {
	'A': 12 - 0,
	'K': 12 - 1,
	'Q': 12 - 2,
	'J': 12 - 3,
	'T': 12 - 4,
	'9': 12 - 5,
	'8': 12 - 6,
	'7': 12 - 7,
	'6': 12 - 8,
	'5': 12 - 9,
	'4': 12 - 10,
	'3': 12 - 11,
	'2': 12 - 12,
}

values2 = {
	'A': 12 - 0,
	'K': 12 - 1,
	'Q': 12 - 2,
	'T': 12 - 3,
	'9': 12 - 4,
	'8': 12 - 5,
	'7': 12 - 6,
	'6': 12 - 7,
	'5': 12 - 8,
	'4': 12 - 9,
	'3': 12 - 10,
	'2': 12 - 11,
	'J': 12 - 12,
}


sample_input = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483'''


# Tests
assert(day7_part1(sample_input) == 6440)
assert(day7_part2(sample_input) == 5905)


# Results
my_input = open(r"2023/inputs/Day_07.txt").read()
print(day7_part1(my_input))
print(day7_part2(my_input))
