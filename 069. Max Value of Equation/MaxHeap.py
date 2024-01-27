from heapq import heappush, heappop
def findMaxValueOfEquation(points, k: int) -> int:
        
        # Number of points
        n = len(points)
        
        # So, for each pair [xj,yj], we simply need the maximum value for (yi - xi) where
        # xi - xj is <= k
        maxValue = float("-inf")
        
        # So, we can use a Max Heap here
        # Initially, it will have the pair [(yi - xi),xi] for the point at index 0
        maxHeap = [[-(points[0][1] - points[0][0]), points[0][0]]]
            
        # Now, we will loop over each point, starting from index 1
        for i in range(1,n):
            
            # Because the list is sorted in increasing order of "x" values
            # If xj - xi is not <= k for current point and point on top of maxHeap
            # Then it cannot be <= k for any upcoming point as well
            # So, we can discard it from the maxHeap in this case
            while maxHeap and points[i][0] - maxHeap[0][1] > k: heappop(maxHeap)
                
            # If the heap is not empty at this point, it means we have a valid pair
            if maxHeap: maxValue = max(maxValue, -maxHeap[0][0] + points[i][0] + points[i][1])
                
            # Push the current point into the maxHeap
            heappush(maxHeap, [-(points[i][1] - points[i][0]), points[i][0]])
            
        return maxValue

points = [[1,3],[2,0],[5,10],[6,-10]]
k = 1
print("Output ->", findMaxValueOfEquation(points,k))