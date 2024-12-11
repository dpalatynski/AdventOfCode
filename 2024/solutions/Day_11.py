# Day 11
import functools


def day11(my_input, part_2):
    lista = [x for x in my_input.strip().split(' ')]

    _sum = 0
    for el in lista:
        _sum += _count(int(el), 0, 75 if part_2 else 25)
    return _sum

@functools.cache
def _count(el, i, limit):
    if i == limit:
        return 1
    if el == 0:
        return _count(1, i + 1, limit)
    if len(str(el)) & 1 == 0:
        return _count(int(str(el)[:len(str(el))//2]), i+1, limit) + _count(int(str(el)[len(str(el))//2:]), i+1, limit)
    return _count(el*2024, i+1, limit)


sample_input = """125 17"""

my_input = open(r"2024/inputs/Day_11.txt").read()

# Tests
assert day11(sample_input, part_2=False) == 55312

# Results
print(day11(my_input, part_2=False))
print(day11(my_input, part_2=True))
