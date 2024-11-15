import aocd
import re
from math import gcd

data = aocd.get_data(day=10,year=2023)
sample = """..........
.S------7.
.|F----7|.
.||OOOO||.
.||OOOO||.
.|L-7F-J|.
.|II||II|.
.L--JL--J.
.........."""

def part1(puzzle_input):
    cur = None
    matrix = None
    def xy(coor):
        return tuple(x+y for x, y in zip(cur,coor))
    
    def sym(coor):
        return matrix[coor[0]][coor[1]]
    
    directions = {(1,0):{'|':(1,0),'L':(0,1),'J':(0,-1)},
                  (-1,0):{'|':(-1,0),'F':(0,1),'7':(0,-1)},
                  (0,1):{'-':(0,1),'J':(-1,0),'7':(1,0)},
                  (0,-1):{'-':(0,-1),'L':(-1,0),'F':(1,0)}}

    matrix = [list(row) for row in puzzle_input.splitlines()]
    start = r'S'
    for i, row in enumerate(matrix):
        s = re.search(r'S',''.join(row))
        if s:
            start = (i,s.start())
            break
    cur = start
    for i in directions:
        valid = [k for k in directions[i]]
        d = i
        cur = xy(i)
        s = sym(cur)
        if s in valid:
            break
    steps = 1
    while cur != start:
        step = directions[d][s]
        d = step
        cur = xy(step)
        s = sym(cur)
        steps+=1
    return steps//2

def part2(puzzle_input):

    def boundary_points(x1, y1, x2, y2):
        # The number of boundary points between (x1, y1) and (x2, y2) is the GCD of the differences of the coordinates
        return gcd(abs(x2 - x1), abs(y2 - y1))
    
    def shoelace_formula(coords):
        n = len(coords)  # Number of vertices
        area = 0
        
        for i in range(n):
            # Get current and next vertex (wrap around using modulo)
            x1, y1 = coords[i]
            x2, y2 = coords[(i + 1) % n]
            
            # Shoelace formula summation
            area += x1 * y2 - x2 * y1
        
        return abs(area) / 2.0

    def pick_theorem(coords):
        # Step 1: Calculate area using Shoelace formula
        area = shoelace_formula(coords)
        
        # Step 2: Calculate the number of boundary points (B)
        B = 0
        n = len(coords)
        for i in range(n):
            x1, y1 = coords[i]
            x2, y2 = coords[(i + 1) % n]
            B += boundary_points(x1, y1, x2, y2)
        
        # Step 3: Use Pick's Theorem to calculate interior points (I)
        I = area - B / 2 + 1
        
        return area, I, B

    cur = None
    matrix = None

    def xy(coor):
        return tuple(x+y for x, y in zip(cur,coor))
    
    def sym(coor):
        return matrix[coor[0]][coor[1]]
    
    directions = {(1,0):{'|':(1,0),'L':(0,1),'J':(0,-1)},
                  (-1,0):{'|':(-1,0),'F':(0,1),'7':(0,-1)},
                  (0,1):{'-':(0,1),'J':(-1,0),'7':(1,0)},
                  (0,-1):{'-':(0,-1),'L':(-1,0),'F':(1,0)}}

    matrix = [list(row) for row in puzzle_input.splitlines()]
    start = r'S'
    for i, row in enumerate(matrix):
        s = re.search(r'S',''.join(row))
        if s:
            start = (i,s.start())
            break
    cur = start
    area = [cur]
    for i in directions:
        valid = [k for k in directions[i]]
        d = i
        cur = xy(i)
        s = sym(cur)
        if s in valid:
            break
    while cur != start:
        area.append(cur)
        step = directions[d][s]
        d = step
        cur = xy(step)
        s = sym(cur)
       
    #print(shoelace_formula(area))
    areas, I, B = pick_theorem(area)
    return I

#print(f'Part 1 answer: {part1(sample)}')
print(f'Part 2 answer: {part2(data)}')




