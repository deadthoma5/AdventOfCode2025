from aocd.models import Puzzle

def parse_input(data):
    return {device: outputs.split() 
            for line in data.strip().splitlines() 
            for device, outputs in [line.split(': ')]}

def count_paths(graph, start, end, required_nodes=None):
    memo = {}
    
    def dfs(node, visited_required):
        cache_key = (node, frozenset(visited_required))
        if cache_key in memo:
            return memo[cache_key]
        
        if node == end:
            return 1 if (required_nodes is None or visited_required == required_nodes) else 0
        
        if node not in graph:
            return 0
        
        total = sum(
            dfs(neighbor, visited_required | ({neighbor} if required_nodes and neighbor in required_nodes else set()))
            for neighbor in graph[node]
        )
        
        memo[cache_key] = total
        return total
    
    initial_visited = {start} if (required_nodes and start in required_nodes) else set()
    return dfs(start, initial_visited)

def solve_part1(data):
    return count_paths(parse_input(data), 'you', 'out')

def solve_part2(data):
    return count_paths(parse_input(data), 'svr', 'out', required_nodes={'dac', 'fft'})

if __name__ == "__main__":
    data = Puzzle(year=2025, day=11).input_data
    print(solve_part1(data))
    print(solve_part2(data))