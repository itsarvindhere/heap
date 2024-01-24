from heapq import heappush, heappop
def maxPerformance(n: int, speed, efficiency, k: int) -> int:

	# Mod
	mod = 10**9 + 7

	# Maximum performance value to return
	maxPerformanceValue = 0

	# Aggregate the two lists
	data = [[efficiency[i], speed[i]] for i in range(n)]

	# Sort the list in increasing order, based on efficiency
	data.sort()

	# Go over each engineer in the "data" list from left to right
	for i in range(n):

		# The minimum efficiency among the "k" engineers
		# This will be minimum because the list is sorted based on efficiency from smallest to largest
		minEfficiency = data[i][0]

		# To keep track of the sum of speeds of the "k" engineers
		sumOfSpeeds = data[i][1]

		# Go over all the choices on the right side of "i"
		# And pick at most "k - 1" engineers with highest speed
		# A Min Heap to get the k - 1 highest speed values
		minHeap = []

		for j in range(i + 1, n):

			# Push the speed value to the minHeap
			heappush(minHeap, data[j][1])

			# If heap size exceeds "k - 1", pop
			if len(minHeap) > (k - 1): heappop(minHeap)

		# At this point, minHeap has the "k - 1" largest speed values
		# Add them to the "sumOfSpeeds"
		while minHeap: sumOfSpeeds += heappop(minHeap)

		# Update the maximum performance accordingly
		maxPerformanceValue = max(maxPerformanceValue, sumOfSpeeds * minEfficiency)

	# Return the maximum performance
	return maxPerformanceValue % mod

n = 6
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k = 2

print("Output -> ", maxPerformance(n,speed,efficiency,k))