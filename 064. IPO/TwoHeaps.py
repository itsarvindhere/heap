from heapq import heappush, heappop
def findMaximizedCapital(k: int, w: int, profits, capital) -> int:
        
        # Finished projects
        finishedProjects = set()
        
        # Number of projects
        n = len(profits)
        
        # A Max Heap to order the projects by the profit from maximum to minimum
        maxHeap = []
        
        # Another heap to order the projects by the capital from minimum to maximum
        # This will be used for those projects that we cannot take up at some point
        # But they might be available to pick once we have enough capital
        minHeap = []
        
        # Fill the maxHeap and minHeap
        for i in range(n): 
            # If capital required is <= w, we can push it to the maxHeap as we can take it up
            if capital[i] <= w: heappush(maxHeap, [-profits[i], capital[i]])
                
            # Otherwise, we have to wait till we get enough capital
            # Hence, we push it to the minHeap
            else: heappush(minHeap, [capital[i], profits[i]])
        
        # We can finish at most "k" projects
        while k > 0:
                
            # If there are projects in the minHeap
            # Move them back into the maxHeap if their capital required is <= w
            while minHeap and minHeap[0][0] <= w: 
                top = heappop(minHeap)
                heappush(maxHeap, [-top[1], top[0]])
                
            # At this point, the top of maxHeap has the most suitable project that we can take up
            # But, if the heap is empty, it means we cannot take up any project so we can break
            if not maxHeap: break
                
            # Pick the project on top of the maxHeap
            top = heappop(maxHeap)
            
            # Update the capital by the profit from this project
            w += -top[0]
            
            # Update k
            k -= 1
        
        # Finally, return the Final Maximized Capital
        return w

k = 3
w = 0
profits = [1,2,3]
capital = [0,1,2]

print("Output is ->", findMaximizedCapital(k, w, profits, capital))