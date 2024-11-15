import aocd

data = aocd.get_data(day=9,year=2023)
sample = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

last_item = []
first_item = []
'''
def generate_next(sequence,parent=0):

    #print(sequence)
    diffs = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
    last_item.append(sequence[-1])
    if any(x != 0 for x in diffs):
        #last_item.append(sequence[-1])
        return generate_next(diffs)
    return sum(last_item)
'''
def part1(puzzle_input):

    def generate_next(sequence,parent=0):

        #print(sequence)
        diffs = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
        last_item.append(sequence[-1])
        if any(x != 0 for x in diffs):
            #last_item.append(sequence[-1])
            return generate_next(diffs)
        return sum(last_item)

    #sequences = [[int(num) for num in sequence] for sequence in puzzle_input.splitlines()]
    sequences = puzzle_input.splitlines()
    sequences = [list(map(int, sequence.split())) for sequence in sequences]
    #print(sequences)
    results = []
    for seq in sequences:
        last_item.clear()
        results.append(generate_next(seq))
    return sum(results)




def part2(puzzle_input):
    def generate_next(sequence,parent=0):

        #print(sequence)
        diffs = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
        if len(first_item) % 2 == 0:
            first_item.append(sequence[0])
        else:
            first_item.append(sequence[0]*-1)
        #print(sequence)
        if any(x != 0 for x in diffs):
            #last_item.append(sequence[-1])
            return generate_next(diffs)
        #print(first_item)
        #z = reduce(lambda x, y: x - y, first_item)
        #print(z)
        return sum(first_item) #reduce(lambda x, y: x - y, first_item)

    #sequences = [[int(num) for num in sequence] for sequence in puzzle_input.splitlines()]
    sequences = puzzle_input.splitlines()
    sequences = [list(map(int, sequence.split())) for sequence in sequences]
    #print(sequences)
    results = []
    for seq in sequences:
        first_item.clear()
        results.append(generate_next(seq))
    return sum(results)

#print(f'Part 1 answer: {part1(data)}')
print(f'Part 2 answer: {part2(data)}')




