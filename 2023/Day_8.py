# Day 8 

from math import gcd

sample_input = '''RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)'''

sample_input_2 = '''LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)'''

sample_input_3 = '''LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)'''


def day8_part1(my_input):
    instructions = my_input.split('\n\n')[0]
    nodes = my_input.split('\n\n')[1].split('\n')
    elements = {}
    for node in nodes:
        elements[node.split(' =')[0]] = (node.split(' =')[1][2:5], node.split(' =')[1][7:10])

    current_node = 'AAA'
    steps = 0
    while current_node != 'ZZZ':
        for ins in instructions:
            if ins == 'R' and current_node != 'ZZZ':
                current_node = elements[current_node][1]
                steps += 1
            elif ins == 'L' and current_node != 'ZZZ':
                current_node = elements[current_node][0]
                steps += 1
        
    return steps


def day8_part2(my_input):
    instructions = my_input.split('\n\n')[0]
    nodes = my_input.split('\n\n')[1].split('\n')
    elements = {}
    for node in nodes:
        elements[node.split(' =')[0]] = (node.split(' =')[1][2:5], node.split(' =')[1][7:10])

    starting_nodes = []
    for key in elements.keys():
        if key[-1] == 'A':
            starting_nodes.append(key)

    n_steps = []
    for node in starting_nodes:
        current_node = node
        steps = 0
        while current_node[-1] != 'Z':
            for ins in instructions:
                if ins == 'R' and current_node[-1] != 'Z':
                    current_node = elements[current_node][1]
                    steps += 1
                elif ins == 'L' and current_node[-1] != 'Z':
                    current_node = elements[current_node][0]
                    steps += 1
            
            #print(current_node)
        n_steps.append(steps)

    lcm = 1
    for i in n_steps:
        lcm = lcm*i//gcd(lcm, i)

    return lcm


# Tests
assert day8_part1(sample_input) == 2
assert day8_part1(sample_input_2) == 6
assert day8_part2(sample_input_3) == 6


# Results
my_input = open(r"2023/inputs/Day_8.txt").read()
print(day8_part1(my_input))
print(day8_part2(my_input))
