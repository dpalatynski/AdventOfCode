# Day 13


def day13(my_input, part_2=False):
    lista = my_input.strip().split('\n\n')
    machines = []

    for section in lista:
        lines = section.split('\n')
        A = lines[0].split(': ')[1].replace('X+', '').replace('Y+', '').split(', ')
        B = lines[1].split(': ')[1].replace('X+', '').replace('Y+', '').split(', ')
        prize = lines[2].split(': ')[1].replace('X=', '').replace('Y=', '').split(', ')
        machines.append({'A': (int(A[0]), int(A[1])), 
                        'B': (int(B[0]), int(B[1])), 
                        'prize': (10000000000000+int(prize[0]), 10000000000000+int(prize[1])) if part_2 else (int(prize[0]), int(prize[1]))})

    cost = 0
    for machine in machines:
        A_x, A_y = machine['A']
        B_x, B_y = machine['B']
        X_target, Y_target = machine['prize']
        
        ans_x = (X_target * B_y - Y_target * B_x) // (A_x * B_y - B_x * A_y)
        ans_y = (A_x * Y_target - X_target * A_y) // (A_x * B_y - B_x * A_y)

        if ans_x * A_x + ans_y * B_x == X_target and ans_x * A_y + ans_y * B_y == Y_target:
            cost += 3 * ans_x + ans_y
    
    return cost


sample_input = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""

my_input = open(r"2024/inputs/Day_13.txt").read()

# Tests
assert day13(sample_input) == 480

# Results
print(day13(my_input))
print(day13(my_input, part_2=True))
