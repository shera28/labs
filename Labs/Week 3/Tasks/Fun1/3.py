def solve(numheads, numlegs):
    chickens = (2 * numheads - numlegs / 2)
    print(f'rabbits: {int(numheads - chickens)}, chickens: {int(chickens)}')

solve(35, 94)