#AoC-24_05

bl = {}
for i, j in [l.strip().split('|') for l in open('input/05.txt').readlines() if l.count('|') > 0]:
    bl[i] = [j] if i not in bl else bl[i] + [j]
updates = [l.strip().split(',') for l in open('input/05.txt').readlines() if l.count(',') > 0]
p1, p2 = 0, 0

for ud in updates:
    if all(a not in bl[b] for i, a in enumerate(ud) for b in ud[i+1:]): p1 += int(ud[len(ud)//2])
    else:
        for i, n in enumerate(ud):
            j = min([ud.index(m) for m in bl[n] if m in ud]) if any(m in ud for m in bl[n]) else i
            if j < i: ud = ud[:j] + ud[i:i+1] + ud[j:j+1] + ud[j+1:i] + ud[i+1:]
        p2 += int(ud[len(ud)//2])

print(p1), print(p2)
