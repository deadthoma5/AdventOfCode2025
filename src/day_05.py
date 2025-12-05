from aocd.models import Puzzle

def parse_input(data):
    top, bottom = data.split('\n\n')
    ranges = list(tuple(map(int, r.split('-'))) for r in top.strip().split('\n'))
    IDs = list(map(int, bottom.strip().split('\n')))
    return ranges, IDs

def merge_intervals(intervals):
    sorted_intervals = sorted(intervals)
    merged = [sorted_intervals[0]]
    for start, end in sorted_intervals[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))
    return merged

def solve_part1(data):
    ranges, IDs = parse_input(data)
    return sum(1 for id in IDs if any(start <= id <= end for (start, end) in ranges))

def solve_part2(data):
    ranges, _ = parse_input(data)
    return sum(end - start + 1 for (start, end) in merge_intervals(ranges))

if __name__ == "__main__":
    data = Puzzle(year=2025, day=5).input_data
    print(solve_part1(data))
    print(solve_part2(data))