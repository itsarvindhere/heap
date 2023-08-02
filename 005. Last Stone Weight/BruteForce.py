def lastStoneWeight(stones) -> int:
	# Length of the list
	n = len(stones)

	# Sort the list
	stones.sort()

	# While we don't have only one stone left with us
	while len(stones) > 1: 
		# Heaviest stone
		firstHeaviest = stones.pop()

		# Second heaviest stones
		secondHeaviest = stones.pop()

		# If both are different
		if firstHeaviest != secondHeaviest:

			# The new weight
			newWeight = firstHeaviest - secondHeaviest

			# Push this new weight to the list
			stones.append(newWeight)

			# Sort the list again
			stones.sort()

	# Finally, return the weight of the only stone left
	return 0 if not stones else stones[-1]


stones = [2,7,4,1,8,1]
print("Output ->", lastStoneWeight(stones))