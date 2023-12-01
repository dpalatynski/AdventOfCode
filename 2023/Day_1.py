# Day 1

sample_input = '''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet'''

sample_input_2 = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''


def day1(text, part=None):
    lines = text.split('\n')
    values = []
    for line in lines:
        if part == 2:
            line = line.replace("one", "one1ene")
            line = line.replace("two", "two2two")
            line = line.replace("three", "three3three")
            line = line.replace("four", "four4gour")
            line = line.replace("five", "five5five")
            line = line.replace("six", "six6six")
            line = line.replace("seven", "seven7seven")
            line = line.replace("eight", "eight8eight")
            line = line.replace("nine", "nine9nine")

        first, last = False, False
        for i in range(len(line)):
            if line[i].isdigit() and first == False:
                x = line[i]
                first = True
        for j in range(len(line), 0, -1):
            if line[j-1].isdigit() and last == False:
                y = line[j-1]
                last = True

        values.append(int(x+y))

    return sum(values)


# Tests
assert day1(sample_input) == 142
assert day1(sample_input_2, 2) == 281


# Results
my_input = open(r"2023/inputs/Day_1.txt").read()
print(day1(my_input))
print(day1(my_input, 2))
