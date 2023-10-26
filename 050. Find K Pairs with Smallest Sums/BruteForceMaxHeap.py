from heapq import heappop, heappush


def kSmallestPairs(nums1, nums2, k):
     # Output list
    output = []
        
    # Lengths
    m,n = len(nums1), len(nums2)
        
    # Instead of getting all the pairs
    # Let's just get the "k" pairs with smallest sum
    # We will use a maxHeap for that
    # Why maxHeap? because we want to discard all the pairs with larger sum values
    maxHeap = []
        
    # For each element in first list
    for i in range(m):
        # Go over each element in second list and form a pair
        for j in range(n):
            # Put this pair in maxHeap with the "sum" 
            heappush(maxHeap, [-(nums1[i] + nums2[j]), nums1[i], nums2[j]])
                
            # If heap size exceeds k, pop
            if len(maxHeap) > k: heappop(maxHeap)
                
    # Now, just populate the output list
    while maxHeap:
        top = heappop(maxHeap)
        output.append([top[1], top[2]])
        
    # Return the "k" smallest pairs
    return output

nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3

print("Output -> ", kSmallestPairs(nums1,nums2,k))