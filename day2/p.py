f = open('input.txt', 'r')
l = f.readlines()

count2 = 0
count3 = 0
for i in l:
    for letter in i:
        if i.count(letter) == 2:
            count2 += 1
            break

for i in l:
    for letter in i:
        if i.count(letter) == 3:
            count3 += 1
            break

print('checksum:', count2 * count3)

# part 2
print('\npart2\n')
for i in l:
    for j in l:
        diffs = []
        diff = 0
        for n in range(len(j)):
            if i[n] != j[n]:
                diff += 1
                diffs.append(i[n])

        if diff == 1:
            print(diffs)
            print(i)
            print(j)
