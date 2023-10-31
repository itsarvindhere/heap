from heapq import heappop, heappush
def eatenApples(apples, days) -> int:
        
		# Number of trees
        n = len(apples)
        
		# Count of Apples eaten
        count = 0
        
        # MinHeap
        minHeap = []
        
        i = 0 
        while i < n or minHeap:
            
            # Push the current data to the minHeap
			# We will order it based on the day when the apples rot
			# Basically, we want to eat those apples first that will rot first
            if i < n and apples[i] > 0: heappush(minHeap, [i + days[i], apples[i]])
            
            # Remove all those trees for which apples are already rotten
            while minHeap and minHeap[0][0] <= i: heappop(minHeap)
            
            # Now, we can choose the tree for which apples will rot first
            if minHeap:
                
                top = heappop(minHeap)

                # Eat one apple
                top[1] -= 1
                count += 1

                # If apples are still remaining in this tree, push it back to minHeap
                if top[1] > 0: heappush(minHeap, top)
                
            # Increment i
            i += 1
            
		# Finally, return the count of Apples Eaten
        return count

apples = [1,2,3,5,2]
days = [3,2,1,4,2]

print("Output -> ", eatenApples(apples,days))