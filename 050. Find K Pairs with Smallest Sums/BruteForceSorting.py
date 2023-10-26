def kSmallestPairs(nums1, nums2, k):
        
    # Lengths
    m,n = len(nums1), len(nums2)
        
    # All the pairs
    pairs = []
        
    # For each element in first list
    for i in range(m):
        # Go over each element in second list and form a pair
        for j in range(n):
            # Put this pair in "pairs" list
            pairs.append([nums1[i], nums2[j]])
                
    # Sort the list by the sum
    pairs.sort(key = lambda x: x[0] + x[1])
        
    # Return the "k" smallest pairs
    return pairs[:k]

nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3

print("Output -> ", kSmallestPairs(nums1,nums2,k))