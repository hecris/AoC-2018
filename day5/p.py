f = open('input.txt', 'r')

content = f.read()


def react(content):
    res = content
    diff = 1

    while diff > 0:
        res = res.replace('#', '')
        c = list(res)
        diff = 0
        for i in range(len(c) - 1):
            cur = c[i]
            nex = c[i + 1]
            if cur == '#':
                continue
            if ord(cur) < 96: # lower case
                if ord(nex) == ord(cur) + 32:
                    c[i] = '#'
                    c[i + 1] = '#'
                    diff += 1
            elif ord(cur) > 96: # upper case
                if ord(nex) == ord(cur) - 32:
                    c[i] = '#'
                    c[i + 1] = '#'
                    diff += 1
   
                
        res = ''.join(c)
        
    return res

res = react(content)

print('Answer to part1:', len(res))

c = list(res)
u = set(c)
lens = []
for letter in u:
    copy = res
    copy = copy.replace(letter, '').replace(letter.upper(), '')
    lens.append(len(react(copy)))
    
print('Answer to part2', min(lens))




    
