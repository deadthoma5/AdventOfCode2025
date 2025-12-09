from aocd.models import Puzzle
from itertools import combinations, starmap, compress
from shapely import Polygon, box

def parse_input(data):
    return [tuple(map(int, line.split(','))) for line in data.strip().splitlines()]

def solve_part1(data):
    coords = parse_input(data)
    areas = [(abs(x2 - x1) + 1) * (abs(y2 - y1) + 1) for (x1, y1), (x2, y2) in combinations(coords, 2)]
    return max(areas)

def solve_part2(data):
    coords = parse_input(data)
    rects = [(min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)) 
             for (x1, y1), (x2, y2) in combinations(coords, 2)]
    areas = [(x2 - x1 + 1) * (y2 - y1 + 1) for x1, y1, x2, y2 in rects]
    poly = Polygon(coords)
    return max(compress(areas, map(poly.contains, starmap(box, rects))))

if __name__ == "__main__":
    data = Puzzle(year=2025, day=9).input_data
    print(solve_part1(data))
    print(solve_part2(data))