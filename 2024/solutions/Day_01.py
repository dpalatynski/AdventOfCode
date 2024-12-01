# Day 1


def day1(my_input):
    lines = my_input.strip().split('\n')
    lines = [(int(line.split('   ')[0]), int(line.split('   ')[1])) for line in lines]
    left = sorted([line[0] for line in lines])
    right = sorted([line[1] for line in lines])

    elements = {}
    for item in set(left):
        elements[item] = right.count(item)

    sum1 = 0
    for item in left:
        sum1 += item * elements[item] if elements[item] != 0 else 0

    return sum(abs(l - r) for l, r in zip(left, right)), sum1


sample_input = '''3   4
4   3
2   5
1   3
3   9
3   3'''

my_input = open(r"2024/inputs/Day_01.txt").read()

# Tests
assert day1(sample_input) == (11, 31)

# Results
print(day1(my_input))
