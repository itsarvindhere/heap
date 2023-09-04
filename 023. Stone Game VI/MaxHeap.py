from heapq import heappop, heappush


def stoneGameVI(aliceValues, bobValues) -> int:
        # How many stones
        n = len(aliceValues)
        
        # Instead of creating a list and then sorting it, we can use a maxHeap here
        maxHeap = []
        for i in range(n):heappush(maxHeap, (-(aliceValues[i] + bobValues[i]), i ))
        
        # Now, we can start playing the same
        aliceScore, bobScore = 0,0
        
        # To keep track of whose turn it is
        i = 0
        
        # While the maxHeap is not empty
        while maxHeap:
            
            # Most optimal stone index is on top of the maxHeap
            stoneIdx = heappop(maxHeap)[1]
            
            # Since alice starts first, each even value "i" represents Alice's turn
            if i % 2 == 0: aliceScore += aliceValues[stoneIdx]
            else: bobScore += bobValues[stoneIdx]
                
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