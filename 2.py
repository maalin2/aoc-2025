from itertools import *
import re

def solve(rgs):
    res = 0
    for rg in rgs:
        for x in rg:
            # match any repeat group of digits at least twice with a backref
            m = re.search(r'^(\d+)\1+$', str(x))
            if m:
                match = int(m.group(0))
                res += match
    return res

def parse(data):
    split = data.strip().split(',')
    ranges = []
    for x in split:
        l, r = map(int, (x.split('-')))
        ranges.append(range(l, r + 1))
    return ranges

def main():
    ranges = []
    with open('2-input.txt') as f:
        data = f.read()
        ranges = parse(data)
    soln = solve(ranges)
    print(soln)

if __name__ == '__main__':
    main()
