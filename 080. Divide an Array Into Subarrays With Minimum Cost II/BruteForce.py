from heapq import heappush,heappop
def minimumCost(nums, k: int, dist: int) -> int:

	# Length of the list
	n = len(nums)

	# To keep track of the cost
	minCostSum = float("inf")

	# The minimum possible starting index for second subarray is index "1"
	# So, go over each valid starting index for second subarray
	# The maximum valid starting index for second subarray is the one after which we have at least "k - 2" elements left
	for i in range(1, n - (k - 2)):

		# To keep track of the sum of costs of current divison of subarrays
		# First subarray will always have cost = nums[0]
		# Second subarray cost is nums[i] since "i" is the starting index
		costSum = nums[0] + nums[i]

		# Now, from the remaining elements on right, we want the "k - 2" smallest elements
		# For that, we can use a maxHeap and fix its max size as "k - 2"
		maxHeap = []

		# To keep track of the minimum sum of "k-2" elements on right of "i"
		minSumOnRight = 0

		# For the "kth" subarray, the maximum possible valid starting index is "i + dist"
		for j in range(i + 1, min(i + dist + 1,n)):

			# Push current value to the maxHeap
			heappush(maxHeap, -nums[j])

			# Update the sum
			minSumOnRight += nums[j]

			# If the heap size exceeds "k-2"
			if len(maxHeap) > k - 2:
				# Pop the top and also update the sum accordingly
				minSumOnRight -= -heappop(maxHeap)

		# Finally, update the current sum of costs
		costSum += minSumOnRight

		# Update the minimum sum of costs
		minCostSum = min(minCostSum, costSum)

	# Return the minimum possible cost
	return minCostSum

nums = [10,1,2,2,2,1]
k = 4
dist = 3

print("Output ->", minimumCost(nums, k, dist))