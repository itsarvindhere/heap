from heapq import heappop, heappush
from math import sqrt
from math import floor


def pickGifts(gifts, k: int) -> int:
        # Length of the list
        n = len(gifts)
        
        # Since at each second, we want the maximum value in the list
        # We can use a MaxHeap here which has the max value at any time on top
        maxHeap = []
        for gift in gifts: heappush(maxHeap, -gift)
            
        while k > 0:
            
            # Pop the top element (maximum gifts at this point)
            maxGifts = -heappop(maxHeap)
            
            # Leave behind the floor of the square root of the number of gifts
            giftsLeftBehind = floor(sqrt(maxGifts))
            
            # Push back
            heappush(maxHeap, -giftsLeftBehind)
            
            # If the number of gifts left behind are same as previous value, break early
            # Since in all next seconds, this index will always be the maximum
            # And in all cases, we will not take any gifts at all form this pile
            if giftsLeftBehind == maxGifts: break
            
            # Decrement k
            k -= 1
        
        
        # Get the sum of values in the maxHeap
        finalSum = 0
        while maxHeap: finalSum += -heappop(maxHeap)
        
        # Return the sum of values in the maxHeap
        return finalSum


gifts = [25,64,9,4,100]
k = 4

print("Output ->", pickGifts(gifts,k))