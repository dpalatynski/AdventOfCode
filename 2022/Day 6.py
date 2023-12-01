samples = ['mjqjpqmgbljsphdztnvjfqwrcgsmlb',
           'bvwbjplbgvbhsrlpgdmjqwftvncz',
           'nppdvjthqldpwncqszvftbrmjlhg',
           'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg',
           'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw']

answers = [7, 5, 6, 10, 11]
answers_2 = [19, 23, 23, 29, 26]


def find_start_of_packet(signal, length):
    for i in range(len(signal)-3):
        if len(set(signal[i:i+length])) == length:
            return i+length


for i, sample in enumerate(samples):
    assert find_start_of_packet(sample, 4) == answers[i]
    assert find_start_of_packet(sample, 14) == answers_2[i]


puzzle_input = open("Day 6.txt").read()
print(find_start_of_packet(puzzle_input, 4))
print(find_start_of_packet(puzzle_input, 14))
