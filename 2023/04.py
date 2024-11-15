import aocd
import re, math
data = aocd.get_data(day=4,year=2023).splitlines()

sample = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".splitlines()

def part1(puzzle_input):
    results = []
    for line in puzzle_input:
        numbers = line.split(':')[1]
        wins, nums = [x.strip().split() for x in numbers.strip().split('|')]
        points = 0
        for num in nums:
            if num in wins:
                points += 1
        if points: results.append(2**(points-1))
    return sum(results)

def part2(puzzle_input):
    cards = [1] * len(puzzle_input)
    for index, line in enumerate(puzzle_input):
        points = 0
        numbers = line.split(':')[1]
        wins, nums = [x.strip().split() for x in numbers.strip().split('|')]
        
        for num in nums:
            if num in wins:
                points += 1
        for p in range(points):
            cards[index+p+1] += cards[index]

    return sum(cards)

print(f'Part 1 answer: {part1(data)}')
print(f'Part 2 answer: {part2(data)}')


