from heapq import heappop, heappush
def smallestChair(times, targetFriend):
        
        # The chair number to return for "target" friend
        chairNumberForTarget = -1
        
        # Number of friends
        n = len(times)
        
        # Sort the "times" by the arrival time 
        # Before sorting, also preserve the original indices
        times = [[times[i][0], times[i][1], i] for i in range(n)]
        times.sort()
        
        # When a friends arrives at "x", we want to check if there is a friend that leaves or has already left at that time
        # We can take that chair
        # So, let's use a minHeap to keep track of the "leaving" time of the friends from smallest to largest
        leavingTimes = []
        
        # Also, from all the available chairs, we want the one with the smallest number at any time so let's use a minHeap for this as well
        availableChairs = []
        
        # If available chairs minHeap is empty, we will keep assigning the lowest number chair to the friends
        # Initially, this number will be set to 0, the lowest possible chair number
        lowestChairNumberAvailable = 0
        
        # Go over each time value
        for arrival, leaving, i in times:
            
            # If there are friends with leaving times <= current "arrival" time
            # Then all those chairs are now empty at this point
            # So, we can put them all back in "availableChairs" list
            while leavingTimes and leavingTimes[0][0] <= arrival:
                top =  heappop(leavingTimes)
                
                # Since "availableChairs" is ordered by the chair number, 
                # the first value in each pair is top[1] since in "leavingTimes", chair number is the second value
                heappush(availableChairs,[top[1], top[0]])
                
            # Now we can take the chair with the smallest number from the "availableChairs" minHeap
            
            # If the "availableChairs" minHeap is empty, simply take the "lowestChairNumberAvailable"
            if not availableChairs:
                
                # If this is the "targetFriend", we can save the chair number on which he/she will sit
                if i == targetFriend: chairNumberForTarget = lowestChairNumberAvailable
                
                # Push this value in leavingTimes list for current person
                # We will push this data in leavingTimes (leavingTime, chairNumber)
                heappush(leavingTimes, [leaving, lowestChairNumberAvailable])
                
                # Increment chair number
                lowestChairNumberAvailable += 1
                
            # If we have "availableChairs" minHeap
            else:
                # The person sits at the chair with the smallest number
                top = heappop(availableChairs)
                
                # If this is the "targetFriend", we can save the chair number on which he/she will sit
                if i == targetFriend: chairNumberForTarget = top[0]
                    
                # Push this value in leavingTimes list for current person
                # We will push this data in leavingTimes (leavingTime, chairNumber)
                heappush(leavingTimes, [leaving, top[0]])
                
        # Finally, "chairNumberForTarget" will give us the required output
        return chairNumberForTarget


times = [[1,4],[2,3],[4,6]]
targetFriend = 1

print("Output ->", smallestChair(times,targetFriend))