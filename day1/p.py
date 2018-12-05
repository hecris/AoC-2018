f = open('input.txt', 'r')

def part1():
    res = 0
    for i in f.readlines():
        res += int(i)

    print(res)

def part2():
    l = [int(x) for x in f.readlines()]
    freqs = []
    cur = 0
    i = 0
    while True:
        if i == len(l):
            i = 0
        change = l[i]
        freqs.append(cur)
        cur += change
        i += 1
        if cur in freqs:
            return cur

print(part2())
