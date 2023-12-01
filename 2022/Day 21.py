def part1(puzzle):
    calculations = [(monkey.split(': ')[0], monkey.split(': ')[1]) for monkey in puzzle.split('\n')]
    results = {}

    for calculation in calculations:
        if len(calculation[1].split(' ')) == 1:
            results[calculation[0]] = int(calculation[1])

    while 'root' not in results:
        for calculation in calculations:
            if calculation[0] in results:
                continue
            else:
                a, op, b = calculation[1].split(' ')
                if a in results and b in results:
                    results[calculation[0]] = int(eval(str(results[a]) + op + str(results[b])))

    return results['root']


sample_input = open("Day 21.txt").read().split('\n\n\n')[0]
assert part1(sample_input) == 152

puzzle_input = open("Day 21.txt").read().split('\n\n\n')[1]
print(part1(puzzle_input))
