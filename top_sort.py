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

def top_sort(graph):
	sorted_list = []
	stack = []

	# create indegree list
	indegree = calc_indegree(graph)

	# go through indegree list and take the ones that have an indegree of 0 and put them onto the stack
	for key,val in indegree.items():
		if val == 0:
			stack.append(key)
			sorted_list.append(key)

	while(stack != []):
		# Get item out of stack
		popped = stack.pop()

		for v in graph[popped]:
			indegree[v] -= 1
			# if the indegree is 0 add it to the stack to process and then add it to the final path
			if indegree[v] == 0:
				stack.append(v)
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
	print(top_sort(graph))
	print(top_sort(cyclic_graph))