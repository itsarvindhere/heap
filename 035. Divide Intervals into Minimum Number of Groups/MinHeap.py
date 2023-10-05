from heapq import heappop, heappush


def minGroups(intervals) -> int:
        
        # How many intervals we have
        n = len(intervals)
        
        # Sort the intervals in increasing order based on left value
        intervals.sort()
        
        # Now, since the intervals are sorted, it means
        # For any two intervals, we can say that the one on right start at or after the one on left ends
        # And in this way, it is easier to check if the interval on right is overlapping with the interval on left
        # If it is, then we cannot put them in the same group
        # But if they are not overlapping, they both will go in the same group
        
        # Min Heap to get the smallest "right" value so far and compare it with the "left" value of current interval
        minHeap = []
        
        for interval in intervals:
            
            # Since it is a minHeap, it will always have the smallest "right" value so far on top
            # If the minHeap has a value on top, and the current interval's "left" value is greater than the top value
            # What does it mean? It just means, current interval does not overlap with the interval that is on top of heap
            # So, both can be put in the same group
            # And since we have already sorted the list in increasing order, we know that now we no longer require the value 
            # that is on top of the heap because it is going in same group as current interval
            # So, instead, we will push the "right" value of current interval in the minHeap and remove the top value
            if minHeap and minHeap[0] < interval[0]: heappop(minHeap)
                
            heappush(minHeap, interval[1])
                
        # Finally, the length of the minHeap will be same as number of groups we have to make
        # Because in the end, the minHeap will have the "right" values for all the "last" intervals of each group
        return len(minHeap)

intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]

print("Minimum Groups ->", minGroups(intervals))