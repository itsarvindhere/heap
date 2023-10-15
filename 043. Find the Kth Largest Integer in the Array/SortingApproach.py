def kthLargestNumber(nums, k) -> str:
    # Sort the list in decreasing order
    nums.sort(key = lambda x: int(x), reverse = True)
        
    # And now, return the kth largest
    return nums[k - 1]

nums = ["2","21","12","1"]
k = 3

print("Output -> ", kthLargestNumber(nums,k))