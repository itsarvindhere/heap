def maxProduct(nums) -> int:
        # All that we are looking for is the first greatest and second greatest element in the list
        # And that can be found without sorting or using a heap
        
        # Initialize first greatst and second greatest by -1
        firstGreatest, secondGreatest = -1,-1
        
        # Go through the numbers
        for num in nums:
            
            # If the current element is greater than firstGreatst
            if num > firstGreatest:
                # Then this first greatest will now be the second greatest
                # Since we now have a number greater than it
                secondGreatest = firstGreatest
                
                # And now update the first greatest by current number
                firstGreatest = num
                
            # Otherwise, if the current element is not greater than first greatest
            # But it is greater than second greatest
            # Then it means we found a new second greatest
            # Hence, update accordingly
            elif num > secondGreatest: secondGreatest = num
        
        # Return the product
        return (firstGreatest - 1) * (secondGreatest - 1)

nums = [3,4,5,2]
print("Output ->", maxProduct(nums))