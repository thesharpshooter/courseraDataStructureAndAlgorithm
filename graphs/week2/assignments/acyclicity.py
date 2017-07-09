#Uses python2
v,e = map(int,raw_input().split(" "))
graph = [[] for i in range(v)]
for i in range(e):
    x,y = map(int,raw_input().split(" "))
    graph[x-1].append(y-1)

visited = [False]*(len(graph))
previsit= {}
postvisit = {}
clock = 1
stack = []
cyclic = False
def dfs(graph):
    for i in range(len(graph)):
        if not visited[i]:
            explore(i)

def explore(i):
    global stack
    global visited
    global cyclic
    global clock
    global previsit
    global postvisit
    stack.append(i)
    visited[i] = True
    previsit[i] = clock
    clock += 1
    for x in graph[i]:
        if visited[x] and x in stack:
            cyclic = True
        if not visited[x]:
            explore(x)
    stack.pop(stack.index(i))
    postvisit[i] = clock
    clock += 1
dfs(graph)
print int(cyclic)


