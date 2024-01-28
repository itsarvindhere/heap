from heapq import heappush, heappop
from sortedcontainers import SortedList
def busiestServers(k: int, arrival, load):
        
        # How many requests are there
        n = len(arrival)
        
        # We will use a Sorted List to keep track of the available servers and their indices
        availableServers = SortedList()
        
        # Initially, all servers are available
        for i in range(k): availableServers.add(i)
        
        # A queue-like data structure that will be used to keep track of all the busy servers
        # This will order the servers by the time at which they will be available again (from smallest to largest)
        # So, it will be a MIN HEAP
        busyServers = []
        
        # A dictionary to keep track of how many requests each server handled
        requestCount = {}
        
        # We will go over the arrival times from left to right
        for i in range(n):
            
            # First, check if there are servers in the "busyServers"  Min Heap
            # That should be available by the current arrival time
            # If yes, then move them back to the available servers list
            while busyServers and busyServers[0][0] <= arrival[i]: 
                
                # Index of the server on top of "busyServers" Min Heap
                idx = heappop(busyServers)[1]
                
                # Add the server back to the "availableServers" Sorted List
                availableServers.add(idx)
                
            # If no servers are available, drop the current request
            if not availableServers: continue
                
            # Now, for the current request "i", we are looking for the most optimal server
            # And that server is "i % k"
            # If "i%k" is not available, we can use "i%k" + 1... and so on till we reach the end
            # Because if we reach the end, we have to then pick a server from the beginning, if available
            # So basically, we want the leftmost index of server in our "availableServers" list that is >= i % k
            # So, we can use Binary Search here since we have a "SORTED LIST"
            
            leftmostIndex = -1
            
            start,end = 0, len(availableServers) - 1
            
            while start <= end:
                mid = start + (end - start) // 2
                
                # Does the server at "mid" have index >= i % k?
                # If yes, then save it and keep searching on left side of mid
                if availableServers[mid] >= i % k:
                    leftmostIndex = mid
                    end = mid - 1
                    
                # Otherwise, look for a server on the right side of mid
                else: start = mid + 1
                    
            # If leftmostIndex is -1 at this point, it means we will have to look at the servers, starting from index 0
            # That is, we are now wrapping around the list of server starting from 0
            # And well, since "availableServers" list is already sorted, it means that would be the first server in this list
            if leftmostIndex == -1: leftmostIndex = 0
                
            # The server at "leftmostIndex" will process the current request and so, we push it to the "busyServers" Min Heap
            idx = availableServers.pop(leftmostIndex)
            
            # The time at which it will be available again is -> arrival time + load time
            heappush(busyServers, [arrival[i] + load[i], idx])
            
            # Update the dictionary
            requestCount[idx] = requestCount.get(idx,0) + 1       

        # What is the maximum count of requests handled
        maxCount = max(requestCount.values())

        # Return all the servers that handles "maxCount" number of requests     
        return [key for key in requestCount if requestCount[key] == maxCount]


k = 3
arrival = [1,2,3,4,5]
load = [5,2,3,3,3]
print("Output ->", busiestServers(k, arrival ,load))