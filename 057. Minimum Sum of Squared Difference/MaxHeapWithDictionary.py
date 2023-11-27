from heapq import heappop, heappush
from math import sqrt
def minSumSquareDiff(nums1, nums2, k1: int, k2: int) -> int:
        
        # Minimum sum to return
        minSum = 0
        
        # Length of both lists
        n = len(nums1)
        
        # Max Heap
        maxHeap = []
        
        # A Dictionary to keep the frequency of "squared difference" for each index "i"
        freq = {}
		
        for i in range(n):
            
            # What is the squared difference?
            sqDiff = (nums1[i] - nums2[i]) ** 2
            
            # Push to the maxHeap if not already present
            if sqDiff not in freq: heappush(maxHeap, -sqDiff)
            
            # Update the dictionary
            freq[sqDiff] = freq.get(sqDiff,0) + 1
            
        # How many total operations we have that we can use?
        operations = k1 + k2
    
        # While we have the operations and the maxHeap has a non zero value on top
        while -maxHeap[0] > 0 and operations > 0:
            
            # What is the maximum squared difference on top of the maxHeap?
            maxDiff = -heappop(maxHeap)
            
            # How many times this is the squared difference for different indices?
            # For this, we can use our freq dictionary
            count = freq[maxDiff]
			
            # At any time, we can use min(operations, count) operations
            operationsUsed = min(operations,count)
            
            # What will be the new squared difference
            newDiff = (sqrt(maxDiff) - 1) ** 2
            
            # If this newDiff is not already in "freq", push it to the maxHeap as well
            if newDiff not in freq: heappush(maxHeap, -newDiff)
            
            # Update "freq" dictionary with this new difference
            # The count will be "operationsUsed" since that's the number of new "newDiff" values that we now have
            freq[newDiff] = freq.get(newDiff,0) + operationsUsed
            
            # Also, reduce the count for the "maxDiff"
            freq[maxDiff] -= operationsUsed
            
            # Reduce operations
            operations -= operationsUsed
        
        # Finally, we can calculate the minimum sum of squared difference
        for key in freq: minSum += key * freq[key]
        
        # Return the minimum sum
        return int(minSum)


nums1 = [7,11,4,19,11,5,6,1,8]
nums2 = [4,7,6,16,12,9,10,2,10]
k1 = 3
k2 = 6

print("Output -> ", minSumSquareDiff(nums1,nums2,k1,k2))