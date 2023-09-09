def findScore(nums) -> int:
	# Length of the list
	n = len(nums)

	# Score to return
	score = 0

	# Elements that have been marked
	markedElements = set()

	# Index of smallest element
	smallestIdx = -1

	while len(markedElements) != n:

		# Smallest element
		smallestElement = float("inf")

		for i in range(n):
			if i not in markedElements and nums[i] < smallestElement: 
				smallestElement = nums[i]
				smallestIdx = i

		# Increment the score
		score += smallestElement

		# Mark the elements
		markedElements.add(smallestIdx)

		# Mark the index on left
		if smallestIdx > 0: markedElements.add(smallestIdx - 1)  

		# Mark the index on right
		if smallestIdx < n - 1: markedElements.add(smallestIdx + 1)


	# Return the score
	return score


nums = [2,1,3,4,5,2]

print("Score -> ", findScore(nums))