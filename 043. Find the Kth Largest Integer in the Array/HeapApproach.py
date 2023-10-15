from heapq import heappop, heappush
def kthLargestNumber(nums, k) -> str:
    # Min Heap with size maintained as at most "k"
    minHeap = []
        
    # Loop over the list
    for num in nums: 
        # Push the current number in the heap
        heappush(minHeap, int(num))
            
        # If heap size exceeds k, pop
        if len(minHeap) > k: heappop(minHeap)
        
    # Finally, the kth largest will be on top of the heap
    return str(minHeap[0])

nums = ["2","21","12","1"]
k = 3

print("Output -> ", kthLargestNumber(nums,k))