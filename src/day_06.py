from aocd.models import Puzzle
import operator
from functools import reduce

def transpose(grid):
    return list(zip(*grid))

def parse_input(data):
    grid = data.splitlines()
    breakpoints = [i for i, ch in enumerate(grid[-1]) if ch in '+*'] + [len(grid[0]) + 1]
    chunksgrid = [[grid[r][breakpoints[i]:breakpoints[i + 1] - 1] for i in range(len(breakpoints) - 1)] for r in range(len(grid))]
    return transpose(chunksgrid)

def apply_operator(nums, symbol):
    ops = {
        '+': operator.add,
        '*': operator.mul,
    }
    return reduce(ops[symbol], nums)

def solve_part1(data):
    return sum(apply_operator([int(x.strip()) for x in row[:-1]], row[-1].strip()) for row in parse_input(data))

def solve_part2(data):
    grid = [[int(''.join(chunk[i] for chunk in row[:-1]).strip()) for i in range(len(row[0]))] + [row[-1].strip()] for row in parse_input(data)]
    return sum(apply_operator(row[:-1], row[-1]) for row in grid)

if __name__ == "__main__":
    data = Puzzle(year=2025, day=6).input_data
    print(solve_part1(data))
    print(solve_part2(data))