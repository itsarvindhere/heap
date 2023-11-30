def maxSpending(values) -> int:

	# How many shops are there
	m = len(values)

	# How many items each shop has
	n = len(values[0])

	# Maximum amount that can be spent
	maxAmountSpent = 0

	# To keep track of the day
	day = 1

	# Items bought
	itemsBought = 0

	# Till we have items to buy
	while itemsBought < m * n:

		# Go over the rightmost value in each shop
		# And get the smallest among all
		itemValue = float("inf")

		# Which shop's item we are going to buy
		shop = -1

		for i in range(m):
			if values[i] and values[i][-1] < itemValue:
				itemValue = values[i][-1]
				shop = i

		# Now, buy the item on current day and add the value to the maxAmountSpent
		maxAmountSpent += itemValue * day

		# Remove the item from the shop
		values[shop].pop()

		# Increment the day
		day += 1

		# Increment hte items bought
		itemsBought += 1


	# Return the maximum amount spent
	return maxAmountSpent

values = [[10,8,6,4,2],[9,7,5,3,2]]
print("Output -> ", maxSpending(values))