# Day 24
from sympy import Symbol
from sympy import solve


def find_intersection(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    slope = (y2 - y1) / (x2 - x1)
    intercept = y1 - slope * x1
    return slope, intercept


def calculate_intersection(point1, point2):
    point11 = [point1[0], point1[1]]
    point22 = [point1[0] + point1[3], point1[1] + point1[4]]
    point33 = [point2[0], point2[1]]
    point44 = [point2[0] + point2[3], point2[1] + point2[4]]

    slope1, intercept1 = find_intersection(point11, point22)
    slope2, intercept2 = find_intersection(point33, point44)
    
    if slope1 != slope2:
        x = (intercept2 - intercept1) / (slope1 - slope2)
        y = slope1 * x + intercept1
        return x, y
    
    return None


def day24(my_input, test_area):
    hailstones = [line.split('@') for line in my_input.split('\n')]

    points = []
    for hailstone in hailstones:
        px = int(hailstone[0].split(',')[0])
        py = int(hailstone[0].split(',')[1])
        pz = int(hailstone[0].split(',')[2])
        vx = int(hailstone[1].split(',')[0])
        vy = int(hailstone[1].split(',')[1])
        vz = int(hailstone[1].split(',')[2])

        points.append([px, py, pz, vx, vy, vz])

    # part 1
    counter = 0
    for i in range(len(points)):
        for j in range(i, len(points)):
            intersection = calculate_intersection(points[i], points[j])

            if intersection == None:
                continue
            t1 = (intersection[0] - points[i][0]) / points[i][3]
            t2 = (intersection[0] - points[j][0]) / points[j][3]
            if t1 < 0 or t2 < 0:
                continue
            if test_area[0] <= intersection[0] <= test_area[1] and test_area[0] <= intersection[1] <= test_area[1]:
                counter += 1

    # part 2
    px, py, pz = Symbol('x'), Symbol('y'), Symbol('z')
    vx, vy, vz = Symbol('vx'), Symbol('vy'), Symbol('vz')
    symbols = [px, py, pz, vx, vy, vz]
    lines = []

    for i in range(3):
        t = Symbol('t'+str(i))
        symbols.append(t)

        point = points[i]
        line_x = px + vx*t - point[0] - point[3]*t
        line_y = py + vy*t - point[1] - point[4]*t
        line_z = pz + vz*t - point[2] - point[5]*t

        lines.append(line_x)
        lines.append(line_y)
        lines.append(line_z)

    result = solve(lines, *symbols)
    answer = result[0][0]+result[0][1]+result[0][2]

    return counter, answer


sample_input = '''19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3'''



# Test
assert(day24(sample_input, (7, 27)) == (2, 47))


# Results
my_input = open(r"2023/inputs/Day_24.txt").read()
print(day24(my_input, (200000000000000, 400000000000000)))
