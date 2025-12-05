from src.day_05 import solve_part1, solve_part2

sample = '''\
3-5
10-14
16-20
12-18

1
5
8
11
17
32'''

def test_part1():
    assert solve_part1(sample) == 3

def test_part2():
    assert solve_part2(sample) == 14