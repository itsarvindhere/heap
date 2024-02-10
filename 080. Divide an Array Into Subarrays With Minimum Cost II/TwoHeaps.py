from heapq import heappush,heappop
def minimumCost(nums, k: int, dist: int) -> int:
        
        # Length of the list
        n = len(nums)
        
        # To keep track of the cost
        minCostSum = float("inf")
        
        # MAX HEAP
        maxHeap = []
        
        # Sum of smallest "k - 2" values on right
        minRightSum = 0
        
        # A Set to keep track of the indices of "k-2" smallest elements
        indices = set()
        
        # To Keep the candidate values that might be useful later, we can use a minHeap
        minHeap = []
        
        for i in range(2,min(dist + 2,n)):
            
            # Push current value to the maxHeap
            heappush(maxHeap, [-nums[i], -i, i])
            
            # Update the sum
            minRightSum += nums[i]
            
            # Update the set
            indices.add(i)

            # If the heap size exceeds "k - 2"
            if len(indices) > k - 2:
                
                val,_,idx = heappop(maxHeap)
                
                # Push the data to the minHeap as it might be helpful later
                heappush(minHeap, [-val, idx, idx])
                
                # Update the sum
                minRightSum -= -val
                
                # Update the set
                indices.remove(idx)
                
        # Now, we can start the main logic
        # For the second subarray, the minimum possible valid starting index is "1"
        # And the maximum possible valid starting index is "n - (k - 2) - 1"
        for i in range(1, n - (k - 2)):
            
            # REMOVE INVALID DATA FROM BOTH HEAPS
            while maxHeap and maxHeap[0][2] not in indices: heappop(maxHeap)
            while minHeap and minHeap[0][2] <= i: heappop(minHeap)
                
            # Update the minCostSum
            minCostSum = min(minCostSum, nums[0] + nums[i] + minRightSum)
            
            # Now, we increment "i"
            # What if value at index "i + 1" is present in the maxHeap? 
            # When we increment "i" to "i + 1", the value needs to be removed from the maxHeap
            # How to check if value at index "i + 1" is present in the maxHeap?
            # We can use our set for that
            if i + 1 in indices:
                
                # Reduce the sum as we will remove this element
                minRightSum -= nums[i + 1]
                
                # Remove it from the set
                indices.remove(i + 1)
                
                # Since a value is reduced from the maxHeap, we can push a value from minHeap into maxHeap
                if minHeap: 
                    
                    top = heappop(minHeap)
                    heappush(maxHeap, [-top[0], -top[2], top[2]])
                    
                    # Update the set
                    indices.add(top[2])
                    
                    # Update the sum
                    minRightSum += top[0]

            # Since "i" is incremented in next iteration, for the last subarray, 
            # the maximum possible starting index is also increased by 1
            # So, we can push the value at index "i + 1 + dist" in the maxHeap
            # Only if it is a valid index
            if i + 1 + dist < n:
                
                heappush(maxHeap, [-nums[i + 1 + dist], -(i + 1 + dist), i + 1 + dist])

                # Update sum
                minRightSum += nums[i + 1 + dist]

                # Update the set
                indices.add(i + 1 + dist)

                # If the heap size becomes > (k -2)
                if len(indices) > k - 2:

                    # Pop the value on top
                    val,_,idx = heappop(maxHeap)
                    
                    # Push the data to the minHeap as it might be helpful later
                    heappush(minHeap, [-val, idx, idx])

                    # Update the sum
                    minRightSum -= -val

                    # Update the set
                    if idx in indices: indices.remove(idx)

        # Return the minimum possible cost
        return minCostSum

nums = [10,1,2,2,2,1]
k = 4
dist = 3

print("Output ->", minimumCost(nums, k, dist))