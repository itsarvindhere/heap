def minimumOperations(nums) -> int:
        # Minimum operations
        operations = 0
        
        # Keep track of elements an their frequency in a list of size 101 
        # Since nums can have elements in the range from 0 to 100
        freq = [0] * 101
        for num in nums: freq[num] += 1
        
        # Sum of Minimums
        sumOfMinimums = 0
        
        # Minimum element
        minimumElement = 0
        
        # Loop over this new list
        i = 1
        while i < 101:
            
            # Skip 0 frequency elements 
            if freq[i] == 0: i += 1
                
            else:
			
                # Get the minimum element
                minimumElement = i - sumOfMinimums

                # Increment sumOfMinimums
                sumOfMinimums += minimumElement

                # Skip all elements <= sumOfMinimums
                while i < 101 and i <= sumOfMinimums: i += 1
				
				# Increment operation count
                operations += 1

        
        # Return the operations required
        return operations

nums = [1,5,0,3,5]

print("Output ->", minimumOperations(nums))