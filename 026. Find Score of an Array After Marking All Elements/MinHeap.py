from heapq import heappop, heappush


def findScore(nums) -> int:
	# Length of the list
        n = len(nums)
        
        # Score to return
        score = 0
        
        # Indices of Elements that have been marked
        markedIndices = set()
        
        # We can also use a minHeap here and it will work the same as a sorted list did
        minHeap = []
        for i in range(n): heappush(minHeap, (nums[i], i))
            
        # The only change is we no longer have to use a pointer to keep track of smallest element
        # We know the smallest will always be on top of the minHeap
        while len(markedIndices) != n:
            
            # Get the current smallest element from top of the minHeap
            # If it is already marked in original list, we want the next smallest
            while minHeap[0][1] in markedIndices: heappop(minHeap)
                
            # Smallest
            smallestPair = heappop(minHeap)
                
            # Increment the score
            score += smallestPair[0]

            # Mark the elements
            markedIndices.add(smallestPair[1])

            # Mark the index on left
            if smallestPair[1] > 0: markedIndices.add(smallestPair[1] - 1)  

            # Mark the index on right
            if smallestPair[1] < n - 1: markedIndices.add(smallestPair[1] + 1)
                
                
        # Return the score
        return score


nums = [2,1,3,4,5,2]

print("Score -> ", findScore(nums))