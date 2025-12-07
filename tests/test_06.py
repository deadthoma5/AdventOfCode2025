from src.day_06 import solve_part1, solve_part2

sample = '''\
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  '''

def test_part1():
    assert solve_part1(sample) == 4277556

def test_part2():
    assert solve_part2(sample) == 3263827