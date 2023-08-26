def kthLargestValue(matrix, k: int) -> int:

	# m and n
	m = len(matrix)
	n = len(matrix[0])

	# List to keep all the XOR values
	# There will be m * n values
	xorValues = []

	# Go over each cell
	for a in range(m):
		for b in range(n):

			xorVal = 0

			# Get the XOR value for this cell
			for i in range(a + 1):
				for j in range(b + 1): xorVal ^= matrix[i][j]

			# Put the value in the list
			xorValues.append(xorVal)

	# Sort in decreasing order
	xorValues.sort(reverse=True)

	# Return the "kth" largest Xor Value
	return xorValues[k - 1]


matrix = [[10,9,5], [2,0,4], [1,0,9], [3,4,8]]

print("Output -> ", kthLargestValue(matrix, 4))