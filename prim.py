#!/usr/bin/python
from heapq import *

def prim(graph, start_node, end_node):
	minQueue = []
	mst = []
	connected = set({start_node})
	total_distance = 0
	#begin put all start_nodes edges into the queue
	for dest, value in graph[start_node].items():
		heappush(minQueue,(value,start_node,dest))

	# while the number of visited nodes is less than the number of total nodes
	while(len(connected) < len(graph.keys())):
		lowest = heappop(minQueue) # get the lowest item in the priority queue
		dist = lowest[0]
		vert_from = lowest[1]
		vert_to = lowest[2]
		if vert_to not in connected:
			connected.add(vert_to)	# add the visited item to the list
			mst.append((vert_from,vert_to,dist)) # append the step to the mst list
			total_distance += dist
			for dest,value in graph[vert_to].items():
				heappush(minQueue,(value,vert_to,dest)) # push the edges of the item we popped onto the queue

	return mst, total_distance

if __name__ == '__main__':
	# Graph containing all of the vert's and edges
	graph = {
	"A": {'B': 3, 'D': 4, 'C': 5},
	"B": {'A': 3, 'E': 3, 'F': 6},
	"C": {'A': 5, 'D': 2, 'G': 4},
	"D": {'A': 4, 'C': 2, 'E': 1, 'H': 5},
	"E": {'B': 3, 'D': 1, 'F': 2, 'I': 4},
	"F": {'B': 6, 'E': 2, 'J': 5},
	"G": {'C': 4, 'H': 3, 'K': 6},
	"H": {'D': 5, 'G': 3, 'I': 6, 'K': 7},
	"I": {'E': 4, 'H': 6, 'L': 5, 'J': 3},
	"J": {'F': 5, 'I': 3, 'L': 9},
	"K": {'G': 6, 'H': 7, 'I': 8},
	"L": {'K': 8, 'I': 5, 'J': 9}
	}
	mst = prim(graph,'A','L')
	print(mst)