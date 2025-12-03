from aocd.models import Puzzle
from functools import reduce

def parse_input(data):
    return data.split('\n')

def max_substring(bank, batteryCount):
    bankSize = len(bank)
    dropSize = bankSize - batteryCount
    stack = []
    for digit in bank:
        while dropSize and stack and stack[-1] < digit:
            stack.pop()
            dropSize -= 1
        stack.append(digit)
    return "".join(stack[:batteryCount])

def solve_part1(data):
    banks = parse_input(data)
    return sum(int(max_substring(b, 2)) for b in banks)

def solve_part2(data):
    banks = parse_input(data)
    return sum(int(max_substring(b, 12)) for b in banks)

data = Puzzle(year=2025, day=3).input_data
print(solve_part1(data))
print(solve_part2(data))