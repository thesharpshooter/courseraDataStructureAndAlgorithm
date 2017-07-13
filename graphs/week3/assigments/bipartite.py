#Uses python2
v,e = map(int,raw_input().split(" "))
graph = [[] for _ in range(v)]
for i in range(e):
	x,y = map(int,raw_input().split(" "))
	graph[x-1].append(y-1)
	graph[y-1].append(x-1)
def bipartite(graph):
	queue = [0]
	distance = [-1]*v
	distance[0] = 0
	temp = [0]
	while len(queue) != 0 :
		curr = queue.pop(0)
		temp.pop(0)
		temp = graph[curr]
		for x in graph[curr]:
			if distance[x] == -1:
				queue.append(x)
				distance[x] = distance[curr] + 1
			elif (distance[x] == distance[curr]):
				return 0

	return 1
print bipartite(graph)
