# Day 6

sample_input = '''Time:      7  15   30
Distance:  9  40  200'''


def day6(my_input, part=None):
    if part: # part 2
        time = [int(''.join(my_input.split('\n')[0].split(': ')[1].split(' ')))]
        distance = [int(''.join(my_input.split('\n')[1].split(': ')[1].split(' ')))]
    else: # part 1
        time = my_input.split('\n')[0].split(': ')[1].split(' ')
        distance = my_input.split('\n')[1].split(': ')[1].split(' ')
        time = [int(x) for x in time if x != '']
        distance = [int(x) for x in distance if x != '']

    result = 1
    for i in range(len(time)):
        scores = []
        for j in range(time[i]+1):
            speed = 1*j
            score = speed * (time[i] - j)
            scores.append(score)

        scores = [dist for dist in scores if dist > distance[i]]
        result *= len(scores)

    return result


# Tests
assert day6(sample_input) == 288
assert day6(sample_input, 2) == 71503


# Results
my_input = open(r"2023/inputs/Day_06.txt").read()
print(day6(my_input))
print(day6(my_input, 2))
