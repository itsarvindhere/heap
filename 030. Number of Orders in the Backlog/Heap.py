from heapq import heappop, heappush
def getNumberOfBacklogOrders(orders):
        
        # Mod
        mod = 10**9 + 7
        
        # We want a maxHeap for the buy backlog and a minHeap for the sell backlog
        buyBacklog = []
        sellBacklog = []
        
        # Go over the orders
        for price,amount,orderType in orders:
            
            # If the order is a buy order
            if orderType == 0:
                
                # The order on top of sellBacklog will have the smallest price
                # So, if the price of that sell order is <= price of the current buy order
                while sellBacklog and sellBacklog[0][0] <= price:
                    top = heappop(sellBacklog)
                    
                    # Execute the order accordingly
                    if amount > top[1]:
                        amount -= top[1]
                    else:
                        top[1] -= amount
                        amount = 0
                        heappush(sellBacklog, top)
                        break
                
                # If we couldn't execute all the Buy orders, put the remaining orders in the buyBacklog
                if amount > 0: heappush(buyBacklog, [-price,amount,orderType])

            # If the order is a sell order
            else:
                
                # The order on top of buyBacklog will have the largest price
                # So, if the price of that buy order is >= price of the current sell order
                while buyBacklog and -buyBacklog[0][0] >= price:
                    top = heappop(buyBacklog)
                    
                    # Execute the order accordingly
                    if amount > top[1]:
                        amount -= top[1]
                    else:
                        top[1] -= amount
                        amount = 0
                        heappush(buyBacklog, top)
                        break
                        
                # If we couldn't execute all the Sell orders, put the remaining orders in the sellBacklog
                if amount > 0: heappush(sellBacklog, [price,amount,orderType])
                    
        # How many orders are left in backlog
        ordersLeft = 0
        
        while buyBacklog: ordersLeft += heappop(buyBacklog)[1]
        while sellBacklog: ordersLeft += heappop(sellBacklog)[1]
        
        # Finally, return the Number of orders left in the backlog
        return ordersLeft % mod


orders = [[10,5,0],[15,2,1],[25,1,1],[30,4,0]]

print("Output -> ", getNumberOfBacklogOrders(orders))