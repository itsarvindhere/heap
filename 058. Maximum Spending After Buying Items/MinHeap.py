from heapq import heappop, heappush
def maxSpending(self) -> int:
        
        # How many shops are there
        m = len(values)
        
        # How many items each shop has
        n = len(values[0])
        
        # Maximum amount that can be spent
        maxAmountSpent = 0
        
        # Instead of having to first get all the items and then sort them
        # We can also use a MinHeap that does this sorting automatically as we put items in it
        items = []
        for i in range(m):
            for j in range(n): heappush(items,values[i][j])
        
        # Now, just calculate the maximum amount spent
        day = 1
        while items: 
            maxAmountSpent += heappop(items) * day
            day += 1
        
        # Return the maximum amount spent
        return maxAmountSpent

values = [[10,8,6,4,2],[9,7,5,3,2]]
print("Output -> ", maxSpending(values))