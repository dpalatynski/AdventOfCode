# Day 9
import numpy as np


def day9(my_input, reverse=False):
    all_history = my_input.split('\n')

    history = []
    for i in range(len(all_history)):
        history.append([int(x) for x in my_input.split('\n')[i].split(' ')])

    li = []
    for hi in history:
        temp = hi[:] if not reverse else hi[::-1]
        result = [temp]
        while not all(v==0 for v in result[-1]):
            result.append(list(np.diff(temp)))
            temp = result[-1]

        for i in range(len(result), 0, -1):
            if i == len(result):
                result[i-1].append(0)
            else:
                result[i-1].append(result[i-1][-1]+result[i][-1])
        li.append(result[i-1][-1])

    return sum(li)


sample_input = '''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45'''


# Tests
assert day9(sample_input) == 114
assert day9(sample_input, reverse=True) == 2


# Results
my_input = open(r"2023/inputs/Day_9.txt").read()
print(day9(my_input))
print(day9(my_input, reverse=True))
   