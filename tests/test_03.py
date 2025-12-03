from src.day_03 import solve_part1, solve_part2

sample = '''\
987654321111111
811111111111119
234234234234278
818181911112111'''

def test_part1():
    assert solve_part1(sample) == 357

def test_part2():
    assert solve_part2(sample) == 3121910778619