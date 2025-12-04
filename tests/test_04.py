from src.day_04 import solve_part1, solve_part2

sample = '''\
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.'''

def test_part1():
    assert solve_part1(sample) == 13

def test_part2():
    assert solve_part2(sample) == 43