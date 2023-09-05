from heapq import heappush, heappushpop


def maxScore(nums1, nums2, k: int) -> int:
        # Length of lists
        n = len(nums1)
		
        # For the minimum, we can use sorting
        # Combine the data in a single list
        nums = [(nums1[i], nums2[i]) for i in range(n)]
        
        # Sort based on nums2 value in decreasing order
        nums.sort(key = lambda x: x[1], reverse=True)
		
        # We will use a minHeap here and we want to always have at most k - 1 values in it
        # So, at any time, our minHeap will have the top k - 1 values
        minHeap = []
        
        # To keep track of the maximum possible sum of a subsequence ending at index "i"
        currSubsequenceSum = 0
        
        for i in range(k): 
            heappush(minHeap, nums[i][0])
            currSubsequenceSum += nums[i][0]
        
        # Maximum Subsequence Score (Initialize it by the score of first subsequence)
        maxScore = currSubsequenceSum * nums[k - 1][1]

        # We start our loop from k index
        for i in range(k, n):
            
            # We want to push this value "i" into the heap and increment the currSubsequenceSum by that
            # And if there is some smaller value that is removed from heap, we want to reduce the currSubsequenceSum by that
            removedVal = heappushpop(minHeap, nums[i][0])
            
            # Increment the currSubsequenceSum by nums[i][0]
            currSubsequenceSum += nums[i][0]
            
            # Decrement the currSubsequenceSum by removedVal
            currSubsequenceSum -= removedVal
            
            # Here, each "i" index represents the last index of a subsequence
            # So it is also the minimum among all
            minimum = nums[i][1]
            
            # Update the maximum Score
            maxScore = max(maxScore, currSubsequenceSum * minimum)

        # Return the Maximum Subsequence Score
        return maxScore     


nums1 = [1,3,3,2]
nums2 = [2,1,3,4]
k = 3

print("Maximum Subsequence Score -> ", maxScore(nums1, nums2, k))
