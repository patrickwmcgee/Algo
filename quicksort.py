def Quicksort(array, left, right):
	if (right>left):
	    j = Partition(array, left, right)
	    Quicksort(array, left, j-1)
	    Quicksort(array, j+1, right)
def Partition(array, left, right): 
	pivot = array[left]
	i = left
	j = right + 1  
	# this code is almost direcly from the psuedo code on the slides
	# the key difference is the while true, with the breaks because python does not support do until loops
	while(True):
	 	while(True):
	 		i += 1
	 		if not (i < right and array[i]<pivot):
	 			break
	 	while(True):
	 		j -= 1
	 		if not (left < j and array[j] > pivot):
	 			break
	 	if(i<j and array[i] >= pivot and array[j] <= pivot): 
	 		array[i], array[j] = array[j] , array[i]

	 	if not(i<j):
	 		break
	if (left <j and j<=right):
	      array[left], array[j] = array[j] , array[left]
	return  j


if __name__ == '__main__':
	# a = [100,30,40,50,22,8,13,4,7,9,10,15]
	a = [40,20,10,80,60,50,7,30,100]
	print("before", a)
	Quicksort(a, 0, len(a)-1)
	print("after", a)
	