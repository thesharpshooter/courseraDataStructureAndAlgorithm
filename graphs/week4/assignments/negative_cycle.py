#Uses python2
v,e = map(int,raw_input().split(" "))
graph = [[] for _ in range(v)]
edges = []
neg = 0
for i in range(e):
    x,y,z = map(int,raw_input().split(" "))
    graph[x-1].append((y-1,z))
    edges.append((x-1,y-1,z))
    if z<0:
        neg += 1

def bellmanFord(graph,edges,neg,s):
    if neg == 0:
        return 0
    before = []
    distance = [float("inf")]*len(graph)
    distance[s] = 0
    for i in range(len(graph)):
        if i == len(graph)-1:
            before = distance[:]
        for x in edges:
            if distance[x[1]] > distance[x[0]]+x[2]:
                distance[x[1]] = distance[x[0]] + x[2]
    return int(not (before==distance))
temp = []
for i in range(v):
	temp.append(bellmanFord(graph,edges,neg,i))
print int(0 not in temp)


