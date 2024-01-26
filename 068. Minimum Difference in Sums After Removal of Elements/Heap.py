from heapq import heappush, heappop
def minimumDifference(nums) -> int:
        
        # How many elements to remove
        n = len(nums) // 3
        
        # Minimum Difference to return
        minDiff = float("inf")
        
        # To efficiently get the sum of "n" smallest elements on the left of an index, we will use a Max Heap
        # To efficiently get the sum of "n" largest elements on right of an index, we will use a Min Heap
        # And we will make sure the sizes of both these heaps don't exceed "n"
        minHeap, maxHeap = [],[]
        
        # To keep the sum of "n" elements on the left of each index that can be a partition index
        leftSum = [0] * len(nums)
        
        # To keep the sum of "n" elements on the right of each index that can be a partition index
        rightSum = [0] * len(nums)
        
        # Sum of "n" smallest elements on the left
        nSmallestSum = 0
        
        # Our loop will run till the index "2n"
        # Why "2n"?
        # Because, a value "leftSum[i]" simply means the sum of n smallest numbers on the left of i (including i itself)
        # And since we are doing it for the "first part", the second part also needs to have "n" numbers in it
        # And so, the "leftSum" will be calculated only till the index "2n - 1" because after that we have exactly "n" numbers left
        # So the baseline is that we want to make sure we have at least "n" numbers on the right of an index 
        # so that those can be part of the second part
        for i in range(2 * n):
            
            # Add the current value to the nSmallestSum
            nSmallestSum += nums[i]
            
            # We want the maxHeap to have at least "n" numbers in it
            # Only then we can start calculating the sum of n smallest numbers
            # In other words, if we have nums = [7,9,5,8,1,3], here, n = 2
            # So, to get sum of "n" smallest numbers, we need the maxHeap to have "2" numbers
            # And so, we will first put the numbers "7" into the maxHeap
            # But still, we cannot yet calculate the sum of "2" smallest numbers
            # Then, we will push "9" into the maxHeap
            # And since now we have "2" numbers in the maxHeap, we can calculate the sum
            
            # So, from index 0 to "n - 1" (not including n - 1), we just want to push to the heap
            if i < n - 1: 
                heappush(maxHeap, -nums[i])  
                
            # But, from the index n - 1 to the index 2n (not including 2n), we want to calculate the sum
            else:
            
                heappush(maxHeap, -nums[i])
                
                # Make sure the heap size never exceeds "n"
                # If it does, remove the top element
                if len(maxHeap) > n:
                    removedVal = -heappop(maxHeap)
                    nSmallestSum -= removedVal
                
                # Update the leftSum list for the current index
                leftSum[i] = nSmallestSum
        
        # Sum of "n" largest elements on the right
        nLargestSum = 0
        
        # The logic is the same as for nSmallestNumbers but just in reverse
        # For the nLargest Numbers, we went from index 0 to 2n
        # Here, we will go from the last index to n
        for i in range(len(nums) - 1, n - 1, -1):
            
            nLargestSum += nums[i]
            
            if i > len(nums) - n:
                heappush(minHeap, nums[i])
            else:
                heappush(minHeap, nums[i])
            
                if len(minHeap) > n:
                    removedVal = heappop(minHeap)
                    nLargestSum -= removedVal
                    
                rightSum[i] = nLargestSum
                
        # Now, we will find the minimum difference possible
        for i in range(n - 1, 2 * n): 
            # Any index "i" here represents the point at which we will divide the list into two parts
            # So, from the index [0,i] we want to get the sum of n smallest elements. That is leftSum[i]
            # And from the index [i + 1, length - 1] we want to get the sum of the n largest elements. That is rightSum[i+1]
            # And the difference between the two is the difference between the first part and second part, if we partition at "i"
            # So, update the minimum difference accordingly
            minDiff = min(minDiff,leftSum[i] - rightSum[i + 1])
        
        # Return the minimum difference
        return minDiff

nums = [7,9,5,8,1,3]

print("Output -> ", minimumDifference(nums))