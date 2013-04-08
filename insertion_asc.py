#!/usr/bin/python
def insertion_sort_asc(list):
	for j in range(len(list)):
		key = list[j]
		i = j - 1
		while (i >= 0 and list[i] > key):
			list[i + 1] = list[i]
			i = i - 1
		list[i + 1] = key


