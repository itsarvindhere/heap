from math import sqrt
from math import floor


def pickGifts(gifts, k: int) -> int:
        # Length of the list
        n = len(gifts)
        
        # Index of pile with maximum number of gifts
        maxIdx = 0
        for i in range(n): 
            if gifts[i] > gifts[maxIdx]: maxIdx = i
        
        # Run the loop for "k" seconds
        while k > 0:
            
            # Now, take the required gifts from index "maxIdx"
            # And leave behind the floor of sqrt of the gifts[maxIdx]
            gifts[maxIdx] = floor(sqrt(gifts[maxIdx]))
            
            # Now, we want the new maximum index pile
            for i in range(n): 
                if gifts[i] > gifts[maxIdx]: maxIdx = i
            
            # Reduce the seconds (k)
            k -= 1
        
        # Return the sum of values in the list
        return sum(gifts)


gifts = [25,64,9,4,100]
k = 4

print("Output ->", pickGifts(gifts,k))