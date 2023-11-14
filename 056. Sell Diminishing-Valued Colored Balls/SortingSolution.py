def maxProfit(inventory, orders: int) -> int:
        
        # Mod
        mod = 10**9 + 7
        
        # Max Profit
        profit = 0
        
        # Sort the list in decreasing order
        inventory.sort(reverse=True)
        
        # Go over each ball's "quantity" in the inventory
        
        # Number of different colored balls
        n = len(inventory)
        
        # Main Logic
        for i in range(n):
            
            # What is the difference in the quantities bettwen "i" and "i + 1" ball?
            difference = inventory[i] - (inventory[i + 1] if i < n - 1 else 0)
            
            # How many different colored balls we have traversed so far
            ballsTraversedSoFar = i + 1
            
            # How many balls we can sell at this point?
            availableBallsToSell = ballsTraversedSoFar * difference
            
            # If we can sell all the available balls at this point
            if availableBallsToSell < orders:
                
                # What is the profit that we can generate 
                # from selling "difference" balls of "i" color?
                # That would be sum of values between [inventory[i], inventory[i] - difference]]
                # We can use the "Sum of N natural numbers" formula to get this sum quickly
                
                # Sum from "1" to "inventory[i]"
                sum1 = (inventory[i] * (inventory[i] + 1)) // 2
                
                # Sum from "1" to "inventory[i] - difference"
                sum2 = ((inventory[i] - difference) * ((inventory[i] - difference) + 1)) // 2
                
                # Profit from selling "difference" balls of "i" color
                profitFromOne = (sum1 - sum2) % mod
                
                # So, total profit from selling "availableBallsToSell" balls is
                totalProfitFromSellingBalls = (ballsTraversedSoFar * profitFromOne) % mod
                
                # So, increment profit
                profit = (profit + totalProfitFromSellingBalls) % mod
                
                # Reduce orders
                orders -= availableBallsToSell
            
            # If we cannot sell all the available balls at this point
            else:
                
                ballsTakenFromEachColor = orders // ballsTraversedSoFar
                remaining = orders % ballsTraversedSoFar
                
                # We have to sell "ballsTakenFromEachColor" balls from each color traversed so far
                # So, if we can find the profit by selling "ballsTakenFromEachColor" balls for one color
				# We can easily find total profit from selling "ballsTakenFromEachColor" balls from "ballsTraversedSoFar" colors
                
                # Again, we can use the Sum of N Natural Numbers formula
                
                # Sum from "1" to "inventory[i]"
                sum1 = (inventory[i] * (inventory[i] + 1)) // 2
                
                # Sum from "1" to "inventory[i] - ballsTakenFromEachColor"
                sum2 = ((inventory[i] - ballsTakenFromEachColor) * ((inventory[i] - ballsTakenFromEachColor) + 1)) // 2
                
                # Profit from one color
                profitFromOne = (sum1 - sum2) % mod
                
                # So, if "profitFromOne" is the profit from selling "x" amount of balls of some color
                # Then, what is the total profit from selling "x" amount of balls of all the colors we have traversed?
                totalProfitFromSellingBalls = (ballsTraversedSoFar * profitFromOne) % mod
                
                # Also, don't forget the remaining balls that we need to take
                profitFromSellingRemainingBalls = remaining * (inventory[i] - ballsTakenFromEachColor)
                
                # Update total profit
                totalProfitFromSellingBalls = (totalProfitFromSellingBalls + profitFromSellingRemainingBalls) % mod
                
                # Increment profit
                profit = (profit + totalProfitFromSellingBalls) % mod
                
                # We are done!
                break

        # Finally, return the maximum profit
        return profit

inventory = [4,2,7,1]
orders = 6

print("Output ->", maxProfit(inventory, orders))