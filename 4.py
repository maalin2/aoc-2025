from itertools import *
import re
import heapq
from collections import defaultdict
from collections import deque

DIRS = [
        (1, 0),
        (1, -1),
        (1, 1),
        (-1, 0),
        (-1, 1),
        (-1, -1),
        (0, 1),
        (0, -1)
]

def solve1(grid):
    good = 0

    N, M = len(grid), len(grid[0])
    for x in range(N):
        for y in range(M):
            if grid[x][y] != '@':
                continue
            rolls = 0
            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < N and 0 <= ny < M):
                    continue
                rolls += (grid[nx][ny] == '@')
            good += (rolls < 4)
    return good

def solve2(grid):
    N, M = len(grid), len(grid[0])
    q = deque()

    neighbor_count = [[0] * M for _ in range(N)]

    for x in range(N):
        for y in range(M):
            if grid[x][y] != '@':
                continue
            count = 0
            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy

                if not (0 <= nx < N and 0 <= ny < M):
                    continue
                if grid[nx][ny] == '@':
                    count += 1
            neighbor_count[x][y] = count
            if count < 4:
                q.append((x, y))

    removed = 0

    while q:
        x, y = q.popleft()
        if grid[x][y] != '@':
            continue

        grid[x][y] = '.'
        removed += 1

        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == '@':
                neighbor_count[nx][ny] -= 1
                if neighbor_count[nx][ny] == 3:
                    q.append((nx, ny))

    return removed


def parse(data):
    lines = data.split('\n')
    grid = list(map(list, lines))
    return grid


def main():
    grid = []
    with open('4-input.txt') as f:
        data = f.read().strip()
        grid = parse(data)
    soln1 = solve1(grid)
    print(soln1)
    soln2 = solve2(grid)
    print(soln2)

if __name__ == '__main__':
    main()
