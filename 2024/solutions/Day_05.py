# Day 5


def day5(my_input):
    rules = [(int(x.split('|')[0]), int(x.split('|')[1])) for x in my_input.strip().split('\n\n')[0].split('\n')]
    updates = [[int(y) for y in x.split(',')] for x in my_input.strip().split('\n\n')[1].split('\n')]

    correctly_ordered = []
    incorrectly_ordered = []
    for update in updates:
        correct = True
        for i in range(len(update)-1):
            for j in range(i+1, len(update)):
                if (update[i], update[j]) not in rules:
                    correct = False
                    incorrectly_ordered.append(update)
                    break

        if correct:
            correctly_ordered.append(update)

    incorrectly_ordered = [list(x) for x in set(tuple(x) for x in incorrectly_ordered)]

    part_1 = sum([x[len(x)//2] for x in correctly_ordered])

    updated_order = []
    for update in incorrectly_ordered:
        for i in range(len(update)-1):
            for j in range(i+1, len(update)):
                if (update[i], update[j]) not in rules:
                    update[i], update[j] = update[j], update[i]
        updated_order.append(update)

    part_2 = sum([x[len(x)//2] for x in updated_order])

    return part_1, part_2


sample_input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

my_input = open(r"2024/inputs/Day_05.txt").read()

# Tests
assert day5(sample_input) == (143, 123)

# Results
print(day5(my_input))
