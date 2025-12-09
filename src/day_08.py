from aocd.models import Puzzle
from collections import defaultdict
from itertools import combinations

def parse_input(data):
    return [tuple(map(int, line.split(','))) for line in data.strip().splitlines()]

def solve(data, part2=False):
    coords = parse_input(data)
    coord_to_idx = {c: i for i, c in enumerate(coords)}

    # Problem spec: 10 connections for sample (20 coords), 1000 connections for real input (1000 coords)
    num_connections = 10 if len(coords) == 20 else 1000
    
    all_connections = sorted((sum((x-y)**2 for x, y in zip(c1, c2)), c1, c2) for c1, c2 in combinations(coords, 2))
    
    # Union-Find structure
    UF = list(range(len(coords)))
    def find(i):
        if UF[i] != i:
            UF[i] = find(UF[i])
        return UF[i]
    
    connections = 0
    for i, (_, c1, c2) in enumerate(all_connections):
        if part2 or i < num_connections:
            root1, root2 = find(coord_to_idx[c1]), find(coord_to_idx[c2])
            if root1 != root2:
                UF[root1] = root2
                connections += 1
                if part2 and connections == len(coords) - 1:
                    return c1[0] * c2[0]
        else:
            break
    
    sizes = defaultdict(int)
    for i in range(len(coords)):
        sizes[find(i)] += 1
    
    sorted_sizes = sorted(sizes.values(), reverse=True)
    return sorted_sizes[0] * sorted_sizes[1] * sorted_sizes[2]

def solve_part1(data):
    return solve(data)

def solve_part2(data):
    return solve(data, part2=True)

if __name__ == "__main__":
    data = Puzzle(year=2025, day=8).input_data
    print(solve_part1(data))
    print(solve_part2(data))