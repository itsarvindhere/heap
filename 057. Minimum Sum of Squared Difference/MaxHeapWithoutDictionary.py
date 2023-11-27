from heapq import heappop, heappush
def minSumSquareDiff(nums1, nums2, k1: int, k2: int) -> int:
        
        # Minimum sum to return
        minSum = 0
        
        # Length of both lists
        n = len(nums1)
		
        # Max Heap to get the pair with the maximum contribution at any time
        maxHeap = []
        
        for i in range(n):
            val = (nums1[i] - nums2[i]) ** 2
            if val > 0: heappush(maxHeap, [-val, i])
        
        # While we have k1 or k2
        while maxHeap and (k1 > 0 or k2 > 0):
            
            # Which index is contributing the largest value at this point
            i = heappop(maxHeap)[1]
            
            # If both the numbers at this index are same, 
            # then we alrady have minimum possible value for this index, that is 0
            # So, skip if that's the case
            if nums1[i] == nums2[i]: continue
            
            # If we have k1 (that is, we can increment of decrement the value at nums1[i])
            if k1 > 0:
                
                # If nums1[i] is greater than nums2[i], it needs to be decremented to reduce the overall difference
                # Otherwise, it needs to be incremented to reduce the overall difference
                nums1[i] = nums1[i] - 1 if nums1[i] > nums2[i] else nums1[i] + 1
                k1 -= 1
            
            # If we no longer have k1 but we have k2, then we can increment of decrement value at nums2[i]
            else:
                # If nums2[i] is greater than nums1[i], it needs to be decremented to reduce the overall difference
                # Otherwise, it needs to be incremented to reduce the overall difference
                nums2[i] = nums2[i] - 1 if nums2[i] > nums1[i] else nums2[i] + 1
                k2 -= 1
            
            # Now, we push back the new squared difference for these two values in the maxHeap
            heappush(maxHeap, [-((nums1[i] - nums2[i]) ** 2), i])
                    
        # Finally, take the values from maxHeap and add them to the minSum
        while maxHeap: minSum += -heappop(maxHeap)[0]
        
        # Return the minimum sum
        return minSum


nums1 = [7,11,4,19,11,5,6,1,8]
nums2 = [4,7,6,16,12,9,10,2,10]
k1 = 3
k2 = 6

print("Output -> ", minSumSquareDiff(nums1,nums2,k1,k2))