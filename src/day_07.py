from aocd.models import Puzzle
from collections import defaultdict

def parse_input(data):
    grid = data.strip().splitlines()
    beams = {(r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == 'S'}
    splitters = {(r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == '^'}
    return beams, splitters, len(grid)

def simulate(beams, splitters, ROWS):
    counts = defaultdict(int)
    splits = 0
    
    for beam in beams:
        counts[beam] = 1
    
    while beams and all(r < ROWS - 1 for r, c in beams):
        newBeams = set()
        for r, c in beams:
            nr = r + 1
            if (nr, c) in splitters:
                splits += 1
                for nc in [c - 1, c + 1]:
                    newBeams.add((nr, nc))
                    counts[(nr, nc)] += counts[(r, c)]
            else:
                newBeams.add((nr, c))
                counts[(nr, c)] += counts[(r, c)]
        beams = newBeams
    
    return splits, counts

def solve_part1(data):
    beams, splitters, ROWS = parse_input(data)
    splits, _ = simulate(beams, splitters, ROWS)
    return splits

def solve_part2(data):
    beams, splitters, ROWS = parse_input(data)
    _, counts = simulate(beams, splitters, ROWS)
    return sum(counts[key] for key in counts if key[0] == ROWS - 1)

if __name__ == "__main__":
    data = Puzzle(year=2025, day=7).input_data
    print(solve_part1(data))
    print(solve_part2(data))