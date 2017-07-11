from Queue import PriorityQueue
v,e = map(int,raw_input().split(" "))
graph = [[] for i in range(v)]
for i in range(e):
	x,y,w = map(int,raw_input().split(" "))
	graph[x-1].append((y-1,w))
u,v = map(int,raw_input().split(" "))
def dijkstra(graph,u,v):
	distance = [float("inf")]*len(graph)
	distance[u-1] = 0
	prev = ["nil"]*len(graph)
	pq = PriorityQueue()
	pq.put((distance[u-1],u-1))
	while not pq.empty():
		curr = pq.get()[1]
		for x in graph[curr]:
			if distance[x[0]] > distance[curr] + x[1] :
				distance[x[0]] = distance[curr] + x[1]
				prev[x[0]] = curr
				pq.put((distance[x[0]],x[0]))
	return distance[v-1]
print dijkstra(graph,u,v)