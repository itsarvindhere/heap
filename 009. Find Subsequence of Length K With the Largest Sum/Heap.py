from heapq import heappop, heappush


def maxSubsequence(nums, k) :
        
        # The issue with Sorting is that we have to sort the whole list
        # Just to get the k greatest elements
        # Imagine what if we already have a sorted list as input
        # In that case, we would unnecessarily be sorting the list again
        
        # Here, we can make use of a heap and maintain its size as "k"
        # And it would be a minHeap so that we can discard all the smaller values
        heap = []
        
        # Just as in sorting approach, we will push both the number and its index in the heap
        for i,num in enumerate(nums):
            heappush(heap, (num,i))
            
            # If the size of heap exceeds k, pop from it
            if len(heap) > k: heappop(heap)

        # Finally, we can sort the heap based on original indices
        heap.sort(key = lambda x: x[1])
        
        # And return just the values, not the indices
        return [pair[0] for pair in heap]


nums = [-1,-2,3,4]
k = 3

print("Output ->", maxSubsequence(nums,k))