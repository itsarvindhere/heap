from heapq import heappop, heappush


def furthestBuilding(heights, bricks: int, ladders: int) -> int:
        # How many buildings
        n = len(heights)
        
        # Max Heap to keep track of how many bricks were used for a jump
        # So that we can quickly get the maximum bricks used for a jump
        maxHeap = []
        
        i = 1
        
        # Go over the heights list
        while i < n:
            
            # What is the height difference between current and previous building
            heightDifference = heights[i] - heights[i - 1]
             
            # If the height difference is <= 0, no need to use ladder or bricks
            if heightDifference <= 0: 
                i += 1
                continue
                
            # If we don't have enough bricks to make the current jump
            # We can check if in any previous jump we used more bricks than current heightDifference
            # If yes, then we can use a ladder in place of those bricks and use those bricks here in current jump
            while maxHeap and -maxHeap[0] > heightDifference and ladders > 0 and bricks < heightDifference:
                bricks += -heappop(maxHeap)
                ladders -= 1
                
            # If we have bricks available, make a jump
            if bricks >= heightDifference: 
                bricks -= heightDifference
                heappush(maxHeap, -heightDifference)
                i += 1
            # If we don't have bricks available, check if we have ladders available
            elif ladders > 0:
                ladders -= 1
                i += 1
            # If we don't have bricks or ladders available, we cannot make the jump at all
            else: break
        
        # Finally, return the furthest building we reached
        return i - 1

heights = [4,12,2,7,3,18,20,3,19]
bricks = 10
ladders = 2

print("Output ->", furthestBuilding(heights, bricks, ladders))