# Day 2

sample_input = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''


def day2_part1(sample_input):
    values = sample_input.replace(':', ';').split('\n')
    game_ids = []
    for value in values:
        games = value.split(';')
        game_id = games[0].split(' ')[1]

        possible = True
        for reveal in games[1:]:
            cubes = reveal.split(',')
            for cube in cubes:
                if 'blue' in cube and int(cube.split(' ')[1]) > 14:
                    possible = False
                if 'red' in cube and int(cube.split(' ')[1]) > 12:
                    possible = False
                if 'green' in cube and int(cube.split(' ')[1]) > 13:
                    possible = False

        if possible:
            game_ids.append(int(game_id))

    return sum(game_ids)


def day2_part2(sample_input):
    values = sample_input.replace(':', ';').split('\n')
    game_ids = []
    for value in values:
        games = value.split(';')
        game_id = games[0].split(' ')[1]

        r, g, b = [], [], []
        for reveal in games[1:]:
            cubes = reveal.split(',')

            for cube in cubes:
                #print(cube.split(' ')[1])
                if 'blue' in cube:
                    b.append(int(cube.split(' ')[1]))
                else: 
                    b.append(0)
                if 'red' in cube:
                    r.append(int(cube.split(' ')[1]))
                else: 
                    r.append(0)
                if 'green' in cube:
                    g.append(int(cube.split(' ')[1]))
                else: 
                    g.append(0)

        ra, gs, bs = max(r), max(g), max(b)
        game_ids.append(int(ra * gs * bs))

    return sum(game_ids)


# Tests
assert day2_part1(sample_input) == 8
assert day2_part2(sample_input) == 2286


# Results
my_input = open(r"2023/inputs/Day_2.txt").read()
print(day2_part1(my_input))
print(day2_part2(my_input))
