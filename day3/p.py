f = open('input.txt', 'r')
l = f.readlines()

fabric = []
for i in range(1000):
    row = []
    for j in range(1000):
        row.append('.')
    fabric.append(row)

for line in l:
    s = line.split(' ')
    coordinates = s[2].replace(':', '')
    left, top = [int(x) for x in coordinates.split(',')]
    width, height = [int(x) for x in s[3].replace('\n', '').split('x')]

    for w in range(left, left + width):
        for h in range(top, top + height):
            if fabric[w][h] == 'X':
                continue

            if fabric[w][h] == '#':
                fabric[w][h] = 'X'
            elif fabric[w][h] == '.':
                fabric[w][h] = '#'

count = 0
for i in range(1000):
    for j in range(1000):
        if fabric[i][j] == "X":
            count += 1

print('Part 1 answer:', count)

for line in l:
    s = line.split(' ')
    coordinates = s[2].replace(':', '')
    left, top = [int(x) for x in coordinates.split(',')]
    width, height = [int(x) for x in s[3].replace('\n', '').split('x')]
    overlap = False
    for w in range(left, left + width):
        for h in range(top, top + height):
            if fabric[w][h] == 'X':
                overlap = True

    if overlap == False:
        print('Part 2 Answer:', line)
