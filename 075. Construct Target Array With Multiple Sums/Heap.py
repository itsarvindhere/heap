from heapq import heappop, heappush
def isPossible(arget) -> bool:
        
        # Length
        n = len(target)
		
		# If there is only one element, then only if it is 1, it can be converted
        if n == 1: return target[0] % 2 != 0
        
        # What is the total sum of the target list at any time
        totalSum = 0
        
        # Instead of taking an initial array with all 1s and try to convert it to target array
        # We can try to do the opposite. That is, take the target array and try to convert it to an array of all 1s
        # If we can do it, it means we can return True
        
        # A Max Heap to get the largest element efficiently
        maxHeap = []
        for val in target:
            totalSum += val
            heappush(maxHeap, -val)
        
        # While the largest element in the heap is > 1
        while -maxHeap[0] > 1:
            
            # What is the largest element at this point?
            largestElement = -heappop(maxHeap)
            
            # What is the sum except the largestElement?
            totalSum -= largestElement
            
			# Largest element cannot be <= remaining sum
            if largestElement <= totalSum: return False
            
            # What do we need to push back into the maxHeap?
            newVal = largestElement % totalSum
            
            # If remaining sum is > 1 and the newVal is 0, then not possible
            # For example, [2,4]
            if totalSum > 1 and newVal == 0: return False
            
            # If remaining sum is "1", then it will always be possible
            # For example, [1,doesn't matter what we have here]
            if totalSum == 1: return True
            
            # Update the totalSum after we replace the "largestElement" with the "newVal"
            totalSum += newVal
            
            # Push to the maxHeap
            heappush(maxHeap, -newVal)
        
        # It is possible
        return True

target = [9,3,5]
print("Outpt => ", isPossible(target))