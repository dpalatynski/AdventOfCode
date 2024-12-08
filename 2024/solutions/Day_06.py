# Day 6


def day6_part1(my_input):
    array = [list(x) for x in my_input.strip().split('\n')]
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == '^':
                starting_point = (i, j)

    i, j = starting_point
    visited = set()
    visited.add((i, j))
    while True:
        current_position = array[i][j]
        if current_position == '^':
            if i - 1 < 0:
                break
            elif array[i - 1][j] == '#':
                array[i][j] = '>'
            else:
                array[i][j] = '.'
                i, j = i - 1, j
                visited.add((i, j))
                array[i][j] = '^'
        elif current_position == '>':
            if j + 1 >= len(array[0]):
                break
            elif array[i][j + 1] == '#':
                array[i][j] = 'v'
            else:
                array[i][j] = '.'
                i, j = i, j + 1
                visited.add((i, j))
                array[i][j] = '>'
        elif current_position == 'v':
            if i + 1 >= len(array):
                break
            elif array[i+1][j] == '#':
                array[i][j] = '<'
            else:
                array[i][j] = '.'
                i, j = i + 1, j
                visited.add((i, j))
                array[i][j] = 'v'
        elif current_position == '<':
            if j - 1 < 0:
                break
            elif array[i][j - 1] == '#':
                array[i][j] = '^'
            else:
                array[i][j] = '.'
                i, j = i, j - 1
                visited.add((i, j))
                array[i][j] = '<'

        if i == -1 or j == -1 or i == len(array) or j == len(array[0]):
            break

    return len(visited), visited

def day6_part2(my_input):
    already_visited = day6_part1(my_input)[1]

    array = [list(x) for x in my_input.strip().split('\n')]
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == '^':
                starting_point = (i, j)

    indices = []
    loops = 0
    for k in range(len(array)):
        for l in range(len(array[i])):
            if array[k][l] == '.' and (k, l) in already_visited:
                indices.append((k, l))

    for index in indices:
        array = [list(x) for x in my_input.strip().split('\n')]
        array[index[0]][index[1]] = '#'

        i, j = starting_point
        visited = set()
        visited.add((i, j, '^'))     
        while True:
            current_position = array[i][j]
            if current_position == '^':
                if i - 1 < 0:
                    break
                elif array[i - 1][j] == '#':
                    array[i][j] = '>'
                else:
                    array[i][j] = '.'
                    i, j = i - 1, j
                    if (i, j, '^') in visited:
                        loops += 1
                        break
                    else:
                        visited.add((i, j, '^'))
                        array[i][j] = '^'
            elif current_position == '>':
                if j + 1 >= len(array[0]):
                    break
                elif array[i][j + 1] == '#':
                    array[i][j] = 'v'
                else:
                    array[i][j] = '.'
                    i, j = i, j + 1
                    if (i, j, '>') in visited:
                        loops += 1
                        break
                    else:
                        visited.add((i, j, '>'))
                        array[i][j] = '>'
            elif current_position == 'v':
                if i + 1 >= len(array):
                    break
                elif array[i+1][j] == '#':
                    array[i][j] = '<'
                else:
                    array[i][j] = '.'
                    i, j = i + 1, j
                    if (i, j, 'v') in visited:
                        loops += 1
                        break
                    else:
                        visited.add((i, j, 'v'))
                        array[i][j] = 'v'
            elif current_position == '<':
                if j - 1 < 0:
                    break
                elif array[i][j - 1] == '#':
                    array[i][j] = '^'
                else:
                    array[i][j] = '.'
                    i, j = i, j - 1
                    if (i, j, '<') in visited:
                        loops += 1
                        break
                    else:
                        visited.add((i, j, '<'))
                        array[i][j] = '<'

            if i == -1 or j == -1 or i == len(array) or j == len(array[0]):
                break

    return loops


sample_input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

my_input = open(r"2024/inputs/Day_06.txt").read()

# Tests
assert day6_part1(sample_input)[0] == 41
assert day6_part2(sample_input) == 6

# Results
print(day6_part1(my_input)[0])
print(day6_part2(my_input))
