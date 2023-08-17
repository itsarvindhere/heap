from heapq import heappop, heappush


def maximumScore(a: int, b: int, c: int) -> int:
        
        # Maximum Score
        score = 0
        
        # The most optimal approach is to take the two piles with most number of stones in each step
        # We can use a maxHeap here that will give us the piles with the most number of stones
        maxHeap = []
        
        heappush(maxHeap, -a)
        heappush(maxHeap, -b)
        heappush(maxHeap, -c)
        
        # While there are at least two non-empty piles available
        while len(maxHeap) > 1:
            
            # Take the top two piles
            pile1 = -heappop(maxHeap)
            pile2 = -heappop(maxHeap)
            
            # Take one stone from each
            pile1 -= 1
            pile2 -= 1
            
            # Increment the score
            score += 1
            
            # Push back the values if they are not yet 0
            if pile1 > 0: heappush(maxHeap, -pile1)
            if pile2 > 0: heappush(maxHeap, -pile2)
                
        # Finally, return the maximum score
        return score

a = 2
b = 4
c = 6

print("Maximum Score -> ", maximumScore(a,b,c))