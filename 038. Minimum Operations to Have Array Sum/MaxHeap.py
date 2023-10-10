from heapq import heappop, heappush


def halveArray(nums):
        
        # What is the total sum of the list
        totalSum = 0
        
        # The most optimal way is to choose the greatest number each time
        # And half it. So that will ensure that minimum operations are performed
        # We can use a maxHeap to keep track of the minimum number at any time
        maxHeap = []
        for num in nums: 
            totalSum += num
            heappush(maxHeap, -num)
            
        # Now we can start the main logic
        
        # How many operations were performed
        operations = 0
        
        # What is the half of the totalSum
        half = totalSum / 2
        
        # What is the reduced sum of the list after we do the operations
        # Initially, it will be same as the totalSum
        reducedSum = totalSum
        
        # The loop will run until the original sum is not reduced by at least half
        while (totalSum - reducedSum) < half:
            
            # Take the greatest number at this point
            greatest = -heappop(maxHeap)
            
            # Half it and put it back in the heap
            halfOfGreatest = greatest / 2
            heappush(maxHeap, -halfOfGreatest)
            
            # The reduced sum will get reduced by the half
            # Since we halved the greatest number in this operation
            reducedSum -= halfOfGreatest
            
            # Increment the operations
            operations += 1
        
        # Finally, return the minimum operations done
        return operations



nums = [5,19,8,1]

print("Output ->", halveArray(nums))