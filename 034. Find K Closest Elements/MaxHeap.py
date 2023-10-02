from heapq import heappop, heappush


def findClosestElements(arr, k: int, x: int):

	# Since we want the "K" closest integers
	# Those will be the "K" integers with the least difference with "x"
	# So, we want to order elements with their differences from greatest to smallest
	# Hence, we can use a maxHeap here for that
	maxHeap = []

	# Length of the list
	n = len(arr)

	# Go over each element in the list
	for i in range(n):
		# Put it in the maxHeap with its difference with "x"
		heappush(maxHeap, (-abs(arr[i] - x), -i, arr[i])) 

		# If heap size exceeds "k", then pop from the heap
		if len(maxHeap) > k: heappop(maxHeap)

	# Finally, the maxHeap will have the "k" closest elements to "x"
	# Output list to return
	output = []
	while maxHeap: output.append(heappop(maxHeap)[2])

	# Output should also be sorted in ascending order
	output.sort()

	# Finally, return the output
	return output

arr = [1,2,3,4,5]
k = 4
x = 3
print("Output -> ", findClosestElements(arr,k,x))