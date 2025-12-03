from itertools import *
import re
import heapq
from collections import defaultdict

def voltage(bank, k):
    # monotonic stack
    drop = len(bank) - k
    stack = []
    for ch in bank:
        while drop and stack and stack[-1] < ch:
            stack.pop()
            drop -= 1
        stack.append(ch)
    return int(''.join(stack[:k]))

def solve(k, banks):
    return sum(map(lambda b: voltage(b, k), banks))

def parse(data):
    banks = data.strip().split('\n')
    return banks

def main():
    banks = []
    with open('3-input.txt') as f:
        data = f.read()
        banks = parse(data)
    soln1 = solve(2, banks)
    print(soln1)
    soln2 = solve(12, banks)
    print(soln2)

if __name__ == '__main__':
    main()
