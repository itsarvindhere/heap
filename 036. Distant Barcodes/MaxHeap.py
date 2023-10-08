from collections import Counter
from heapq import heappop, heappush

def rearrangeBarcodes(barcodes):

	# The most optimal way to arrange the barcodes is such that
	# We give priority to the barcode that occurs most number of times
	# And between two such barcodes, we will place a barcode that is occuring second most time
	# So, to keep track of this efficiently, we will use a maxHeap

	# First, let's get the frequencies
	freq = Counter(barcodes)

	# Max Heap
	maxHeap = []
	for key in freq: heappush(maxHeap, (-freq[key], key))

	# Now, we can start creating the output list
	output = []

	while maxHeap:

		# What is the top barcode
		top = heappop(maxHeap)

		# If previous barcode is not same as top, we can push the top barcode to output
		if not output or output[-1] != top[1]:
			output.append(top[1])

			# Reduce the frequency of top barcode
			freq[top[1]] -= 1

			# If the frequency becomes 0, no need to push it back in maxHeap
			# Else, push it back with the new frequency
			if freq[top[1]] != 0: heappush(maxHeap, (-freq[top[1]], top[1]))

		# If the previous barcode was the same as top, we cannot push the top barcode to output
		# In this case, we will push the barcode that appears second most times
		else:
			secondTop = heappop(maxHeap)

			# Now do the same as above
			output.append(secondTop[1])

			# Reduce the frequency of second top barcode
			freq[secondTop[1]] -= 1

			# If the frequency becomes 0, no need to push it back in maxHeap
			# Else, push it back with the new frequency
			if freq[secondTop[1]] != 0: heappush(maxHeap, (-freq[secondTop[1]], secondTop[1]))

			# And finally, since we popped the top barcode in the beginning, push it back as well
			heappush(maxHeap, top)

	# And finally, we return the Output list
	return output


barcodes = [1,1,1,1,2,2,3,3]

print("Output -> ", rearrangeBarcodes(barcodes))