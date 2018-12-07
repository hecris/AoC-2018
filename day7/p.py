# didn't actually need to use nodes
class Node():
    def __init__(self, val):
        self.val = val
        self.prereqs = []

def make_dict(l):
    d = {}
    for i in l:
        d[i.val] = i.prereqs
    return d

def alpha(l):
    ords = []
    for i in l:
        ords.append(ord(i))
    return l[ords.index(min(ords))]

f = open('input.txt', 'r')
content = f.readlines()

def part1():
    l = []
    for i in content:
        s = i.split()
        prereq, this = [x for x in s if len(x) == 1]
        nodes = [x.val for x in l]
        if this in nodes:
            node = l[nodes.index(this)]
            node.prereqs.append(prereq)
        else:
            node = Node(this)
            node.prereqs.append(prereq)
            l.append(node)

    d = make_dict(l)
    possible_heads = []
    for v in d.values():
        for n in v:
            if n not in d.keys() and n not in possible_heads:
                possible_heads.append(n)

    for p in possible_heads:
        d[p] = []

    head = alpha(possible_heads)
    path = []

    while True:
        if head not in path:
            path.append(head)
        for k,v in d.items():
            if head in v:
                d[k].remove(head)

        possible = []

        for k,v in d.items():
            if len(v) == 0:
                possible.append(k)
        if len(possible) == 0:
            break
        
        nex = alpha(possible)
        del d[nex]
        head = nex


    print(''.join(path))

part1()
