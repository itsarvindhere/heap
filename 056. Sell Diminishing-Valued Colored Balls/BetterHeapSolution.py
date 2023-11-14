from heapq import heappop, heappush


def maxProfit(inventory, orders: int) -> int:
        mod = 10**9 + 7
        
        # Profit
        profit = 0
        
        # Max Heap
        maxHeap = []
        
        # Fill the Max Heap
        for val in inventory: heappush(maxHeap, -val)
            
        # While we have orders pending
        while orders > 0:
            
            # Get the two greatest values from the heap, if they exist
            firstGreatest = -heappop(maxHeap)
            
            # If there is only one value, consider secondGreatest to be 0
            secondGreatest = 0
            
            # Otherwise, get the second greatest value
            if maxHeap: secondGreatest = -maxHeap[0]
                
            # Now, for how many orders we can choose the "firstGreatest" value
            orderCountForSameBall = firstGreatest - secondGreatest + 1
            
            # Since we only want to sell "orders" balls
            orderCountForSameBall = min(orderCountForSameBall, orders)
            
            # First, let's find the sum from "1" to "15" or from "1" to "firstGreatest"
            sum1 = (firstGreatest * (firstGreatest + 1)) // 2
            
            # Seconds, let's find the sum from "1" to "10" or from "1" to "firstGreatest - orderCountForSameBall"
            sum2 = ((firstGreatest - orderCountForSameBall) * ((firstGreatest - orderCountForSameBall) + 1)) // 2
            
            # So, the profit will be "sum1 - sum2"
            sumDifference = (sum1 - sum2) % mod
            
            profit = (profit + sumDifference) % mod
            
            # Put the "firstGreatest" back to the maxHeap if it is not already 0 after executing the orders
            if firstGreatest - orderCountForSameBall > 0: heappush(maxHeap, -(firstGreatest - orderCountForSameBall))
                
            # And reduce the order count
            orders -= orderCountForSameBall
                
        # Finally, return the profit
        return profit

inventory = [4,2,7,1]
orders = 6

print("Output ->", maxProfit(inventory, orders))