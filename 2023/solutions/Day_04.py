# Day 4

sample_input = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''


def day4(sample_input):
    cards = [card.split(':')[1].split('|') for card in sample_input.split('\n')]

    points = 0
    scratchcards = [1]*len(cards) # for part 2
    for i, card in enumerate(cards):
        winning_numbers = [int(x) for x in card[0].split(' ') if x != '']
        my_numbers = [int(x) for x in card[1].split(' ') if x != '']

        wins = 0
        for number in my_numbers:
            if number in winning_numbers:
                wins += 1
        score = 2**(wins-1) if wins != 0 else 0
        points += score
        
        for j in range(1, min(wins+1, len(cards))): # part 2
            scratchcards[i+j] += scratchcards[i]
        
    return points, sum(scratchcards)


# Tests
assert day4(sample_input) == (13, 30)


# Results
my_input = open(r"2023/inputs/Day_04.txt").read()
print(day4(my_input))
