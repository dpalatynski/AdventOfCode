# Day 18


def find_points(my_input, part):
    starting_point = (0, 0)
    points = []
    current = starting_point
    for line in my_input.split('\n'):
        if part == 1:
            direction, steps = line.split(' ')[0], int(line.split(' ')[1])
        elif part == 2:
            _, _, hex = line.split(' ')[0], int(line.split(' ')[1]), line.split(' ')[2]
            steps = int(hex[2:7], 16)
            direction = hex[-2]
        if direction == '0' or direction == 'R':
            for _ in range(steps):
                points.append((current[0], current[1] + 1))
                current = points[-1]
        elif direction == '2' or direction == 'L':
            for _ in range(steps):
                points.append((current[0], current[1] - 1))
                current = points[-1]
        elif direction == '1' or direction == 'D':
            for _ in range(steps):
                points.append((current[0] + 1, current[1]))
                current = points[-1]
        elif direction == '3' or direction == 'U':
            for _ in range(steps):
                points.append((current[0] - 1, current[1]))
                current = points[-1]

    return points


def Shoelace_formula(points):
    # https://en.wikipedia.org/wiki/Shoelace_formula

    area = 0
    for i in range(len(points)-1):
        x1, y1 = points[i]
        x2, y2 = points[i+1]
        area += x1*y2 - x2*y1

    return abs(area//2)


def Picks_theorem(points):
    # https://en.wikipedia.org/wiki/Pick%27s_theorem
    #
    # A = i + b/2 - 1, where
    # A - area
    # i - the number of integer points interior to the polygon
    # b - the number of integer points on its boundary
    # 
    # Function returns i
    return Shoelace_formula(points) - len(points)//2 + 1


def day18(input, part):
    points = find_points(input, part)
    return Picks_theorem(points) + len(points)


sample_input = r'''R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)'''


# Tests
assert(day18(sample_input, 1) == 62)
assert(day18(sample_input, 2) == 952408144115)


# Results
my_input = open(r"2023/inputs/Day_18.txt").read()
print(day18(my_input, 1))
print(day18(my_input, 2))
