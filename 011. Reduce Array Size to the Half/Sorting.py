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
        
        # Take a list now and put every element with its freq in this list
        freqList = []
        
        for key in count: freqList.append((count[key], key))
            
        # Sort this list in decreasing order
        freqList.sort(reverse=True)
        
        # Count of elements removed
        # We want to remove at least "n/2" elements
        # That is, removedCount should be >= n/2
        removedCount = 0
        
        # Length of the set of removed elements
        setLength = 0
        
        # Main Logic
        for pair in freqList:
            
            # We remove all occurances of "val"
            # So removed Elements will increment by the frequency of "val"
            removedCount += pair[0]
                
            # And lengfth of set increases by 1
            setLength += 1
                
            # If we are already at threshold, return
            if removedCount >= n / 2: return setLength
        
        return setLength


arr = [3,3,3,3,5,5,5,2,2,7]
print("Output -> ", minSetSize(arr))