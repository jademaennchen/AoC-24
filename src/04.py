#AoC-24_04

grid = [l.strip() for l in open('input/04.txt').readlines()]
p1, p2 = 0, 0

for x, y in [(x, y) for x in range(len(grid)) for y in range(len(grid[0]))]:
    for dx, dy in [(dx, dy) for dx in [0, 1, -1] for dy in [0, 1, -1]]:
        if grid[x][y] == 'X' and 0 <= x + 3*dx < len(grid) and 0 <= y + 3*dy < len(grid[0]):
            if grid[x + dx][y + dy] == 'M' and grid[x + 2*dx][y + 2*dy] == 'A' and grid[x + 3*dx][y + 3*dy] == 'S': p1 += 1

for x, y in [(x, y) for x in range(len(grid)) for y in range(len(grid[0]))]:
        if grid[x][y] == 'A' and 0 < x < len(grid)-1 and 0 < y < len(grid[0])-1:
            cross = [grid[x+1][y+1], grid[x-1][y-1], grid[x+1][y-1], grid[x-1][y+1]]
            if grid[x+1][y+1] != grid[x-1][y-1] and cross.count('M') == cross.count('S') == 2: p2 += 1

print(p1), print(p2)
