import aocd
import re
from itertools import cycle
import math

data = aocd.get_data(day=8,year=2023)
sample = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""


def part1(puzzle_input):
    mapping = {}
    t = {'L':0,'R':1}
    directions, maps = puzzle_input.split('\n\n')
    pattern = r"(\w+) = \((\w+), (\w+)\)"
    for node, left, right in re.findall(pattern, maps):
        mapping[node] = (left, right)
    loc = 'AAA'
    for steps, d in enumerate(cycle(directions), start=1):
        loc = mapping[loc][t[d]]
        if loc == 'ZZZ': break
    return(steps)

def part2(puzzle_input):

    def check_all(locations):
        r = []
        for loc in locations:
            l = mapping[loc][t[directions[pos]]]
            r.append(l)
        if all(item.endswith('Z') for item in r):
            return False
        return r

    mapping = {}
    t = {'L':0,'R':1}
    directions, maps = puzzle_input.split('\n\n')
    pattern = r"(\w+) = \((\w+), (\w+)\)"
    for node, left, right in re.findall(pattern, maps):
        mapping[node] = (left, right)

    starts = [key for key in mapping if key[-1] == 'A']
    steps = []
    for loc in starts:
        for step, d in enumerate(cycle(directions), start=1):
            loc = mapping[loc][t[d]]
            if loc.endswith('Z'):
                steps.append(step)
                break
    return(math.lcm(*steps))

print(f'Part 1 answer: {part1(data)}')
print(f'Part 2 answer: {part2(data)}')
