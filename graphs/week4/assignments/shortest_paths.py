#Uses python2
v,e = map(int,raw_input().split(" "))
graph = [[] for i in range(v)]
edges = []
for i in range(e):
    x,y,z = map(int,raw_input().split(" "))
    graph[x-1].append((y-1,z))
    edges.append((x-1,y-1,z))
s = int(raw_input())-1
before = []

def bfs(graph,s,visited):
    visited[s] = True
    q = [s]
    while len(q) != 0:
        curr = q.pop(0)
        for x in graph[curr]:
            if not visited[x[0]] :
                visited[x[0]] = True
                q.append(x[0])
    return visited


def bellmanford(graph,edges,s):
    distance = [float("inf")]*len(graph)
    pre = ["nil"]*len(graph)
    distance[s] = 0
    for i in range(len(graph)):
        if i == len(graph)-1 :
            before = distance[:]
        for x in edges:
            if distance[x[1]] > distance[x[0]] + x[2]:
                distance[x[1]] = distance[x[0]] + x[2]
                pre[x[1]] = x[0]
    return before,distance
before,after = bellmanford(graph,edges,s)
changed = []
for i in range(v):
    if before[i] != after[i]:
        changed.append(i)
visited = [False]*v
for x in changed:
    visited = bfs(graph,x,visited)
for i in range(v):
    if visited[i] :
        print "-"
    else :
        if before[i] == float("inf"):
            print "*"
        else:
            print before[i]
    

