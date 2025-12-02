from aocd.models import Puzzle

def parse_input(data):
    dataList = data.strip().split(',')
    return [tuple(map(int, item.split('-'))) for item in dataList]

def solve_part1(data):
    result = 0
    ranges = parse_input(data)
    for (start, end) in ranges:
        for id in range(start, end + 1):
            s = str(id)
            pattern = s[:len(s)//2]
            if s == pattern * 2:
                result += id
    return result

def solve_part2(data):
    result = 0
    ranges = parse_input(data)
    for (start, end) in ranges:
        for id in range(start, end + 1):
            s = str(id)
            for patternLength in range(1, len(s) // 2 + 1):
                pattern = s[:patternLength]
                if s == pattern * (len(s) // patternLength):
                    result += id
                    break
    return result

data = Puzzle(year=2025, day=2).input_data
print(solve_part1(data))
print(solve_part2(data))