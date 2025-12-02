#AoC-24_10

grid = [l.strip() for l in open('input/10.txt').readlines()]
zeros = [(y, x) for y in range(len(grid)) for x in range(len(grid))  if grid[y][x] == '0']
dir, p2 = ((1, 0), (-1, 0), (0, 1), (0, -1)), 0

def in_bounds(y, x):
    return 1 if 0 <= y < len(grid) and 0 <= x < len(grid) else 0

def traverse(y, x, next):
    global p2
    if grid[y][x] != str(next): return set()
    if grid[y][x] == '9':
        p2 += 1
        return set([(y, x)])
    return set().union(*[traverse(y + dy, x + dx, next + 1) for dy, dx in dir if in_bounds(y + dy, x + dx)])

p1 = sum([len(traverse(y, x, 0)) for y, x in zeros])
    
print(p1), print(p2)
