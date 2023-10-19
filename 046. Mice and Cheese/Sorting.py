def miceAndCheese(reward1, reward2, k: int) -> int:
	# Points
	points = 0

	# Types of cheese
	n = len(reward1)

	# Let's first combine the two lists into one
	reward = [[reward1[i], reward2[i]] for i in range(n)]

	# Now, we sort this list on the basis of "reward1[i] - reward2[i]" difference from maximum to minimum
	reward.sort(key = lambda x : x[0] - x[1], reverse = True)

	# First mouse eats "k" type of cheese
	i = 0
	while i < k:
		points += reward[i][0]
		i += 1

	# Now, the rest of the cheese is eaten by second mouse
	while i < n:
		points += reward[i][1]
		i += 1

	# Finally, return the points
	return points

reward1 = [1,1,3,4]
reward2 = [4,4,1,1]
k = 2

print("Output ->", miceAndCheese(reward1, reward2, k))
