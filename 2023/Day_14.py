# Day 14


def rotate_matrix_right(m):
    return [[m[j][i] for j in range(len(m)-1,-1,-1)] for i in range(len(m[0]))]


def rotate_matrix_left(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]


def tilt(pattern):
    for line in pattern:
        for i in range(len(line)):
            if line[i] == '.':             
                for j in range(i+1, len(line)):   
                    if line[i] == '.' and line[j] == 'O':
                        line[i] = 'O'
                        line[j] = '.'
                    elif line[j] == '#':
                        i = j-1
                        break

    return pattern


def cycle(pattern):
    for _ in range(4):
        pattern = tilt(pattern)
        pattern = rotate_matrix_right(pattern)

    return pattern


def load(pattern):
    total = 0
    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
            if pattern[i][j] == 'O':
                total += len(pattern[0]) - j

    return total


def day14(my_input):
    pattern = [list(line) for line in my_input.split('\n')]
    pattern = rotate_matrix_left(pattern)
    part1 = load(tilt(pattern))

    t = 0
    seen = {}
    run = True
    cycles = 1000000000
    while t < cycles:
        pattern = cycle(pattern)
        t += 1
        h = str(pattern)
        if h in seen and run == True:
            period = t - seen[h]
            t += ((cycles-t)//period)*period
            run = False

        seen[h] = t

    return part1, load(pattern)


sample_input = '''O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....'''


# Tests
assert day14(sample_input) == (136, 64)


# Results
my_input = open(r"2023/inputs/Day_14.txt").read()
print(day14(my_input))
