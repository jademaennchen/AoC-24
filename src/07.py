#AoC-24_07

eqs = [list(map(int, nums.split())) + [int(goal)] for goal, nums in [l.strip().split(': ') for l in open('input/07.txt').readlines()]]
for eq in eqs:
    print(eq)

valid = lambda cur, eq: max(valid(cur+eq[0], eq[1:]), valid(cur*eq[0], eq[1:])) if len(eq) != 1 else eq[0] if eq[0] == cur else 0
valid_c = lambda cur, eq: max(valid_c(cur+eq[0], eq[1:]), valid_c(cur*eq[0], eq[1:]), valid_c(int(str(cur)+str(eq[0])), eq[1:])) if len(eq) != 1 else eq[0] if eq[0] == cur else 0

p1 = sum([valid(eq[0], eq[1:]) for eq in eqs])
p2 = sum([valid_c(eq[0], eq[1:]) for eq in eqs])

print(p1, p2)
