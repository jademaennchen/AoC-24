#AoC-24_08

line, data_p1, data_p2 = open('input/09.txt').readlines()[0].strip(), [], []
for i, c in enumerate(line):
    data_p1 += (int(c) * [i//2] if i % 2 == 0 else int(c) * [None])
    data_p2.append([i//2, int(c)] if i % 2 == 0 else [None, int(c), []])

i, j = 0, len(data_p1) - 1
while(i < j):
    if data_p1[j] == None:
        j -= 1
        continue
    if data_p1[i] == None:
        data_p1[i] = data_p1[j]
        j -= 1
    i += 1
data_p1 = data_p1[:j+1]

for idx, i in enumerate(data_p2[::-1]):
    if i[0] == None: continue
    for j in data_p2[:-idx-1]:
        if j[0] == None and j[1] - len(j[2]) >= i[1]:
            j[2] += i[1] * [i[0]]
            i[0] = 0
            break
data_p2 = [i[0] if i[0] != None else i[2][j] if j < len(i[2]) else 0 for i in data_p2 for j in range(i[1])]

p1 = sum(i * c if c != None else 0 for i, c in enumerate(data_p1))
p2 = sum(i * c for i, c in enumerate(data_p2))

print(p1, p2)
