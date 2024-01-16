# Day 20
from collections import deque
from itertools import count
import math


def day20_part1(my_input):
    graph = {}
    flip_flop = {}
    memory = {}
    for line in my_input.split('\n'):
        source, destinations = line.split(' -> ')
        destinations = destinations.split(', ')
        graph[source.lstrip('%&')] = destinations
        if source.startswith('%'):
            flip_flop[source[1:]] = 0   # each flip flip is off (0) by default
        elif source.startswith('&'):
            memory[source[1:]] = {}

    for conjunction in memory.keys():   # get source modules for conjunctions 
        for source, destinatons in graph.items():
            if conjunction in destinatons:
                memory[conjunction][source] = 0   # initialize memory at low (0)

    signal_count = [0, 0]       # [low, high]
    for _ in range(1000):
        signal_count[0] += 1    # initial low signal from button to broadcaster
        queue = deque([('broadcaster', in_module, 0) for in_module in graph['broadcaster']])
        while queue:
            out_module, in_module, signal = queue.popleft()
            signal_count[signal] += 1

            if in_module in flip_flop and signal == 0:
                flip_flop[in_module] = 1 - flip_flop[in_module]
                out_signal = flip_flop[in_module]

            elif in_module in memory:
                memory[in_module][out_module] = signal
                out_signal = 1 if 0 in memory[in_module].values() else 0

            else:   # no output
                continue
            
            queue.extend([(in_module, nxt, out_signal) for nxt in graph[in_module]])

    return math.prod(signal_count)


def day20_part2(my_input):
    graph = {}
    flip_flop = {}
    memory = {}
    for line in my_input.split('\n'):
        source, destinations = line.split(' -> ')
        destinations = destinations.split(', ')
        graph[source.lstrip('%&')] = destinations
        if source.startswith('%'):
            flip_flop[source[1:]] = 0
        elif source.startswith('&'):
            memory[source[1:]] = {}

    for conjunction in memory.keys():
        for source, destinatons in graph.items():
            if conjunction in destinatons:
                memory[conjunction][source] = 0

    final_layer = [m1 for m1 in graph if 'rx' in graph[m1]]

    semi_final_layer = set(module for module in graph if final_layer[0] in graph[module])
    cycle_lengths = []
    
    for button_push in count(1):
        queue = deque([('broadcaster', in_module, 0) for in_module in graph['broadcaster']])
        while queue:
            out_module, in_module, signal = queue.popleft()

            if in_module in flip_flop and signal == 0:
                flip_flop[in_module] = 1 - flip_flop[in_module]
                out_signal = flip_flop[in_module]

            elif in_module in memory:
                memory[in_module][out_module] = signal
                out_signal = 1 if 0 in memory[in_module].values() else 0
                if in_module in semi_final_layer and out_signal == 1:
                    cycle_lengths.append(button_push)
                    semi_final_layer.remove(in_module)

            else:
                continue
            
            queue.extend([(in_module, nxt, out_signal) for nxt in graph[in_module]])

        if not semi_final_layer:
            break

    return math.lcm(*cycle_lengths)


sample_input = r'''broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a'''


# Test
assert(day20_part1(sample_input) == 32000000)


# Results
my_input = open(r"2023/inputs/Day_20.txt").read()
print(day20_part1(my_input))
print(day20_part2(my_input))
