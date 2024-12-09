# Day 9


def day9_part1(my_input):
    ids = []
    occupied_spaces = []
    free_spaces = []
    for i in range(0, len(my_input), 2):
        ids.append(i//2)
        occupied_spaces.append(int(my_input[i]))
        if i+1 < len(my_input):
            free_spaces.append(int(my_input[i+1]))
        else:
            free_spaces.append(0)

    blocks = []
    for i in range(0, len(ids)):
        blocks.extend([str(ids[i])] * occupied_spaces[i] + ['.'] * free_spaces[i])

    for i in range(len(blocks)):
        if blocks[i] == '.':
            for j in range(len(blocks)-1, i, -1):
                if blocks[j] != '.':
                    blocks[i] = blocks[j]
                    blocks[j] = '.'
                    break

    checksum = 0
    for i in range(len(blocks)):
        if blocks[i] != '.':
            checksum += i * int(blocks[i])

    return checksum

def day9_part2(my_input):
    ids = []
    occupied_spaces = []
    free_spaces = []
    for i in range(0, len(my_input), 2):
        ids.append(i//2)
        occupied_spaces.append(int(my_input[i]))
        if i+1 < len(my_input):
            free_spaces.append(int(my_input[i+1]))
        else:
            free_spaces.append(0)

    blocks = []
    for i in range(len(ids)):
        blocks.extend([str(ids[i])] * occupied_spaces[i] + ['.'] * free_spaces[i])

    for file_id in ids[::-1]:
        file_positions = [i for i, x in enumerate(blocks) if x == str(file_id)]
        file_size = len(file_positions)

        start, length = None, 0
        for i in range(len(blocks)):
            if blocks[i] == '.':
                if start is None:
                    start = i
                length += 1
            else:
                start, length = None, 0
            if length == file_size:
                break

        if start is not None and start < file_positions[0]:
            for i in range(file_size):
                blocks[start + i] = str(file_id)
                blocks[file_positions[i]] = '.'

    checksum = 0
    for i in range(len(blocks)):
        if blocks[i] != '.':
            checksum += i * int(blocks[i])

    return checksum


sample_input = """2333133121414131402"""

my_input = open(r"2024/inputs/Day_09.txt").read()

# Tests
assert day9_part1(sample_input) == 1928
assert day9_part2(sample_input) == 2858

# Results
print(day9_part1(my_input))
print(day9_part2(my_input))
