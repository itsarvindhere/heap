from collections import Counter
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
        
        # We would also need to then first choose elements that occur most number of times
        # So, to avoid manually sorting later, let's use bucket sort here
        # Because, we know that for a list of size "n", an element can occur at most "n" times only
        freqList = [[] for i in range(n)]
        
        for key in count: freqList[count[key] - 1].append(key)
        
        # Count of elements removed
        # We want to remove at least "n/2" elements
        # That is, removedCount should be >= n/2
        removedCount = 0
        
        # Length of the set of removed elements
        setLength = 0
        
        # We loop freqList in reverse since we want to chhose the elements that occur most frequency
        for i in range(n - 1, -1, -1):
            # If there are elements that occur "i + 1" times
            # Remove all the occurances of those elements till removedCount is not >= n / 2
            for val in freqList[i]:
                # We remove all occurances of "val"
                # So removed Elements will increment by the frequency of "val"
                removedCount += (i  + 1)
                
                # And lengfth of set increases by 1
                setLength += 1
                
                # If we are already at threshold, return
                if removedCount >= n / 2: return setLength
        
        return setLength


arr = [3,3,3,3,5,5,5,2,2,7]
print("Output -> ", minSetSize(arr))