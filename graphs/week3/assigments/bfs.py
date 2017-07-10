#Uses python2

v,e = map(int,raw_input().split(" "))
graph = [[] for i in range(v)]
for i in range(e):
    x,y = map(int,raw_input().split(" "))
    graph[x-1].append(y-1)
    graph[y-1].append(x-1)
p,q = map(int,raw_input().split(" "))
def bfs(graph,p,q):
	distance = [-1]*v
	distance[p-1] = 0
	queue = [p-1]
	while len(queue) != 0 :
		curr = queue.pop(0)
		for x in graph[curr]:
			if distance[x] == -1:
				queue.append(x)
				distance[x] = distance[curr] + 1
	return distance[q-1]
print bfs(graph,p,q)

