#AoC-24_02

reps = [list(map(int, l.strip().split())) for l in open('input/02.txt').readlines()]

def check_rep(rep):
    if rep[0] > rep[1]: rep = rep[::-1]
    return all(1 <= rep[j+1] - rep[j] <= 3 for j in range(len(rep) - 1))

p1 = sum(check_rep(rep) for rep in reps)
p2 = sum(any(check_rep(rep[:j]+ rep[j+1:]) for j in range(len(rep))) for rep in reps)

print(p1), print(p2)
