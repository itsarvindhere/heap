from heapq import heappop, heappush
from math import ceil
def maxKelements(nums, k) -> int:
        
        # Initial score
        score = 0
        
        # We want to choose an index such that we increase our score with maximum value
        # And the best way is to choose the greatest value in each operation
        # That, we can do using a maxHeap since using a maxHeap,
        # We can quickly get what is the greatest value at that time
        maxHeap = []
        
        # First, put the numbers in maxHeap
        for num in nums: heappush(maxHeap, -num)
            
        # Now, start the main logic
        while k > 0:
            
            # Take the greatest value from top of heap
            top = -heappop(maxHeap)
            
            # Increase the score by this value
            score += top
            
            # Now, put ceil(top / 3) back in the heap 
            heappush(maxHeap, -ceil(top/3))
            
            # Decrement k
            k -= 1
            
        # In the end, we will have the maximum possible score
        return score

nums = [1,10,3,3,3]
k = 3
print("Output -> ", maxKelements(nums,k))