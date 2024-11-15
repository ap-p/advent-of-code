import aocd
data = aocd.get_data(day=1,year=2023).splitlines()

def part1(puzzle_input):
    line_results = []
    for item in puzzle_input:
        nums = [num for num in item if num.isdigit()]
        line_results.append(int(nums[0]+nums[-1]))
    results = sum(line_results)
    return results


def part2(puzzle_input):
    line_results = []

    replacements={
        'one':'o1ne',
        'two':'t2o',
        'three':'th3ee',
        'four':'f4ur',
        'five':'f5ve',
        'six':'s6x',
        'seven':'se7en',
        'eight':'ei8ht',
        'nine':'n9ne'
    }

    def numberfy(string):
        for old, new in replacements.items():
            string = string.replace(old,new)
        return string

    for item in puzzle_input:
        nums = [num for num in numberfy(item) if num.isdigit()]
        line_results.append(int(nums[0]+nums[-1]))
    results = sum(line_results)

    return results

print(f'Part 1 answer: {part1(data)}')
print(f'Part 2 answer: {part2(data)}')