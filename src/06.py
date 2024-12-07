#AoC-24_06

grid = [list(l.strip()) for l in open('input/06.txt').readlines()]
start = [(y, x) for y in range(len(grid)) for x in range(len(grid[y])) if grid[y][x] == '^'][0]
p1, p2 = 0, 0

def sim_guard(grid, start):
    (y, x), d_y, d_x, tiles, visited = start, -1, 0, set(), set()
    while(True):
        tiles.add((y, x))
        visited.add((y, x, d_y, d_x))
        if not(0 <= y+d_y < len(grid) and 0 <= x+d_x < len(grid[0])): return len(tiles)
        if grid[y+d_y][x+d_x] == '#': d_y, d_x = d_x, -d_y
        else: y, x = y+d_y, x+d_x
        if (y, x, d_y, d_x) in visited: return 0

p1 = sim_guard(grid, start)
for y, x in [(y, x) for y in range(len(grid)) for x in range(len(grid[y])) if grid[y][x] == '.']:
    grid[y][x] = '#'
    if not sim_guard(grid, start): p2 += 1
    grid[y][x] = '.'

print(p1), print(p2)
