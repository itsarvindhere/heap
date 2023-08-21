from collections import Counter
def topKFrequent(nums, k):
    # Counter for counting frequencies of each element
	count = Counter(nums)

	# List of elements and their counts as tuples
	countList = []
	for key in count: countList.append((count[key], key))

	# Now, we can sort the list based on the count in Decreasing order
	countList.sort(reverse=True)

	# Output List to return
	output = []
	for i in range(k): output.append(countList[i][1])

	return output

nums = [1,1,1,2,2,3]
k = 2
print("Output -> ", topKFrequent(nums,k))