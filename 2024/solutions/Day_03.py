# Day 3
import re


def day3_part1(my_input): # Rank 392 in 00:02:37 :)
    x = re.findall(r"mul\((\d+),(\d+)\)", my_input)
    return sum(int(i[0]) * int(i[1]) for i in x)

def day3_part2(my_input):
    enabled = True
    total_sum = 0
    pos = 0
    while pos < len(my_input):
        if re.compile(r"do\(\)").match(my_input, pos):
            enabled = True
            pos += len("do()")
        elif re.compile(r"don't\(\)").match(my_input, pos):
            enabled = False
            pos += len("don't()")
        else:
            mul_match = re.compile(r"mul\((\d+),(\d+)\)").match(my_input, pos)
            if mul_match and enabled:
                x, y = int(mul_match.group(1)), int(mul_match.group(2))
                total_sum += x * y
            pos += 1
    
    return total_sum


sample_input_1 = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
sample_input_2 = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""

my_input = open(r"2024/inputs/Day_03.txt").read()

# Tests
assert day3_part1(sample_input_1) == 161
assert day3_part2(sample_input_2) == 48

# Results
print(day3_part1(my_input))
print(day3_part2(my_input))