from heapdict import heapdict
import math

def parse(filename, adjList):
	'''
	Parses the data in filename into an adjacency list
	
	Parameters
	
	filename: contains the graph data in the form:
	parent child weight\n
	
	adjList: the adjacency list (dict) in which graph edge data will be stored
	'''
	adjList.clear()
	lines = [line.rstrip('\n') for line in open(filename)] #writing into array code is from internet
	min = math.inf
	max = 0
	for line in lines:
		edgeArray = line.split(" ")
		edgeArray = list(map(int, edgeArray))
		if edgeArray[0] < min:
			min = edgeArray[0]
		if edgeArray[0] > max:
			max = edgeArray[0]
		if edgeArray[0] not in adjList:
			adjList[edgeArray[0]] = {}
		adjList[edgeArray[0]][edgeArray[1]] = edgeArray[2]

	for potential_sink in range(min, max+1):
		if potential_sink not in adjList:
			adjList[potential_sink] = {}
	
def dijkstra(adjList, root, result):
	'''
	Given a graph's adjacency list and a root node, for all verticies u in graph, 
	result[u][0] will contain the length of the shortest path from the root to u and
	result[u][1] will contain a path of such a shortest path.
	'''
	#hd will act as our priority queue, where distance values to nodes act as keys
	hd = heapdict()
	previous = {}
	for vertex in adjList:
		result[vertex] = [ math.inf , [] ]
	result[root][0] = 0
	previous[root] = root
	
	for node_val in range(1,len(result)+1):
		hd[node_val] =  result[node_val][0]
	while(len(hd) > 0):
		u, dist_u = hd.popitem()
		for v in adjList[u]:
			if result[v][0] > dist_u + adjList[u][v]:
				result[v][0] = dist_u + adjList[u][v]
				hd[v] = result[v][0]
				previous[v] = u
	for vertex in previous:
	 	u = vertex
	 	result[vertex][1].insert(0,u)
	 	while(u != previous[u]):
	 		result[vertex][1].insert(0,previous[u])
	 		u = previous[u]

if __name__ == '__main__':
	#input graph file and starting node
	filename = input("graph file name (or 1 for Lab6.txt, 2 for rome99.txt): ")
	if filename == "1":
		filename = "Lab6.txt"
	elif filename == "2":
		filename = "rome99.txt"
	adjList = {}
	parse(filename, adjList)

	root = int(input("root number: "))
	# result will store the number associated with its distance form the root
	# and the path to get there
	result = {}
	dijkstra(adjList, root, result)
	action = input("enter row number (or all to print all): ")
	if action == "all":
		print(result)
	else:
		action = int(action)
		print("Length: ", result[action][0])
		print("Path: ", result[action][1])