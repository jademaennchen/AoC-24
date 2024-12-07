#AoC-24_01

lines = open('input/01.txt').readlines()
left, right = sorted(list(map(int, [l[5:] for l in lines]))), sorted(list(map(int,[l.strip()[:-5] for l in lines])))

p1 = sum([abs(l - r) for l, r in zip(left, right)])
p2 = sum([l * right.count(l) for l in left])

print(p1), print(p2)
