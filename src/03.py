#AoC-24_03

string = ''.join([l.strip() for l in open('input/03.txt').readlines()])
p1, p2, status = 0, 0, True

for l, c in enumerate(string):
    if c == 'd': status = True if string[l:l+4] == 'do()' else False if string[l:l+7] == 'don\'t()' else status
    if l > 2 and c == '(' and string[l-3:l] == 'mul':
        r = string.find(')', l)
        nums = string[l+1:r].split(',')
        if all(num.isdigit() for num in nums) and len(nums) == 2:
            p1 += int(nums[0]) * int(nums[1])
            if status: p2 += int(nums[0]) * int(nums[1])

print(p1), print(p2)
