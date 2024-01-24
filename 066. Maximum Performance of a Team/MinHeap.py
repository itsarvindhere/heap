from heapq import heappush, heappushpop
def maxPerformance(n: int, speed, efficiency, k: int) -> int:
        
        # Mod
        mod = 10**9 + 7
        
        # Aggregate the two lists
        data = [[efficiency[i], speed[i]] for i in range(n)]
        
        # Sort the list in decreasing order, based on efficiency
        data.sort(reverse=True)
        
        # Maximum performance value to return
        maxPerformanceValue = 0
        
        # To keep track of the sum of speeds of the "k" engineers
        sumOfSpeeds = 0
        
        # Use a min heap to keep track of the top k speed values
        minHeap = []
        for i in range(k): 
            heappush(minHeap, data[i][1])
            sumOfSpeeds += data[i][1]
            
            # It is important to note that the problem says "At most k" engineers
            # It means, there can also be less than "k" engineers to get the maximum performance
            # Hence, we have to update the maxPerformanceValue here as we iterate over the engineers
            # The minimum efficiency will always be the efficiency of the "i" engineer
            # And the sum of speeds is something we are already tracking as we iterate
            maxPerformanceValue = max(maxPerformanceValue, sumOfSpeeds * data[i][0])

        # Now, we can start from the "kth" value and iterate till the end of the list
        for i in range(k,n):
            
            # Push the current engineer's speed value to the minHeap
            # And since we want to maintain the heap size as "k", 
            # we will also pop the smallest sum value in the minHeap from its top
            removedVal = heappushpop(minHeap, data[i][1])
            
            # Increment the sumOfSpeeds by the current engineer's sum
            sumOfSpeeds += data[i][1]
            
            # Decrement the sumOfSpeeds by the removed speed value
            sumOfSpeeds -= removedVal
            
            # Update the maximum performance value accordingly
            maxPerformanceValue = max(maxPerformanceValue, sumOfSpeeds * data[i][0])
        
        # Return the maximum performance value
        return maxPerformanceValue % mod

n = 6
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k = 2

print("Output -> ", maxPerformance(n,speed,efficiency,k))