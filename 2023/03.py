import aocd
import re, math
data = aocd.get_data(day=3,year=2023).splitlines()

def part1(puzzle_input):
    symbol_regex = r'[^.\d]'
    number_regex = r'\d+'
    result = 0

    symbol_adjacent = set()
    for i, line in enumerate(puzzle_input):
        for m in re.finditer(symbol_regex, line):
            j = m.start()
            symbol_adjacent |= {(r, c) for r in range(i-1, i+2) for c in range(j-1, j+2)}
    #print(symbol_adjacent)
    

    for i, line in enumerate(puzzle_input):
        for m in re.finditer(number_regex, line):
            if any((i, c) in symbol_adjacent for c in range(*m.span())):
                result+=int(m.group())
    return result

def part2(puzzle_input):
    gear_regex = r'\*'
    number_regex = r'\d+'
    result = 0

    gears = dict()
    for i, line in enumerate(puzzle_input):
        for m in re.finditer(gear_regex, line):
            gears[(i,m.start())] = []

    for i, line in enumerate(puzzle_input):
        for m in re.finditer(number_regex, line):
            for r in range(i-1,i+2):
                for c in range(m.start()-1, m.end()+1):
                    if (r,c) in gears:
                        gears[(r,c)].append(int(m.group()))
    for v in gears.values():
        if len(v) == 2:
            result += math.prod(v)

    return result

print(f'Part 1 answer: {part1(data)}')
print(f'Part 2 answer: {part2(data)}')
