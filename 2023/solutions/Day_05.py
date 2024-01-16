# Day 5


def create_maps(content):
    maps = {}
    new_map = True
    for v1 in content[2:]:
        if v1 == "":
            new_map = True
            continue

        if new_map:
            map_name = v1.strip()[:-5]
            maps[map_name] = []
            new_map = False
            continue

        dest, source, count = v1.strip().split()
        dest = int(dest)
        source = int(source)
        count = int(count)
        maps[map_name].append([dest, source, count])

    return maps


def get_from_map(maps, map_name, value):
    working_map = maps[map_name]
    for entry in working_map:
        dest, source, count = entry
        if source <= value < source + count:
            return dest + (value - source)
    return value


def get_from_map2(maps, map_name, value):
    working_map = maps[map_name]
    for entry in working_map:
        dest, source, count = entry
        if dest <= value < dest + count:
            return source + (value - dest)
    return value


def day5_part1(my_input):
    content = my_input.split('\n')
    seeds = content[0].split(':')[1].split(' ')[1:]
    maps = create_maps(content)

    lowest_location = None
    for seed in seeds:
        seed = int(seed)
        soil = get_from_map(maps, 'seed-to-soil', seed)
        fertilizer = get_from_map(maps, 'soil-to-fertilizer', soil)
        water = get_from_map(maps, 'fertilizer-to-water', fertilizer)
        light = get_from_map(maps, 'water-to-light', water)
        temperature = get_from_map(maps, 'light-to-temperature', light)
        humidity = get_from_map(maps, 'temperature-to-humidity', temperature)
        location = get_from_map(maps, 'humidity-to-location', humidity)
        
        if lowest_location is None or location < lowest_location:
            lowest_location = location

    return lowest_location


def valid_seed(seed, seeds):
    for temp_seed in seeds:
        start, count = temp_seed
        start = int(start)
        count = int(count)
        if start <= seed < start + count:
            return True
    return False


def day5_part2(my_input):
    content = my_input.split('\n')
    seeds = content[0].split(':')[1].split(' ')[1:]
    maps = create_maps(content)

    new_seeds = []
    for i in range(0, len(seeds), 2):
        new_seeds.append((seeds[i], seeds[i+1]))

    value = 0
    while True:
        humidity = get_from_map2(maps, 'humidity-to-location', value)
        temperature = get_from_map2(maps, 'temperature-to-humidity', humidity)
        light = get_from_map2(maps, 'light-to-temperature', temperature)
        water = get_from_map2(maps, 'water-to-light', light)
        fertilizer = get_from_map2(maps, 'fertilizer-to-water', water)
        soil = get_from_map2(maps, 'soil-to-fertilizer', fertilizer)
        seed = get_from_map2(maps, 'seed-to-soil', soil)
        if valid_seed(seed, new_seeds):
            return value
        value += 1


sample_input = '''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4'''


# Tests
assert(day5_part1(sample_input) == 35)
assert(day5_part2(sample_input) == 46)


# Results
my_input = open(r"2023/inputs/Day_05.txt").read()
print(day5_part1(my_input))
print(day5_part2(my_input))
