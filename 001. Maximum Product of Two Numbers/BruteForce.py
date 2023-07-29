def maxProduct(nums) -> int:
        # Maximum Product to return
        maximumProduct = 0
        
        # Length of the input list
        n = len(nums)
        
        # In the brute force approach, we will take each index
        # And then multiply that element with every other element on its right
        # And update the maximum product
        
        # For every index "i"
        for i in range(n):
            # Go through every index on right
            for j in range(i + 1, n):
                # Get the product
                currProduct = (nums[i]-1)*(nums[j]-1)
                
                # Update the maximum product
                maximumProduct = max(maximumProduct, currProduct)
                
        # Finally, return the maximum product
        return maximumProduct

nums = [3,4,5,2]
print("Output ->", maxProduct(nums))