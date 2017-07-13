#Uses python2
v,e = map(int,raw_input().split(" "))
graph = [[] for _ in range(v)]
graph_ = graph[:]
for i in range(e):
    x,y = map(int,raw_input().split(" "))
    graph[x-1].append(y-1)
    graph_[y-1].append(x-1)
def dfs(graph):
    visited = [False]*len(graph)
    clock = 1
    pre = {}
    post = {}
    for i in range(len(graph)):
        if not visited[i]:
            explore(graph,i,clock,pre,post,visited)
    p = sorted([(post[k],k) for k in post])[::-1]
    return p
def explore(graph,i,clock,pre,post,visited):
    visited[i] = True
    pre[i] = clock
    clock += 1
    for x in graph[i]:
        if not visited[x]:
            explore(graph,x,clock,pre,post,visited)
    post[i] = clock
    clock += 1

print dfs(graph_)



