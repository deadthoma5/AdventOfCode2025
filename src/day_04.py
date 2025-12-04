from aocd.models import Puzzle
from itertools import product

OFFSETS = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

def parse_input(data):
    lines = data.splitlines()
    R, C = len(lines), len(lines[0])
    return {(r, c) for r, c in product(range(R), range(C)) if lines[r][c] == '@'}

def neighbors(pos):
    r, c = pos
    return {(r + dr, c + dc) for dr, dc in OFFSETS}

def solve_part1(data):
    grid = parse_input(data)
    return sum(1 for pos in grid if len(neighbors(pos) & grid) < 4)

def solve_part2(data):
    grid = parse_input(data)
    initialSize = len(grid)
    while True:
        removal = {pos for pos in grid if len(neighbors(pos) & grid) <  4}
        if not removal:
            break
        grid -= removal
    return initialSize - len(grid)

if __name__ == "__main__":
    data = Puzzle(year=2025, day=4).input_data
    print(solve_part1(data))
    print(solve_part2(data))