def stoneGameVI(aliceValues, bobValues) -> int:
        # How many stones
        n = len(aliceValues)
        
        # Let's combine the values in a single list with each index having a pair
        # Each pair will be like this => (value of stone as per alice, value of stone as per bob)
        values = [(aliceValues[i], bobValues[i]) for i in range(n)]
        
        # We will sort by the sum of aliceValues and bobvalues for each stone
        values.sort(key = lambda x: x[0] + x[1])
        
        # Now, we can start playing the same
        aliceScore, bobScore = 0,0
        
        # To keep track of whose turn it is
        i = 0
        
        # While the values list is not empty
        while values:
            
            # Most optimal pair in the values list is the last pair
            pair = values.pop()
            
            # Since alice starts first, each even index "i" represents Alice's turn
            if i % 2 == 0: aliceScore += pair[0]
            else: bobScore += pair[1]
                
            # Increment i
            i += 1
        
        # Now, return the output based on the scores
        # If both have same score, return 0
        if aliceScore == bobScore: return 0
        
        # If alice has a higher score than bob, return 1
        elif aliceScore > bobScore: return 1
        
        # Otherwise, return -1
        return -1


aliceValues = [2,4,3]
bobValues = [1,6,7]
print("Output -> ", stoneGameVI(aliceValues, bobValues))