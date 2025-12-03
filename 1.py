from itertools import *

# how many times does dial point at 0?
def solve(rotations):
    dial = 50
    mod = 100
    password = 0
    for rotation in rotations:
        direction = rotation[0]
        magnitude = int(rotation[1:])
        sign = 1 if direction == 'R' else -1
        # simulate
        for i in range(magnitude):
            dial += sign
            dial %= mod
            if dial == 0:
                password += 1

    return password

def main():
    rotations = []
    with open('input.txt') as f:
        data = f.read()
        rotations = data.split('\n')[:-1]
    soln = solve(rotations)
    print(soln)

if __name__ == '__main__':
    main()
