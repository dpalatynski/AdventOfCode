# Day 19
import re


def is_accepted(where, instruct, sss):
    if where == 'A':
        return True

    if where == 'R':
        return False

    inst = instruct[where]

    for i in inst:
        if ':' in i:
            tokens = i.split(':')

            if '>' in tokens[0]:
                z = tokens[0].split('>')
                if sss[z[0]] > int(z[1]):
                    return is_accepted(tokens[1], instruct, sss)
                else:
                    continue

            if '<' in tokens[0]:
                z = tokens[0].split('<')
                if sss[z[0]] < int(z[1]):
                    return is_accepted(tokens[1], instruct, sss)
                else:
                    continue

        return is_accepted(i, instruct, sss)


def day20_part1(my_input):
    instructions, coordinates = my_input.split('\n\n')

    instruct = dict()
    for i in instructions.splitlines():
        tmp = i.split('{')
        name = tmp[0]
        instruct[name] = list(tmp[1][:-1].split(','))

    result = 0
    for c in coordinates.splitlines():
        g = re.match(r'{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}', c)
        if g:
            sss = {
                'x': int(g[1]),
                'm': int(g[2]),
                'a': int(g[3]),
                's': int(g[4])
            }

            if is_accepted('in', instruct, sss):
                result += sum(sss.values())

        else:
            assert False

    return result


def valid_combinations(where, instruct, sss, index):
    if where == 'A':
        return (sss['x'][1] - sss['x'][0] + 1) * \
                (sss['m'][1] - sss['m'][0] + 1) * \
                (sss['a'][1] - sss['a'][0] + 1) * \
                (sss['s'][1] - sss['s'][0] + 1)

    if where == 'R':
        return 0

    inst = instruct[where]
    i = inst[index]

    if ':' in i:
        tokens = i.split(':')
        where_next = tokens[1]

        if '>' in tokens[0]:
            z = tokens[0].split('>')
            from_what = z[0]
            value = int(z[1])

            if value < sss[from_what][0]:
                return valid_combinations(where_next, instruct, ss, 0)

            if value > sss[from_what][1]:
                return 0

            ss = sss.copy()
            ss[from_what] = (sss[from_what][0], value)
            a = valid_combinations(where, instruct, ss, index + 1)

            ss[from_what] = (value + 1, sss[from_what][1])
            b = valid_combinations(where_next, instruct, ss, 0)

            return a + b

        if '<' in tokens[0]:
            z = tokens[0].split('<')
            from_what = z[0]
            value = int(z[1])

            if value < sss[from_what][0]:
                return 0

            if value > sss[from_what][1]:
                return valid_combinations(where_next, instruct, ss, 0)

            ss = sss.copy()
            ss[from_what] = (sss[from_what][0], value - 1)
            a = valid_combinations(where_next, instruct, ss, 0)

            ss[from_what] = (value, sss[from_what][1])
            b = valid_combinations(where, instruct, ss, index + 1)

            return a + b

        raise Exception('')

    return valid_combinations(i, instruct, sss, 0)


def day20_part2(my_input):
    instructions, coordinates = my_input.split('\n\n')

    instruct = dict()
    for i in instructions.splitlines():
        tmp = i.split('{')
        name = tmp[0]
        instruct[name] = list(tmp[1][:-1].split(','))

    sss = {
        'x': (1, 4000),
        'm': (1, 4000),
        'a': (1, 4000),
        's': (1, 4000),
    }

    return valid_combinations('in', instruct, sss, 0)


sample_input = '''px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}'''


# Tests
assert(day20_part1(sample_input) == 19114)
assert(day20_part2(sample_input) == 167409079868000)


# Results
my_input = open(r"2023/inputs/Day_19.txt").read()
print(day20_part1(my_input))
print(day20_part2(my_input))
