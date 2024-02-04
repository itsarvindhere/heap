from heapq import heappush, heappop
# *************************************************************
# HELPER FUNCTION TO DELETE VALUES FROM TOP OF THE HEAPS
# *************************************************************
def lazyDelete(maxHeap, minHeap, removed):
    while maxHeap and -maxHeap[0] in removed and removed[-maxHeap[0]] > 0:
        removed[-maxHeap[0]] -= 1
        heappop(maxHeap)

    while minHeap and minHeap[0] in removed and removed[minHeap[0]] > 0:
        removed[minHeap[0]] -= 1
        heappop(minHeap)
    
def medianSlidingWindow(nums, k: int):
        
    # Output list to return
    output = []
        
    # Length of the list
    n = len(nums)
        
    # Two Heap Approach - SIMILAR LOGIC AS 295. Find Median from Data Stream
        
    # We will always push to the maxHeap first
    # At any time, we want the maxHeap to have all the values <= the values in minHeap
    # Also, we want both heaps to have equal elements if possible
    # If there are odd number of elements in a window, one heap can have one extra element
    # But, the difference in lengths cannot be more than 1
    maxHeap, minHeap = [],[]
        
    # Removed values
    removed = {}
        
    # To keep track of the sizes of the two heaps, excluding the values they have that have to be deleted
    maxHeapSize, minHeapSize = 0,0
        
    # Sliding Window
    i,j = 0,0
        
    while j < n:
            
        # LAZY DELETION
        lazyDelete(maxHeap, minHeap, removed)
                    
        # Push the current element into the maxHeap first
        heappush(maxHeap, -nums[j])
        maxHeapSize += 1
            
        # If the top of maxHeap is > than the top of minHeap (if minHeap is not empty)
        # Then we will move the top of maxHeap into the minHeap
        if minHeap and -maxHeap[0] > minHeap[0]: 
            heappush(minHeap, -heappop(maxHeap))
            maxHeapSize -= 1
            minHeapSize += 1
                
        # Make sure difference in lengths is not > 1
        if abs(maxHeapSize - minHeapSize) > 1:
                
            # If the maxHeap is bigger than minHeap
            if maxHeapSize > minHeapSize: 
                heappush(minHeap, -heappop(maxHeap))
                maxHeapSize -= 1
                minHeapSize += 1
                     
            # If the minHeap is bigger than maxHeap
            else: 
                heappush(maxHeap, -heappop(minHeap))
                maxHeapSize += 1
                minHeapSize -= 1
                
            # LAZY DELETION
            lazyDelete(maxHeap, minHeap, removed)
                
        # If the window size is not yet "k", continue
        if j - i + 1 < k: j += 1
                
        # If the window size is "k"
        else:
                
            # If k is even, then the median is always the mean of elements on top of maxHeap and minHeap
            if k % 2 == 0: output.append((-maxHeap[0] + minHeap[0]) / 2)
                    
            # If k is odd, whichever heap has an extra element, that extra element is the median
            else: output.append(-maxHeap[0] if maxHeapSize > minHeapSize else minHeap[0])
            
            # Before sliding the window from left, we need to remove element at index "i" 
            # So, add it to the "removed" dictionary
            removed[nums[i]] = removed.get(nums[i],0) + 1
                
            # If the element to remove is present in maxHeap, then after removal, maxHeap will have one less element
            # So, we reduce the "maxHeapSize"
            if nums[i] <= -maxHeap[0]: maxHeapSize -= 1
                    
            # If the element to remove is present in minHeap, then after removal, minHeap will have one less element
            # So, we reduce the "minHeapSize"
            else: minHeapSize -= 1
                
            # Move to the next window 
            i += 1
            j += 1
            
    # Return the output list
    return output

nums = [1,3,-1,-3,5,3,6,7]
k = 3

print("Output -> ", medianSlidingWindow(nums,k))