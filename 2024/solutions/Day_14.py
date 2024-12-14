# Day 14


def day14(my_input, width, height):
    lista = [robots for robots in my_input.strip().split('\n')]
    positions = [[int(robots.split(' ')[0].split(',')[0].split('=')[1]), int(robots.split(' ')[0].split(',')[1])] for robots in lista]
    velocities = [(int(robots.split(' ')[1].split(',')[0].split('=')[1]), int(robots.split(' ')[1].split(',')[1])) for robots in lista]

    min_safety_factor = []
    for j in range(max(width*height, 100+1)):
        positions = [[int(robots.split(' ')[0].split(',')[0].split('=')[1]), int(robots.split(' ')[0].split(',')[1])] for robots in lista]
        for i, position in enumerate(positions):
            position[0] = (position[0] + j*velocities[i][0]) % width
            position[1] = (position[1] + j*velocities[i][1]) % height

        top_left, top_right, bottom_left, bottom_right = 0, 0, 0, 0
        for position in positions:
            if position[0] < width//2 and position[1] < height//2:
                top_left += 1
            elif position[0] > width//2 and position[1] < height//2:
                top_right += 1
            elif position[0] < width//2 and position[1] > height//2:
                bottom_left += 1
            elif position[0] > width//2 and position[1] > height//2:
                bottom_right += 1

        safety_factor = top_left * top_right * bottom_left * bottom_right
        if j == 100:
            part_1 = safety_factor

        min_safety_factor.append(safety_factor)

    return part_1, min_safety_factor.index(min(min_safety_factor))
        

sample_input = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""

my_input = open(r"2024/inputs/Day_14.txt").read()

# Tests
assert day14(sample_input, 11, 7)[0] == 12

# Results
print(day14(my_input, 101, 103))
