f = open('input.txt', 'r')
content = f.readlines()

def dist(p1, p2):
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        return abs(dx) + abs(dy)
        #return (dx**2) + (dy**2)
    
def part1(content, num, num2):
    tda = []
    for i in range(num):
        row = []
        for j in range(num):
            row.append('a')
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
            if cur_coor in coordinates:
                continue
            distances = []
            for c in coordinates:
                distance = dist(c, cur_coor)
                distances.append(distance)


            if distances.count(min(distances)) > 1:
                tda[j][i] = '.'
            else:
                tda[j][i] = distances.index(min(distances))

    d = {}
    for i in range(len(tda)):
        for j in range(len(tda)):
            d.setdefault(tda[i][j], 0)
            d[tda[i][j]] += 1
    print('done')
    return d

d1 = part1(content, 380, 22)
d2 = part1(content, 500, 24)

finites = []
for k in d1.keys():
    if d1[k] == d2[k]:
        finites.append(d1[k])

answer1 = max(finites)
print(answer1)

