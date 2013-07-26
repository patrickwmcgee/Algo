def BellmanFord(graph, source):
	distance = {}
	pred = {}
	for edge in graph:
		distance[edge] = float("inf") # Thanks to stack overflow this is how you 
		pred[edge] = None 

	#initialize the source
	distance[source] = 0

	for k in range(len(graph)-1):    #note n-1 iterations every time
		for edge in graph: # in the psuedo code edge would be i
			for adj in graph[edge]: # in the psuedo code adj would be j
				if (distance[adj] > graph[edge][adj] + distance[edge]):
					distance[adj] = graph[edge][adj] + distance[edge]
					pred[adj] = edge

	return distance, pred
if __name__ == '__main__':
	# Graph containing all of the vert's and edges
	graph = {
		'1': {'3': 2, '4': 5, '2': 3},
		'2': {'1': 3, '4': 1, '5': 4},
		'3': {'1': 2, '4': 2, '6': 1},
		'4': {'1': 5, '3': 2, '5': 3, '2': 1},
		'5': {'4': 3, '6': 2, '2': 4},
		'6': {'3': 1, '5': 2}
	}
	distance, pred = BellmanFord(graph, "6")

	# very ugly printing of node name (previous, distance)
	for edge in graph:
		print('node: ', end='')
		print(edge, end='')
		print(" = ", end='')
		print('(', end='')
		print(pred[edge], end='')
		print(',', end='')
		print(distance[edge], end='')
		print(') ', end='')