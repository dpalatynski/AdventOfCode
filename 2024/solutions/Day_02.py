# Day 2


def day2(my_input):
    lines = [list(map(int, x.strip().split())) for x in my_input.strip().split('\n')]

    safe_count_1, safe_count_2 = 0, 0
    for report in lines:
        mod = False
        if is_safe(report):
            safe_count_1 += 1
            mod = True
        elif not mod:
            for i in range(len(report)):
                if is_safe(report[:i] + report[i+1:]):
                    safe_count_2 += 1
                    mod = True
                    break
    return safe_count_1, safe_count_1+safe_count_2

def is_safe(report):
    diffs = [report[i+1] - report[i] for i in range(len(report) - 1)]
    
    increasing = all(1 <= diff <= 3 for diff in diffs)
    decreasing = all(-3 <= diff <= -1 for diff in diffs)
    
    return increasing or decreasing


sample_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

my_input = open(r"2024/inputs/Day_02.txt").read()

# Tests
assert day2(sample_input) == (2, 4)

# Results
print(day2(my_input))
