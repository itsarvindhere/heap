from heapq import heappop, heappush
def miceAndCheese(reward1, reward2, k: int) -> int:
        # Points
        points = 0
        
        # Types of cheese
        n = len(reward1)
        
        # A Max Heap that orders the reward based on the difference between reward1 and reward2
        maxHeap = []
        
        # Fill the maxHeap
        for i in range(n): heappush(maxHeap, [-(reward1[i] - reward2[i]), reward1[i], reward2[i]])
        
        # First mouse eats "k" type of cheese
        while k > 0:
            points += heappop(maxHeap)[1]
            k -= 1
            
        # Now, the rest of the cheese is eaten by second mouse
        while maxHeap: points += heappop(maxHeap)[2]
        
        # Finally, return the points
        return points

reward1 = [1,1,3,4]
reward2 = [4,4,1,1]
k = 2

print("Output ->", miceAndCheese(reward1, reward2, k))
