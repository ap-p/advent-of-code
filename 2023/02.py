import aocd
import re, math
data = aocd.get_data(day=2,year=2023).splitlines()

#TODO 12 red, 13 green, 14 blue

def part1(puzzle_input):
    possible = []
    for game_data in puzzle_input:
        game, data = game_data.split(':')
        cubes = re.split(r'[;,]',data)
        for index, c in enumerate(cubes):
            num, color = c.strip().split()
            if (color == 'red' and int(num) > 12) \
                or (color == 'green' and int(num) > 13) \
                or (color == 'blue' and int(num) > 14):
                break
            if index == len(cubes)-1:
                possible.append(int(game.split()[1]))
    results = sum(possible)         
    return results

def part2(puzzle_input):
    power = []
    for game_data in puzzle_input:
        mins = {'red':0,'green':0,'blue':0}
        game, data = game_data.split(':')
        cubes = re.split(r'[;,]',data)
        for c in cubes:
            num, color = c.strip().split()
            if int(num) > mins[color]:
                mins[color] = int(num)
        power.append(math.prod(list(mins.values())))
    results = sum(power)         
    return results

print(f'Part 1 answer: {part1(data)}')
print(f'Part 2 answer: {part2(data)}')