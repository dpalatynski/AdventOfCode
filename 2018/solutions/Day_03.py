# Day 3

sample_input = '''#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2'''


def day3(my_input):
    claims = [claim for claim in my_input.split('\n')]
    claims = [(int(claim.split(' ')[2].split(',')[0]), 
            int(claim.split(' ')[2].split(',')[1].replace(':', '')), 
            int(claim.split(' ')[-1].split('x')[0]), 
            int(claim.split(' ')[-1].split('x')[1]),
            int(claim.split(' ')[0].replace('#', ''))) 
            for claim in claims]

    points = {}
    ids = {}
    for claim in claims:
        for i in range(claim[0], claim[0] + claim[2]):
            for j in range(claim[1], claim[1] + claim[3]):
                if (i, j) not in points:
                    points[(i, j)] = 1
                else:
                    points[(i, j)] += 1

    counter = 0
    for point, value in points.items():
        if value > 1:
            counter += 1

    for claim in claims:
        ids[claim[4]] = True
        for i in range(claim[0], claim[0] + claim[2]):
            for j in range(claim[1], claim[1] + claim[3]):
                if points[(i, j)] > 1:
                    ids[claim[4]] = False

    not_overlapping_id = 0        
    for id, value in ids.items():
        if value:
            not_overlapping_id = id
            break

    return counter, not_overlapping_id


assert day3(sample_input) == (4, 3)

my_input = open('2018/inputs/Day_03.txt').read()
print(day3(my_input))
        