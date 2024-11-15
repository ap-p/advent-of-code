import aocd
from collections import Counter

data = aocd.get_data(day=7,year=2023)
sample = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


def part1(puzzle_input):

    hands = puzzle_input.splitlines()
    hand_types = {6:[],5:[],4:[],3:[],2:[],1:[],0:[]}
    ranked_hands = []
    def trans(cards):
        orig='AKQJT98765432'
        rep ='ABCDEFGHIJKLM'
        translation = str.maketrans(orig,rep)
        return cards.translate(translation)
    def get_type(cards):
        counter = sorted(Counter(cards).values(),reverse=True)
        if counter[0] == 5:
            return 6
        if counter[0] == 4:
            return 5
        if counter[0] == 3 and counter[1] == 2:
            return 4
        if counter[0] == 3:
            return 3
        if counter[0] == 2 and counter[1] == 2:
            return 2
        if counter[0] == 2:
            return 1
        return 0      

    for hand in hands:
        cards, bid = hand.split()
        hand_type = get_type(cards)
        hand_types[hand_type].append([trans(cards),bid])
    for key in hand_types:
        hand_types[key] = sorted(hand_types[key], key=lambda x: x[0])
    for key in sorted(hand_types.keys()):
        ranked_hands.extend(hand_types[key][::-1])
    winnings = [int(c[1]) * (i+1) for i, c in enumerate(ranked_hands)]
    return sum(winnings)


def part2(puzzle_input):
    hands = puzzle_input.splitlines()
    hand_types = {6:[],5:[],4:[],3:[],2:[],1:[],0:[]}
    ranked_hands = []
    def trans(cards):
        orig='AKQT98765432J'
        rep ='ABCDEFGHIJKLM'
        translation = str.maketrans(orig,rep)
        return cards.translate(translation)
    def get_type(cards):
        counter = Counter(cards)
        wilds = counter['J']
        del counter['J']
        counter = sorted(counter.values(),reverse=True)
        if wilds == 5:
            return 6
        if counter[0] + wilds == 5:
            return 6
        if counter[0] + wilds == 4:
            return 5
        if counter[0] + wilds == 3 and counter[1] == 2:
            return 4
        if counter[0] + wilds == 3:
            return 3
        if counter[0] + wilds == 2 and counter[1] == 2:
            return 2
        if counter[0] + wilds == 2:
            return 1
        return 0      

    for hand in hands:
        cards, bid = hand.split()
        hand_type = get_type(cards)
        hand_types[hand_type].append([trans(cards),bid])
    for key in hand_types:
        hand_types[key] = sorted(hand_types[key], key=lambda x: x[0])
    for key in sorted(hand_types.keys()):
        ranked_hands.extend(hand_types[key][::-1])
    winnings = [int(c[1]) * (i+1) for i, c in enumerate(ranked_hands)]
    return sum(winnings)


print(f'Part 1 answer: {part1(data)}')
print(f'Part 2 answer: {part2(data)}')
