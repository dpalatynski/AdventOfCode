# Day 1

sample_inputs = ['+1, +1, +1', '+1, +1, -2', '-1, -2, -3']
sample_inputs_2 = ['+1, -1', '+3, +3, +4, -2, -4', '-6, +3, +8, +5, -6', '+7, +7, -2, -7, -4']
my_input = open(r"2018/inputs/Day_01.txt").read().replace('\n', ',')

def day1_part1(sample_input):
    return sum([int(x.replace('+', '')) for x in sample_input.split(',')])

def day1_part2(sample_input):
    modified_input = [int(x.replace('+', '')) for x in sample_input.split(',')]
    frequencies = {0}
    i, frequency = 1, 0
    while True:
        frequency += modified_input[i%len(modified_input)-1]
        i += 1
        if frequency in frequencies:
            return frequency
        frequencies.add(frequency)

results = [3, 0 , -6]
for i in range(3):
    assert day1_part1(sample_inputs[i]) == results[i]

results_2 = [0, 10, 5, 14]
for i in range(3):
    assert day1_part2(sample_inputs_2[i]) == results_2[i]

print(day1_part1(my_input))
print(day1_part2(my_input))
