f = open('input.txt', 'r')
content = f.readlines()

def dist(p1, p2):
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        return abs(dx) + abs(dy)
        #return (dx**2) + (dy**2)

def part2(content, num, num2, mx):
    tda = []
    for i in range(num):
        row = []
        for j in range(num):
            row.append(' ')
        tda.append(row)

    coordinates = []
    start = 1
    for c in content:
        x,y = [int(s) for s in c.split(', ')]
        x += num2
        y += num2
        tda[y][x] = start
        coordinates.append((y, x))
        start += 1

    for i in range(len(tda)):
        for j in range(len(tda)):
            cur_coor = (j, i)
            distances = []
            for c in coordinates:
                distance = dist(c, cur_coor)
                distances.append(distance)

            if sum(distances) < mx:
                tda[j][i] = "#"
            else:
                tda[j][i] = '.'
    return tda

tda = part2(content, 400, 0, 10000)
count = 0
for i in range(len(tda)):
    for j in range(len(tda)):
        if tda[i][j] == '#':
            count += 1

print(count)
