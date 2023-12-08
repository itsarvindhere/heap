from heapq import heappush, heappop
def minimumDeviation(nums) -> int:
        
        # Length of the list
        n = len(nums)
        
        # Max Heap
        maxHeap = []
        
        # Minimum number in the list
        minimumVal = float("inf")

        # Convert all odd numbers to even by doing one multiply operation
        for i in range(n):
            
            # Convert
            if nums[i] % 2 != 0: nums[i] *= 2
                
            # Push the number to the maxHeap
            heappush(maxHeap, -nums[i])
            
            # Update the minimum number if required
            minimumVal = min(minimumVal, nums[i])
        
        # Minimum Deviation that we have to return
        # Initialize it with the difference between the maximum and the minimum element
        minDeviation = -maxHeap[0] - minimumVal
        
        # While the greatest value in the maxHeap is even number
        # We can keep doing the divide operations on the greatest value
        # As soon as the greatest is an odd number, we stop
        # Because note that we only care about one operation and that's the divide operation
        while maxHeap[0] % 2 == 0:
            
            # The top of heap has the maximum value
            maximumVal = -heappop(maxHeap)
            
            # Now, we apply a divide operation on this maximumVal
            maximumVal //= 2
            
            # Now, after applying this divide operation, this value might be the new minimum
            # So, update accordingly
            minimumVal = min(minimumVal, maximumVal)
            
            # And we push back the value in the maxHeap
            heappush(maxHeap, -maximumVal)
            
            # Update the minimum deviation
            minDeviation = min(minDeviation, -maxHeap[0] - minimumVal)
        
        # Finally, return the Minimum Deviation
        return minDeviation

nums = [4,1,5,20,3]
print("Minimum Deviation ->", minimumDeviation(nums))