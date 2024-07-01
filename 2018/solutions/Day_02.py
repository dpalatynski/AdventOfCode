# Day 2

sample_input = '''abcdef
bababc
abbcde
abcccd
aabcdd
abcdee
ababab'''

sample_input2 = '''abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz'''


def day2_part1(sample_input):
    modified_input = sample_input.split('\n')
    counter_2, counter_3 = 0, 0
    for entry in modified_input:
        all_letters = set(entry)
        once_added_2, once_added_3 = False, False
        for letter in all_letters:
            counter = entry.count(letter)
            if counter == 2 and not once_added_2:
                counter_2 += 1
                once_added_2 = True
            elif counter == 3 and not once_added_3:
                counter_3 += 1
                once_added_3 = True

    return counter_2 * counter_3
    
def day2_part2(sample_input):
    modified_input = sample_input.split('\n')
    for i in range(len(modified_input)):
        for j in range(len(modified_input)):
            diff = 0
            letters = ''
            for letter in range(len(modified_input[i])):
                if modified_input[i][letter] != modified_input[j][letter]:
                    diff += 1
                else:
                    letters += modified_input[i][letter]

            if diff == 1:
                return letters


assert day2_part1(sample_input) == 12
assert day2_part2(sample_input2) == 'fgij'

my_input = open(r'2018/inputs/Day_02.txt').read()
print(day2_part1(my_input))
print(day2_part2(my_input))
