from src.day_01 import solve_part1, solve_part2

sample = '''\
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82'''

def test_part1():
    assert solve_part1(sample) == 3

def test_part2():
    assert solve_part2(sample) == 6