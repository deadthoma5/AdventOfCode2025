from aocd.models import Puzzle
from collections import deque

def solve_part1(data):
    steps = [(d[0], int(d[1:])) for d in data.split('\n')]
    dial = deque(list(range(100)))
    dial.rotate(-50)
    result = 0
    for s in steps:
        sign = 1 if s[0] == 'L' else -1
        dial.rotate(sign * s[1])
        if dial[0] == 0:
            result += 1
    return result

def solve_part2(data):
    steps = [(d[0], int(d[1:])) for d in data.split('\n')]
    dial = deque(list(range(100)))
    dial.rotate(-50)
    result = 0
    for s in steps:
        sign = 1 if s[0] == 'L' else -1
        for n in range(s[1]):
            dial.rotate(sign)
            if dial[0] == 0:
                result += 1
    return result

puzzle = Puzzle(year=2025, day=1)
data = puzzle.input_data
print(solve_part1(data))
print(solve_part2(data))