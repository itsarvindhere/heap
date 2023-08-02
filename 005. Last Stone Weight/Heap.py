from heapq import heapify, heappop, heappush


def lastStoneWeight(stones) -> int:
	# Max Heap - Element on the top of the largest at any time
        stones = [-stone for stone in stones]
        heapify(stones) 
        
        # Keep performing the operations till we are left with only one element in heap
        while len(stones) > 1:
            # Heaviest stone
            firstHeaviest = -heappop(stones)
            
            # Second heaviest stones
            secondHeaviest = -heappop(stones)
            
            # If both are different
            if firstHeaviest != secondHeaviest:
                
                # The new weight
                newWeight = firstHeaviest - secondHeaviest
                
                # Push this new weight to the heap
                # Heap will take care of putting it in its correct place
                heappush(stones, -newWeight)

        # Finally, return the weight of the only stone left
        return 0 if not stones else -stones[-1]


stones = [2,7,4,1,8,1]
print("Output ->", lastStoneWeight(stones))