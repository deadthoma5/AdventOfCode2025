from aocd.models import Puzzle

def parse_input(data):    
    return data.split("\n\n")[-1].replace(":", "").replace("x", " ")

def solve_part1(data):
    regions = parse_input(data)
    result = 0
    for line in regions.splitlines():
        w, h, *counts = map(int, line.split())
        if sum(counts) <= (w // 3) * (h // 3):
            result += 1
    return result

def solve_part2(data):
    return 0

if __name__ == "__main__":
    data = Puzzle(year=2025, day=12).input_data
    print(solve_part1(data))