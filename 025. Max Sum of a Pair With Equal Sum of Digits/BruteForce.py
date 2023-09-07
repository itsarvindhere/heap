def maximumSum(nums) -> int:

	# Length of the list
	n = len(nums)

	# Maixmum Sum value to return
	maxVal = -1

	# Go over each number
	for i in range(n):

		# Current max Sum
		currMax = -1

		# What is the sum of its digits
		digitSumi = 0
		num = nums[i]
		while num > 0:
			remainder = num % 10
			digitSumi += remainder
			num = num // 10

		# Go over every other number
		for j in range(n):

			# If it is not same
			if i != j:

				# Get the sum of its digits
				digitSumj = 0
				num = nums[j]
				while num > 0:
					remainder = num % 10
					digitSumj += remainder
					num = num // 10

				# If sum is same
				if digitSumi == digitSumj: currMax = max(currMax, nums[i] + nums[j])

		# Update the overall max
		maxVal = max(maxVal, currMax)

	# Return the maximum value
	return maxVal


nums = [18,43,36,13,7]
print("Output -> ", maximumSum(nums))