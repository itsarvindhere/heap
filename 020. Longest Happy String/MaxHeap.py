from heapq import heappop, heappush

def longestDiverseString(a: int, b: int, c: int) -> str:
	# Output to return
	output = []

	# We can use a maxHeap here that will order a, b, and c from maximum to minimum
	maxHeap = []

	# We don't want "0" values to be in the heap going forward
	if a != 0: heappush(maxHeap, (-a, 'a'))
	if b != 0: heappush(maxHeap, (-b, 'b'))
	if c != 0: heappush(maxHeap, (-c, 'c'))

	# What was the previous character pushed to the output
	previousCharacter = "z"

	# While the heap is not empty
	while maxHeap:

		# The maximum value is the one on top of heap
		top = heappop(maxHeap)

		# Now, there are two cases

		# 1. Previous character used is not same as the top character
		if previousCharacter != top[1]:

			# In this case, we can use the character on top of heap

			# Buffer is how many occurances we have available to use
			buffer = -top[0]

			# We can use at most "2" occurances only
			occurancesUsed = min(2, buffer)

			# We use the occurances so reduce the buffer
			buffer -= occurancesUsed

			# And we will put "occurancesUsed" characters in the output
			output.append(top[1] * occurancesUsed)

			# Also update the value of previousCharacter for the next iteration
			previousCharacter = top[1]

			# If we still have some occurances available, put the character back in the heap with reduced buffer
			# Otherwise, don't put it in the heap since we want to avoid characters with "0" occurances in the heap
			if buffer != 0: heappush(maxHeap, (-buffer, top[1]))    

		# 2. Previous character used is same as the top character
		else:
			# In that case, we want to use the character with second maximum available occurances
			# If we don't have any, break. Since it is not possible to have a longer valid string at this point
			if not maxHeap: break

			# Otherwise, get the second maximum
			secondTop = heappop(maxHeap)

			# Now, do the same as above but this time, we will use only "1" occurance of this character
			# WHY?

			# Since we know that there is already a character occuring more number of time
			# So, we want to make sure we have characters to put between that other character
			# And that's why, we will use the minimum possible occurances of the second maximum character i.e., "1"
			buffer = -secondTop[0]
			buffer -= 1

			# Push only one occurance of the character in the output
			output.append(secondTop[1])

			# Update the previous character
			previousCharacter = secondTop[1]

			# If we still have some occurances available, put the character back in the heap with reduced buffer
			# Otherwise, don't put it in the heap since we want to avoid characters with "0" occurances in the heap
			if buffer != 0: heappush(maxHeap, (-buffer, secondTop[1]))

			# And also push the "top" since we had popped it in the beginning
			heappush(maxHeap, top)

	# Return the string
	return "".join(output)


a = 2
b = 4
c = 10

print(longestDiverseString(a,b,c))




