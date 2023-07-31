def minimumOperations(nums) -> int:
        
        # In the Brute Force approach, let's do just what the problem says to do
        # Without thinking of how fast the solution is or how efficient it is
        
        # Minimum operations
        operations = 0
        
        # Minimum Element initially which is not zero
        minElement = float("inf")
        
        for num in nums: 
            if num > 0 and num < minElement: minElement = num
                
        # Now, we go over the list
        # Flag to know whether we performed an operation to substract or not
        # If we did not, it would mean all elements are now 0
        # Initially, we set it to true so that the loop runs at least once
        flag = True
        
        while flag:
            # Now reset it back to False
            # We are using this while loop as a do while basically
            # So that it runs at least once
            flag = False
            
            # Now, we will loop over our list
            # And if we find a number that is > 0, we substract the minElement from it
            # To reduce the amount of work we have to do
            # We will also keep track of the new minimum element after we reduce the values
            newMinimum = float("inf")
            
            for i,num in enumerate(nums):
                # If the current element is greater than 0
                if num > 0:
                    # Reduce it by "minElement"
                    # And, set this as the new value at index "i"
                    nums[i] = num - minElement
                    
                    # ALso update the newMinimum if required (Only if new nums[i] is not 0)
                    if nums[i] > 0: newMinimum = min(newMinimum, nums[i])
                    
                    # And since we did perform the operation here, make the flag as True
                    flag = True
                    
            # When the loop ends, if flag is true, that means we did perform the operation
            # So, update the operations count
            if flag: operations += 1
                
            # And don't forget to update the minimum element
            # Because, the minElement always points to previous minimum
            # But after we substract "minElement" from all values of the list
            # There may be a new Minimum element that is not necessarily same as "minElement"
            # It could be greater than "minElement" or smaller than "minElement"
            # But still, going forwards, it is the new minimum for the list now
            minElement = newMinimum
        
        # Return the operations required
        return operations


nums = [1,5,0,3,5]

print("Output ->", minimumOperations(nums))