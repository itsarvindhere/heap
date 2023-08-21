from collections import Counter
from heapq import heappop, heappush
def topKFrequent(nums, k):
    # Counter
        count = Counter(nums)
        
        # We want a Min heap so as to remove all less frequent elements from top
        # And be left with only the "k" most frequent ones
        minHeap = []
        
        # For each element in the Counter
        for element, frequency in count.items():
            # Put it in heap along with its frequency
            # In the heap, the elements will be ordered based on the frequency
            heappush(minHeap, (frequency, element))
            
            # If heap size exceeds k, remove the top element
            # We want our heap to be of size "k"
            if len(minHeap) > k: heappop(minHeap)
                
        # At the end, we will be left with the top "k" frequent elements in the heap
        output = []
        while minHeap: output.append(heappop(minHeap)[1])
                
        return output

nums = [1,1,1,2,2,3]
k = 2
print("Output -> ", topKFrequent(nums,k))