from aocd.models import Puzzle
from itertools import product
import numpy as np

EPSILON = 1e-9  # Floating-point tolerance for numerical comparisons
MAX_FREE_VARS_SEARCH = 20  # Limit search space for systems with free variables

def parse_lights(lights_str):
    return lights_str.strip('[]').translate(str.maketrans('#.', '10'))

def parse_buttons(buttons_str, num_lights):
    indices = set(int(x) for x in buttons_str.strip('()').split(','))
    return ''.join('1' if i in indices else '0' for i in range(num_lights))

def parse_joltages(joltages_str):
    return [int(x) for x in joltages_str.strip('{}').split(',')]

def parse_input(data):
    result = []
    for line in data.strip().splitlines():
        parts = line.split()
        lights = parse_lights(parts[0])
        buttons = [parse_buttons(b, len(lights)) for b in parts[1:-1]]
        joltages = parse_joltages(parts[-1])
        result.append((lights, buttons, joltages))
    return result

def solve_lights(lights, buttons):
    n_lights, n_buttons = len(lights), len(buttons)
    button_matrix = np.array([[int(c) for c in b] for b in buttons])
    augmented = np.column_stack([button_matrix.T, [int(c) for c in lights]])
    pivot_cols, row = [], 0
    
    # Gaussian elimination to RREF over GF(2)
    # GF(2) = binary numbers, addition is XOR (^), multiplication is AND (&)
    for col in range(n_buttons):
        pivot_row = next((r for r in range(row, n_lights) if augmented[r, col] & 1), None)
        if pivot_row is None:
            continue
        
        pivot_cols.append(col)
        if pivot_row != row:
            augmented[[row, pivot_row]] = augmented[[pivot_row, row]]
        
        for r in range(n_lights):
            if r != row and augmented[r, col] & 1:
                augmented[r] ^= augmented[row]
        row += 1
    
    # Check for inconsistent equations (0 = 1 in GF(2))
    if any(augmented[r, -1] & 1 for r in range(row, n_lights)):
        return -1
    
    free_vars = [i for i in range(n_buttons) if i not in set(pivot_cols)]
    
    # Unique solution case
    if not free_vars:
        return sum(augmented[r, -1] for r in range(len(pivot_cols)))
    
    min_weight = float('inf')
    for free_vals in product([0, 1], repeat=len(free_vars)):
        solution = np.zeros(n_buttons, dtype=int)
        solution[free_vars] = free_vals
        
        for r in range(len(pivot_cols) - 1, -1, -1):
            col = pivot_cols[r]
            solution[col] = (augmented[r, -1] + sum(augmented[r, c] * solution[c] for c in range(col + 1, n_buttons))) & 1
        
        min_weight = min(min_weight, solution.sum())
    
    return min_weight if min_weight != float('inf') else -1

def solve_joltages(buttons, joltages):
    n_machines = len(joltages)
    n_buttons = len(buttons)
    
    A = np.array([[int(buttons[b][m]) for b in range(n_buttons)] for m in range(n_machines)], dtype=float)
    augmented = np.column_stack([A, joltages])
    
    pivot_cols, row = [], 0
    for col in range(n_buttons):
        pivot_row = next((r for r in range(row, n_machines) if abs(augmented[r, col]) > EPSILON), None)
        if pivot_row is None:
            continue
        
        pivot_cols.append(col)
        if pivot_row != row:
            augmented[[row, pivot_row]] = augmented[[pivot_row, row]]
        
        pivot = augmented[row, col]
        augmented[row] = augmented[row] / pivot
        
        for r in range(n_machines):
            if r != row and abs(augmented[r, col]) > EPSILON:
                augmented[r] = augmented[r] - augmented[r, col] * augmented[row]
        row += 1
    
    # Check for inconsistent equations
    if any(abs(augmented[r, -1]) > EPSILON for r in range(row, n_machines)):
        return -1
    
    free_vars = [i for i in range(n_buttons) if i not in set(pivot_cols)]
    
    # Unique solution case
    if not free_vars:
        solution_vals = [int(round(augmented[r, -1])) for r in range(len(pivot_cols))]
        return sum(solution_vals) if all(v >= 0 for v in solution_vals) else -1
    
    min_weight = float('inf')
    for free_vals in product(range(MAX_FREE_VARS_SEARCH), repeat=len(free_vars)):
        solution = np.zeros(n_buttons, dtype=float)
        solution[free_vars] = free_vals
        
        for r in range(len(pivot_cols) - 1, -1, -1):
            col = pivot_cols[r]
            solution[col] = augmented[r, -1] - sum(augmented[r, c] * solution[c] for c in range(col + 1, n_buttons))
        
        rounded = np.round(solution)
        if np.all(np.abs(solution - rounded) < EPSILON) and np.all(rounded >= 0):
            weight = int(rounded.sum())
            min_weight = min(min_weight, weight)
    
    return min_weight if min_weight != float('inf') else -1

def solve_part1(data):
    return sum(solve_lights(lights, buttons) for lights, buttons, _ in parse_input(data))

def solve_part2(data):
    return sum(solve_joltages(buttons, joltages) for _, buttons, joltages in parse_input(data))

if __name__ == "__main__":
    data = Puzzle(year=2025, day=10).input_data
    print(solve_part1(data))
    print(solve_part2(data))