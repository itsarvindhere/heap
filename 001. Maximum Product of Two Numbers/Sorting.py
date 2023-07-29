def maxProduct(nums) -> int:
        # All that we want is the maximum product of two numbers
        # So that means, those two numbers should be the 2 largest numbers in the list
        # Hence, we can sort the input list to get those 2 largest numbers
        nums.sort()
        
        # Now that list is sorted, return the maximum product of 2 largest numbers
        return (nums[-1] - 1) * (nums[-2] - 1)

nums = [3,4,5,2]
print("Output ->", maxProduct(nums))