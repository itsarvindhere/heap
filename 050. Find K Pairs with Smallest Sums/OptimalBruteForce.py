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
                    
            currSum = nums1[i] + nums2[j]
                
            # Before we push the pair with its sum in maxHeap
            # We check the size
                
                
            # If maxHeap size is not yet "k"
            if len(maxHeap) < k:
                 # We push the pair with its sum to the maxHeap
                heappush(maxHeap, [-currSum, nums1[i], nums2[j]])
                    
            # If maxHeap size is already k
            else:
                # If the current sum is smaller than the top, we can replace top with the current pair
                if currSum < -maxHeap[0][0]:
                    heappop(maxHeap)
                    heappush(maxHeap, [-currSum, nums1[i], nums2[j]])
                        
                # But, if the current sum is greater than the top, it means
                # Not only this pair, but no other upcoming pair can now replace the top
                # Because the lists are sorted in increasing order
                # So, the next elements in both lists will be equal or greater than current elements
                # And so, we can break here because we already have "k" pairs in the heap
                elif currSum > -maxHeap[0][0]: break
                
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