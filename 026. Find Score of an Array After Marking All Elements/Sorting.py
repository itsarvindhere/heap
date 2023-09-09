def findScore(nums) -> int:
	# Length of the list
        n = len(nums)
        
        # Score to return
        score = 0
        
        # Indices of Elements that have been marked
        markedIndices = set()
        
        # The reason why the Brute Force approach failed is -
        # In each iteration, we have to loop over the entire list to find the current smallest element
        # Instead, let's use Sorting to make the solution better
        # Basically we want the indices of the smallest elements so that's why we will keep the original indices with the elements
        # So, at each index in sortedIndices, we have a pair - (element, its original index)
        # Because when we mark the indices on left and right, we do that in the original list, not in the sorted list. Got it?
        sortedIndices = [(nums[i], i) for i in range(n)]
        sortedIndices.sort()
        
        # To keep track of the current smallest element
        # Since sortedIndices list is sorted in increasing order, initially, the smallest is at the index 0
        i = 0
        
        while len(markedIndices) != n:
            
            # Get the current smallest element
            # We use "i" to keep track of current smallest
            # So, if it is already marked in original list, we want the next smallest
            while sortedIndices[i][1] in markedIndices: i += 1
                
            # Increment the score
            score += sortedIndices[i][0]

            # Mark the elements
            markedIndices.add(sortedIndices[i][1])

            # Mark the index on left
            if sortedIndices[i][1] > 0: markedIndices.add(sortedIndices[i][1] - 1)  

            # Mark the index on right
            if sortedIndices[i][1] < n - 1: markedIndices.add(sortedIndices[i][1] + 1)
                
            # Update i
            i += 1
                
                
        # Return the score
        return score


nums = [2,1,3,4,5,2]

print("Score -> ", findScore(nums))