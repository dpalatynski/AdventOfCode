# Day 15


def hash(word):
    current = 0
    for char in word:
        current += ord(char)
        current *= 17
        current = current % 256

    return current


def calculate_focusing_power(boxes):
    s = 0
    for i in range(len(boxes)):
        for j in range(len(boxes[i])):
            s += (i+1) * (j+1) * int(boxes[i][j].split(' ')[1])

    return s


def day15_part1(my_input):
    return sum([hash(step) for step in my_input.split(',')])


def day15_part2(my_input):
    boxes =  [[] for i in range(256)]
    for step in my_input.split(','):
        label = step.split('=')[0].split('-')[0]
        box = hash(label)
        if '=' in step:
            cand = [elem for elem in boxes[box] if elem.split(' ')[0] == label]
            if cand != []:
                boxes[box][boxes[box].index(cand[0])] = step.replace('=', ' ')
            else:
                boxes[box].append(step.replace('=', ' '))
        elif '-' in step:
            cand = [elem for elem in boxes[box] if elem.split(' ')[0] == label]
            if cand != []:
                for c in cand:
                    boxes[box].remove(c)

    return calculate_focusing_power(boxes)


sample_input = '''rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'''


# Tests
assert day15_part1(sample_input) == 1320
assert day15_part2(sample_input) == 145


# Results
my_input = open(r"2023/inputs/Day_15.txt").read()
print(day15_part1(my_input))
print(day15_part2(my_input))
