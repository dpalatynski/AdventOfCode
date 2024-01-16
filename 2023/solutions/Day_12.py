# Day 12
from itertools import combinations
from functools import lru_cache


def validate(row, pattern):
    dd = row.split('.')
    ddd = [dddd for dddd in dd if dddd != '']
    dddd = [len(ddddd) for ddddd in ddd]
    
    return dddd == [int(i) for i in pattern.split(',')]


@lru_cache
def search(l, lengths, i, curlen):
	if i == len(l):
		return not lengths and curlen == 0 or len(lengths) == 1 and lengths[0] == curlen

	total = 0

	# broken
	if l[i] == '#':
		# cur chunk is 1 longer, advance
		total += search(l, lengths, i + 1, curlen + 1)

	# not broken
	elif l[i] in '.':
		# cannot have chunk here, start new chunk later
		if not curlen:
			# we had no previous chunk
			total += search(l, lengths, i + 1, 0)
		elif lengths and lengths[0] == curlen:
			# previous chunk completed
			total += search(l, lengths[1:], i + 1, 0)

	# unknown
	else:
		# put '#' here
		total += search(l, lengths, i + 1, curlen + 1)

		# put '.' here, start new chunk
		if not curlen:
			# we had no previous chunk
			total += search(l, lengths, i + 1, 0)
		elif lengths and lengths[0] == curlen:
			# previous chunk completed
			total += search(l, lengths[1:], i + 1, 0)

	return total


def day12_part1(my_input):
    lines = my_input.split('\n')
    counter = 0
    for line in lines:
        x = line.split(' ')
        maxx = sum([int(i) for i in x[1].split(',')])
        indexes = [k for k in range(len(x[0])) if x[0][k] == '?']
        to_fill = maxx - x[0].count('#')
        T = [*map(list, [i for i in combinations(indexes, to_fill)])]
        row = list(x[0])
        for i in T:
            row = list(x[0])
            for j in i:
                row[j] = '#'
            
            if validate(''.join(row).replace('?', '.'), x[1]):
                counter += 1

    return counter


def day12_part2(my_input):
	lines = my_input.split('\n')

	ans2 = 0
	for k, line in enumerate(lines):
		modified_x0 = line.split(' ')[0]
		modified_x1 = line.split(' ')[1]

		modified_x1 = tuple([int(i) for i in modified_x1.split(',')]*5)
		modified_x0 = '?'.join([modified_x0] * 5)

		ans2 += search(modified_x0, modified_x1, 0, 0)
		search.cache_clear()

	return ans2


sample_input = '''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1'''


# Tests
assert day12_part1(sample_input) == 21
assert day12_part2(sample_input) == 525152


# Results
my_input = open(r"2023/inputs/Day_12.txt").read()
print(day12_part1(my_input))
print(day12_part2(my_input))
