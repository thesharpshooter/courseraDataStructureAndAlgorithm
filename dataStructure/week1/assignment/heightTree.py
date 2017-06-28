#Uses python2

n = int(raw_input())
parent = map(int,raw_input().split(" "))
nodes = []
root = parent.index(-1)

child = {}
child[-1] = []
for i in range(n):
    child[i] = []

for i in range(n):
    child[parent[i]].append(i)


def getHeight(i):
    childs = child[i]
    if len(childs) == 0:
        return 1
    elif len(childs) == 1:
        return 1+getHeight(childs[0])
    else:
        return 1+max([getHeight(c) for c in childs])

print getHeight(root)
