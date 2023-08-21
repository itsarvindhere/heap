from heapq import heappop, heappush
from math import sqrt
def kClosest(points, k):
        # Length of the list
        n = len(points)
        
        # MaxHeap
        maxHeap = []
        
        # For each point, calculate its distance with the origin
        for i in range(n):
            # X and Y value for current point
            x,y = points[i][0], points[i][1]
            
            # Distance from origin
            distance = sqrt(x**2 + y**2)
            
            # Put the distance and the point in the maxHeap
            heappush(maxHeap, (-distance, points[i]))
            
            # If the maxHeap size exceeds k, pop from the top
            if len(maxHeap) > k: heappop(maxHeap)

        # In the end, maxHeap will have the "k" closest points to origin
        return [pair[1] for pair in maxHeap]


points = [[3,3],[5,-1],[-2,4]]
k = 2

print("Output -> ", kClosest(points,k))