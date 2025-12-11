from src.day_11 import solve_part1, solve_part2

sample1 = '''\
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out'''

sample2 = '''\
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out'''

def test_part1():
    assert solve_part1(sample1) == 5

def test_part2():
    assert solve_part2(sample2) == 2