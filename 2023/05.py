import aocd
import re
data = aocd.get_data(day=5,year=2023)

sample = """seeds: 79 14 55 13

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
56 93 4"""

def part1(puzzle_input):
    data = puzzle_input.split('\n\n')
    seeds = re.findall(r'\d+',data[0])
    location = []
    for seed in map(int,seeds):
        for m in data[1:]:
            for nums in re.findall(r'(\d+) (\d+) (\d+)',m):
                destination, source, dist = map(int, nums)
                if seed in range(source, source+dist):
                    seed += destination-source
                    break
        location.append(seed)
    return min(location)

def part2(puzzle_input):
    data = puzzle_input.split('\n\n')
    interval = []
    locations = []
    for seed_pack in re.findall(r'(\d+) (\d+)',data[0]):
        seed_start, dist = map(int,seed_pack)
        seed_end = seed_start+dist
        interval.append((seed_start,seed_end,1))

    while interval:
        seed_start, seed_end, step = interval.pop()
        if step == 8:
            locations.append(seed_start)
            continue
        for mapping in re.findall(r'(\d+) (\d+) (\d+)', data[step]):
            destination, source, dist = map(int, mapping)
            finish = source+dist
            diff = destination-source
            if seed_end <= source or finish <= seed_start:
                continue
            if seed_start < source:
                interval.append((seed_start,source,step))
                seed_start = source
            if finish < seed_end:
                interval.append((finish,seed_end,step))
                seed_end = finish
            interval.append((seed_start+diff, seed_end+diff, step+1))
            break
    
        else:
            interval.append((seed_start,seed_end,step+1))
    return min(locations)

print(f'Part 1 answer: {part1(data)}')
print(f'Part 2 answer: {part2(data)}')