from collections import Counter
from heapq import heappop, heappush


def minSetSize(arr) -> int:
        # Length of the list
        n = len(arr)
        
        # We want to choose a set such that at least half of integers are removed
        # So, the best way would be to choose the integers that are occuring the most number of times
        # Because in that way, we can be sure that we will remove maximum possible integers
        # Ofcourse we can choose all the integers and so array will be empty
        # But, we want the minimum possible size of a set of integers to remove.
        
        # So, first we want the frequency of every value in the list
        count = Counter(arr)
        
        # Instead of filling a list first and then sorting it
        # We can use a maxHeap here and so as we put pairs in it, it will automatically order them
        maxHeap = []
        for key in count: heappush(maxHeap, (-count[key], key))
        
        # Count of elements removed
        # We want to remove at least "n/2" elements
        # That is, removedCount should be >= n/2
        removedCount = 0
        
        # Length of the set of removed elements
        setLength = 0
        
        # Main Logic
        while maxHeap:
            
            pair = heappop(maxHeap)
            
            # We remove all occurances of "val"
            # So removed Elements will increment by the frequency of "val"
            removedCount += -pair[0]
                
            # And length of set increases by 1
            setLength += 1
                
            # If we are already at threshold, return
            if removedCount >= n / 2: return setLength
        
        return setLength


arr = [3,3,3,3,5,5,5,2,2,7]
print("Output -> ", minSetSize(arr))