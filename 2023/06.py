import aocd
import re, math

data = aocd.get_data(day=6,year=2023)
sample = """Time:      7  15   30
Distance:  9  40  200"""

def part1(puzzle_input):
    time, distance = puzzle_input.splitlines()
    times = re.findall(r'\d+',time)
    distances = re.findall(r'\d+',distance)
    total = []
    for i, t in enumerate(map(int, times)):
        ways_to_win = 0
        for s in range(1,t):
            d = s*(t-s)
            if d > int(distances[i]):
                ways_to_win+=1
        total.append(ways_to_win)
    return math.prod(total)

def part2(puzzle_input):
    time, distance = puzzle_input.splitlines()
    times = re.sub(r'\D+','',time)
    print(times)
    distances = re.sub(r'\D+','',distance)
    print(distances)
    #total = []
    #for i, t in enumerate(map(int, times)):
    ways_to_win = 0
    for s in range(1,int(times)):
        d = s*(int(times)-s)
        if d > int(distances):
            ways_to_win+=1
    return ways_to_win

print(f'Part 1 answer: {part1(data)}')
print(f'Part 2 answer: {part2(data)}')