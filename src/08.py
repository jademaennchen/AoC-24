#AoC-24_08

grid = [l.strip() for l in open('input/08.txt').readlines()]
nodes = [(c, y, x) for y in range(len(grid)) for x, c in enumerate(grid[y]) if c != '.']
anodes_p1, anodes_p2 = set(), set()

def inBounds(y, x):
    return 1 if 0 <= y < len(grid) and 0 <= x < len(grid) else 0

for i, (c, y, x) in enumerate(nodes):
    for (c2, y2, x2) in nodes[i+1:]:
        if c == c2:
            dy, dx, k = y2 - y, x2 - x, 0
            for k in range(50):
                if not inBounds(y2 + k*dy, x2 + k*dx): break
                if k == 1: anodes_p1.add((y2 + dy, x2 + dx))
                anodes_p2.add((y2 + k*dy, x2 + k*dx))
            for k in range(50):
                if not inBounds(y - k*dy, x - k*dx): break
                if k == 1: anodes_p1.add((y - k*dy, x - k*dx))
                anodes_p2.add((y - k*dy, x - k*dx))

print(len(anodes_p1)), print(len(anodes_p2))
