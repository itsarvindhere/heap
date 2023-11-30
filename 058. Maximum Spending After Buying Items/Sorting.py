def maxSpending(values) -> int:
        
        # How many shops are there
        m = len(values)
        
        # How many items each shop has
        n = len(values[0])
        
        # Maximum amount that can be spent
        maxAmountSpent = 0
        
        items = []
        for i in range(m):
            for j in range(n): items.append(values[i][j])
        
        # Sort the items in increasing order
        items.sort()
        
        # Now, just calculate the maximum amount spent
        for i in range(m*n): maxAmountSpent += items[i] * (i + 1)
        
        # Return the maximum amount spent
        return maxAmountSpent

values = [[10,8,6,4,2],[9,7,5,3,2]]
print("Output -> ", maxSpending(values))