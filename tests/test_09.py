from src.day_09 import solve_part1, solve_part2

sample = '''\
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3'''

def test_part1():
    assert solve_part1(sample) == 50

def test_part2():
    assert solve_part2(sample) == 24