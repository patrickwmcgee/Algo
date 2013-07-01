#!/usr/bin/python


def dfs(graph,start_vert):
	stack = [] # going to use a python list as a stack, using append for push and pop
	explored_path = []
	discovered_nodes = []
	stack.append(start_vert)
	# while the stack is not equal to the empty list []
	while(stack != []):
		t = stack.pop()	
		
		# if the vertext t from the stack is not in the explored path, add it
		if t not in explored_path:
			explored_path.append(t)
		# add all of the neighbors of t onto the stack if they are not already in the path
		for v in graph[t]:
			if v not in explored_path:
				discovered_nodes.append(v)
				stack.append(v)
	return explored_path

#Using the Wikipedia verison of topological sorting
def top_sort(graph):
	sorted_list = []
	# the list of unmarked nodes are the verts / keys in the graph
	unmarked_nodes = list(graph.keys())
	discovered = []
	
	def visit(v):
		if v in discovered:
			print("NOT A DAG")
			return
		else:
			#mark the node as discovered
			discovered.append(v)
			# remove the node from the unmarked list
			unmarked_nodes.remove(v)
			for e in graph[v]:
				visit(e)
			#discovered.remove(v)
			sorted_list.insert(0,v)

	#Loop while there are unmarked nodes
	while (unmarked_nodes != []):
		visit(unmarked_nodes[0])
	
	return sorted_list
def top_sort_new(graph):
	sorted_list = []
	queue = []
	next = 0

	# create indegree list
	indegree = calc_indegree(graph)
	# go through indegree list and take the ones that have an indegree of 0 and put them onto the list / stack
	for key,val in indegree.items():
		if val == 0:
			queue.append(key)
			sorted_list.append(key)

	while(queue != []):
		# Get item out of queue/stack
		popped = queue.pop()
		next += 1
		for v in graph[popped]:
			indegree[v] -= 1
			if indegree[v] == 0:
				queue.append(v)
				sorted_list.append(v)


	if len(sorted_list) != len(graph.keys()):
		return "Not a DAG"
	else:
		return sorted_list
def calc_indegree(graph):
	indegree = {}
	for v in graph:
		indegree[v] = 0
	for v in graph:
		for e in graph[v]:
				indegree[e] += 1
	return indegree

if __name__ == '__main__':
	graph = {
	"A": [],
	"B": ["G" , "C"],
	"C": ["A"],
	"D": ["B", "G"],
	"E": ["D","G"],
	"F": ["D", "B", "E"],
	"G": ["C","A"]
	}
	cyclic_graph = {
	"A": [],
	"B": ["G" , "C","D"],
	"C": ["A"],
	"D": ["B", "G", "C"],
	"E": ["D","G"],
	"F": ["D", "B", "E"],
	"G": ["C","A"]
	}

	# print(graph)
	# print(dfs(graph, "F"))
	# # print(dfs(graph, "A"))
	# # print(dfs(cyclic_graph, "F"))
	# print(top_sort(graph))
	# print(top_sort(cyclic_graph
	# print(calc_indegree(graph))
	print(top_sort_new(graph))
	print(top_sort_new(cyclic_graph))