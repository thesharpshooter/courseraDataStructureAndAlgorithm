#Uses python2
n = int(raw_input())
x = map(int,raw_input().split(" "))
parent = {}
nodes = {}
root = {}
for i in range(n):
    parent[i] = x[i]
    nodes["node"+str(i)] = {"key":i,"child":[]}
    if x[i] == -1:
        root = nodes["node"+str(i)]
for x in parent:
    if parent[x]!= -1:
        nodes["node"+str(parent[x])]["child"].append(int(x))
    

for x in nodes:
    print nodes[x]

print root

def getHeight(root):
    if len(root['child'] == 0 ):
        return 1
    else :
        return 1 + max([getHeight(nodes['node'+str(x)]['child']) for x in ])
