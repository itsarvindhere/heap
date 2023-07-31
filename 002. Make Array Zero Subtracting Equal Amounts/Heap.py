from heapq import heapify, heappop, heappush


def minimumOperations(nums) -> int:
        # Minimum operations
        operations = 0
        
        # Convert the input list to a MinHeap 
        # to efficiently get the minimum element ( greater than 0) at any time
        heapify(nums)
        
        # Sum of minimum elements so far
        sumOfMinimums = 0
        
        while nums:
            
            # Remove zeros if any
            while nums and nums[0] == 0: heappop(nums)
                
            # At this point, if nums is not empty
            # Then top element is the smallest element at this point
            if nums:
                
                # Smallest non-zero element - O(LogN)
                smallestElement = heappop(nums)
                
                # Sum of minimum elements so far
                sumOfMinimums += smallestElement
                
                # Remove all the elements that are equal or less than sumOfMinimums
                # Those all will be 0 when we are at this operation
                while nums and nums[0] <= sumOfMinimums: heappop(nums)
                    
                # If heap is not empty yet, then reduce the top element by sumOfMinimums
                if nums: 
                    # Pop the top element - O(LogN)
                    topElement = heappop(nums)
                    
                    # Push (topElement - sumofMinimums) to the heap - O(LogN)
                    heappush(nums, topElement - sumOfMinimums)
                    
                # Increment the operations
                operations += 1
        
        # Return the operations required
        return operations

nums = [1,5,0,3,5]

print("Output ->", minimumOperations(nums))