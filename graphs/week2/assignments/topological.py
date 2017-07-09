#Uses python2

v,e = map(int,raw_input().split(" "))
graph = [[] for _ in range(v)]
for i in range(e):
    x,y = map(int,raw_input().split(" "))
    graph[x-1].append(y-1)

visited = [False]*v
clock = 1
previsit = {}
postvisit = {}
def dfs():
    for i in range(v):
        if not visited[i]:
            explore(i)
def explore(i):
    global graph
    global clock
    global visited
    global previsit
    global postvisit
    visited[i] = True
    previsit[i] = clock
    clock += 1
    for x in graph[i]:
        if not visited[x]:
            explore(x)
    postvisit[i] = clock
    clock += 1

dfs()
post = []
for x in postvisit:
    post.append((postvisit[x],x))
post = sorted(post)[::-1]
for i in post:
    print i[1]+1,
