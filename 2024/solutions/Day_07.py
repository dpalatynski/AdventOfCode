# Day 7
from itertools import product


def day7_part1(my_input):
    lista = [x.split(' ') for x in my_input.strip().replace(':', '').split('\n')]

    combinations = [list(product('*+', repeat=(len(el) - 2))) for el in lista]
    sum = 0
    for i in range(len(lista)):
        res = int(lista[i][0])
        skl = [int(x) for x in lista[i][1:]]
        for comb in combinations[i]:
            curr = skl[0]
            for j in range(1, len(skl)):
                if comb[j-1] == '+':
                    curr += skl[j]
                elif comb[j-1] == '*':
                    curr *= skl[j]
                  
            if res == curr:
                sum += curr
                break

    return sum

def day7_part2(my_input):
    lista = [x.split(' ') for x in my_input.strip().replace(':', '').split('\n')]
    combinations = [list(product('*+|', repeat=(len(el) - 2))) for el in lista]
    sum = 0
    for i in range(len(lista)):
        res = int(lista[i][0])
        skl = [int(x) for x in lista[i][1:]]
        for comb in combinations[i]:
            curr = skl[0]
            join = ''
            for j in range(1, len(skl)):
                if comb[j-1] == '+':
                    curr += skl[j] if join == '' else int(join + str(skl[j]))
                elif comb[j-1] == '*':
                    curr *= skl[j] if join == '' else int(join + str(skl[j]))
                elif comb[j-1] == '|':
                    curr = int(str(curr) + str(skl[j]))

            if res == curr:
                sum += curr
                break

    return sum


sample_input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

my_input = open(r"2024/inputs/Day_07.txt").read()

# Tests
assert day7_part1(sample_input) == 3749
assert day7_part2(sample_input) == 11387

# Results
print(day7_part1(my_input))
print(day7_part2(my_input))
