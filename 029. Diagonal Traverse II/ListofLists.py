def findDiagonalOrder(nums):
        # Output to return
        output = []
        
        # A list where each item will be another list that represents a group
        groups = []
        
        # How many rows are there
        rows = len(nums)
        
        # For each row
        for i in range(rows):
            
            # How many column are there in current row
            cols = len(nums[i])
            
            # Go over each column
            for j in range(cols):
                
                # Sum of row and column number
                # If the index is out of bounds
                if len(groups) == i + j: groups.append([])
                    
                # Push the number to its respective group
                groups[i + j].append(nums[i][j])
        
        # Now, we can fill the output list
        for stack in groups:
            while stack: output.append(stack.pop())
        
        # Return the output list
        return output


nums = [[1,2,3],[4,5,6],[7,8,9]]

print("Output -> ", findDiagonalOrder(nums))
