#!/usr/bin/python


def dfs(graph,start_vert):
	stack = [] # going to use a python list as a stack, using append for push and pop
	explored_path = []
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
				stack.append(v)
	return explored_path


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
	print(graph)
	print(dfs(graph, "F"))