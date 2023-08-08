def maxSubsequence(nums, k) :
        
        # Since we want to preserve the order, let's also keep track of original indices
        nums = [(num,i) for i,num in enumerate(nums)]
        
        # Sort the list in decreasing order
        nums.sort(reverse=True)
        
        # We want "k" length subsequence with the largest sum
        # Basically, we want the k greatest elements in this list
        nums = nums[:k]
        
        # But we want them in the same order as they appear in original list
        # So now, we can sort again, this time in increasing order based on the indices
        nums.sort(key=lambda x: x[1])
        
        # And now, we return the final list but with only values, not indices
        return [pair[0] for pair in nums]


nums = [-1,-2,3,4]
k = 3

print("Output ->", maxSubsequence(nums,k))