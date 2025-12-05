from itertools import *
import re
import heapq
from collections import defaultdict
from collections import deque
from collections import Counter

def solve1(ranges, available):
    res = 0
    for a in available:
        for l, r in ranges:
            if l <= a <= r:
                res += 1 
                break
    return res

def solve2(ranges):
    counter = Counter()
    for l, r in ranges:
        counter[l] += 1
        counter[r + 1] -= 1
    res = 0
    prev = -1
    cur = 0
    for k in sorted(counter):
        p = cur
        cur += counter[k]
        if p == 0:
            prev = k
            continue
        res += k - prev
        prev = k

    return res 

def parse(data):
    ranges, available = [], []

    lines = data.split('\n')

    for line in lines:
        if not line:
            continue
        if '-' not in line:
            available.append(int(line))
        else: # range
            l, r = map(int, line.split('-'))
            ranges.append((l, r))

    return ranges, available

def main():
    with open('5-input.txt') as f:
        data = f.read().strip()
        ranges, available = parse(data)
        soln1 = solve1(ranges, available)
        print(soln1)
        soln2 = solve2(ranges)
        print(soln2)

if __name__ == '__main__':
    main()
