# Day 4
import numpy as np


def day4_part1(my_input):
    lista = my_input.strip().split('\n')

    horizontal = ' '.join(lista)
    vertical = ' '.join([''.join(x) for x in zip(*lista)])
    horizontal_reversed = horizontal[::-1]
    vertical_reversed = vertical[::-1]

    diagonal_left_right = ''
    for i in range(len(lista)):
        diagonal_left_right += ''.join([lista[j][i+j] for j in range(len(lista)) if i+j < len(lista)]) + ' '
    for i in range(1, len(lista)):
        diagonal_left_right += ''.join([lista[j+i][j] for j in range(len(lista)) if j+i < len(lista)]) + ' '

    diagonal_right_left = ''
    for i in range(len(lista)):
        diagonal_right_left += ''.join([lista[j][i-j] for j in range(len(lista)) if i-j >= 0]) + ' '
    for i in range(1, len(lista)):
        diagonal_right_left += ''.join([lista[j+i][len(lista)-j-1] for j in range(len(lista)) if i+j < len(lista)]) + ' '

    diagonal_left_right_reversed = diagonal_left_right[::-1]
    diagonal_right_left_reversed = diagonal_right_left[::-1]

    return horizontal.count('XMAS') + \
    vertical.count('XMAS') + \
    horizontal_reversed.count('XMAS') + \
    vertical_reversed.count('XMAS') + \
    diagonal_left_right.count('XMAS') + \
    diagonal_right_left.count('XMAS') + \
    diagonal_left_right_reversed.count('XMAS') + \
    diagonal_right_left_reversed.count('XMAS')

def day4_part2(my_input):
    lista = my_input.strip().split('\n')
    part_2 = np.array([list(x) for x in lista])

    count = 0
    for i in range(len(part_2) - 2):
        for j in range(len(part_2[i]) - 2):
            arr = part_2[i:i+3, j:j+3]
            if arr[0, 0] == 'M' and arr[0, 2] == 'S' and arr[1, 1] == 'A' and arr[2, 0] == 'M' and arr[2, 2] == 'S':
                count += 1
            elif arr[0, 0] == 'S' and arr[0, 2] == 'M' and arr[1, 1] == 'A' and arr[2, 0] == 'S' and arr[2, 2] == 'M':
                count += 1       
            elif arr[0, 0] == 'M' and arr[0, 2] == 'M' and arr[1, 1] == 'A' and arr[2, 0] == 'S' and arr[2, 2] == 'S':
                count += 1   
            elif arr[0, 0] == 'S' and arr[0, 2] == 'S' and arr[1, 1] == 'A' and arr[2, 0] == 'M' and arr[2, 2] == 'M':
                count += 1   

    return count


sample_input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

my_input = open(r"2024/inputs/Day_04.txt").read()

# Tests
assert day4_part1(sample_input) == 18
assert day4_part2(sample_input) == 9

# Results
print(day4_part1(my_input))
print(day4_part2(my_input))
