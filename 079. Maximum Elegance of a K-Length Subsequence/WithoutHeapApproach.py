def findMaximumElegance(items, k: int) -> int:
        
        # Length of the list
        n = len(items)
        
        # Sort the items by profit in decreasing order
        items.sort(reverse=True)
        
        # Get the first "k" items for the first subsequence
        # This will ensure that we have the "k" items with maximum profit
        # Also, to keep track of each category we can use a set
        # This will help us to check if a category is already present in current subsequence or not
        categories = set()
        
        # Total profit
        totalProfit = 0
        
        # A simple list track of the items based on their profits from smallest to largest
        # There is no need to use a Heap because since the list is sorted based on profits already
        # The candidate list will also be sorted in decreasing order
        # So at any time, the best item to replace will be at the end of the list
        candidates = []
        
        for i in range(k):
            
            # Update the profit so far
            totalProfit += items[i][0]
            
            # if this category already exists in the subsequence so far
            if items[i][1] in categories:
                
                # Put the item into the candidates list
                candidates.append(items[i][0])
            
            # Add to the set
            categories.add(items[i][1])
            
        # Maximum Elegance
        # Initialize it with the current elegance
        maxElegance = totalProfit + (len(categories) ** 2)
        
        # Now, we go over the rest of the values
        for i in range(k,n):
            
            # If the candidates list is empty, there is no item left to replace, so we can return the maxElegance here
            if not candidates: return maxElegance
            
            # If current item has a category that is not already present in the current subsequence
            # Then, we can replace the item at the end of candidates list with this item
            # Since we have sorted the list by the profit initially
            # It also means current item is the item with highest profit among all items of its category
            if items[i][1] not in categories:
                
                # We can replace the item
                # Hence, pop the item at the end of candidates list
                top = candidates.pop()
    
                # If current item is added to the subsequence, what will be the new total profit
                newTotalProfit = totalProfit - top + items[i][0]
                
                # The count of distincts will increase by 1
                newDistinctCount = len(categories) + 1
                
                # So, what will be the new elegance
                newElegance = newTotalProfit + (newDistinctCount ** 2)
                
                # Add the current category to the set
                categories.add(items[i][1])
                
                # Update the total profit
                totalProfit = newTotalProfit

                # If new elegance is higher than maxElegance so far
                maxElegance = max(maxElegance, newElegance)
        
        # Return the maximum elegance
        return maxElegance


items = [[3,2],[5,1],[10,1]]
k = 2

print("Output ->", findMaximumElegance(items,k))