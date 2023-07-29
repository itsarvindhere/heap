from heapq import heappop, heappush


def maxProduct(nums) -> int:
        # Since all we want is the "2" largest numbers in the list
        # We can use a heap and maintain its size as "2"
        # This will be a minHeap so elements on top will be smaller than elements on bottom
        # In this way, we can remove all the smaller elements to have the 2 largest elements at the end
        minHeap = []
        
        # Go through the list
        for num in nums:
            
            # Push the element in the heap
            heappush(minHeap, num)
            
            # If the heap size exceeds 2, pop the top element
            if len(minHeap) > 2: heappop(minHeap)
                
        # Finally, return the product of the two elements in the heap
        # Since these are the two largest elements in the input list
        return (minHeap[0] - 1) * (minHeap[1] - 1)

nums = [3,4,5,2]
print("Output ->", maxProduct(nums))